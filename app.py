# -*- coding: utf-8 -*-
"""
DATA 602 Assignment Final Project: Instacart Basket
Authors: 
    Jagruti Salao
    Harpreet Shocker
    Albert Gilharry
"""

from flask import Flask, render_template, request
import json
import numpy as np
import mysql.connector
from mysql.connector import MySQLConnection, Error
import graphlab as gl

app = Flask(__name__)

class Recommender:
    
    item_similarity_top_k = 0
    def __init__(self):
        self.dbCon=None
        self.department_dist = {"departments":[], "orders":[]}
        self.item_similarity_top_k = gl.load_sframe('/home/ec2-user/insta/data/item_similarity_top_5_model')
     
    # Get the recommended top 5 products per user    
    def topFiveProductRecommendationForUser( self, user_id):
        recommendedValue = self.item_similarity_top_k[self.item_similarity_top_k['user_id'] == user_id ]
        return list(recommendedValue["item_id"].astype(str))
	
    # Create dashboard visuals
    # Data is gathered from a MYSQL Database on EC2 and sent to the browser and vsiuals are generated using Highcharts.js	
    def getVisuals(self):
        self.dbCon=self.connect()
        cursor = self.dbCon.cursor()
        cursor.execute("SELECT * FROM aisles_distribution ORDER BY aisles_distribution.orders DESC LIMIT 25")
        rows = cursor.fetchall()

        aisles_dist = {"success":True,"data":[]}
        for row in rows:
            aisles_dist['data'].append([row[1],row[2]])
            
            
        cursor.execute("SELECT orders.order_hour_of_day, COUNT(*) as orders FROM orders GROUP BY orders.order_hour_of_day ORDER BY order_hour_of_day ASC")
        rows = cursor.fetchall()

        hour_dist = {"success":True,"hour":[], "orders":[]}
        for row in rows:
            hour_dist['hour'].append(row[0])
            hour_dist['orders'].append(row[1])
        
        
        cursor.execute("SELECT orders.order_dow, COUNT(*) as orders FROM orders GROUP BY orders.order_dow ORDER BY order_dow ASC")
        rows = cursor.fetchall()
        dow_dist = {"success":True, "data":[]}

        days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]
        i = 0;
        for row in rows:
            dow_dist['data'].append({"name": days[i],"y":row[1]})
            i = i + 1
            
        
        cursor.execute("SELECT COUNT(*) AS num_orders, COUNT(DISTINCT user_id) AS num_users FROM orders;")
        row = cursor.fetchone()
        num_orders = row[0]
        num_users = row[1]
        
        cursor.execute("SELECT COUNT(*) AS num_products FROM products;")
        row = cursor.fetchone()
        num_products= row[0]
        
        cursor.execute("SELECT * FROM products_distribution ORDER BY orders DESC LIMIT 1;")
        row = cursor.fetchone()
        top_product = row[1]
        self.dbCon.close()
        return {"aisles":aisles_dist,"doweek":dow_dist,"hour_of_day":hour_dist,
                "num_orders":num_orders, 
                "num_users":num_users,
                "num_products":num_products,
                "top_product":top_product}
        
    # Get a sample of users to reduce load on the interface
    def sampleUsers(self):
        users = np.array(list(self.item_similarity_top_k['user_id']))
        users = np.unique(users)
        users = np.random.choice(users, 10, replace=False).reshape(10,1).tolist()
        return {"success":True, "data":users}
    
    # Send recommendations along with additonal product information to the browswer 
    def recommend(self,user_id):
        recommendedValue = self.item_similarity_top_k[self.item_similarity_top_k['user_id'] == int(user_id) ]
        data = list(recommendedValue["item_id"].astype(str))
        recommendations = ",".join( data )
        print("recommendations: " + recommendations)
        self.dbCon=self.connect()
        cursor = self.dbCon.cursor()
        cursor.execute("SELECT products.product_id, " +  
                       "products.product_name, " + 
                       "departments.department, " + 
                       "aisles.aisle " + 
                       "FROM products " +
                       "INNER JOIN departments ON (departments.department_id = products.department_id) " +
                       "INNER JOIN aisles ON (aisles.aisle_id = products.aisle_id) " +
                       "WHERE products.product_id IN (" + recommendations + ") ")
        
        rows = cursor.fetchmany(10)
        self.dbCon.close()
        return {"success":True, "data":rows}        
        
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host="54.172.68.230", 
                                           user="insta_user", 
                                           password="Inst@User!",
                                           db="insta_cart")
            if conn.is_connected():
                return conn
     
        except Error as e:
            print(e)
            exit()
 
recommender = Recommender()       

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('index.html')

@app.route("/recommendations")
def recommendations():
    return render_template('recommendations.html')

@app.route("/getGraphics",methods=['GET'])
def getGraphics():
    graphics = recommender.getVisuals()
    return json.dumps(graphics) 

@app.route("/sampleUsers",methods=['GET'])
def sampleUsers():
    sample = recommender.sampleUsers()
    return json.dumps(sample) 

@app.route("/getRecommendations",methods=['POST'])
def getRecommendations():
    user_id = request.form['user']
    recommendations = recommender.recommend(user_id)
    return json.dumps(recommendations) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
