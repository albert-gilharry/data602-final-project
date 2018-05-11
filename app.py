# -*- coding: utf-8 -*-
"""
DATA 602 Assignment Final Project: Crypto Trading
Authors: 
    Jagruit Salao
    Harpreet Shocker
    Albert Gilharry
"""

import os
from flask import Flask, render_template, request
import pandas as pd
from requests import get
import json
from pymongo import MongoClient
import urllib.parse
import numpy as np
import mysql.connector
from mysql.connector import MySQLConnection, Error
app = Flask(__name__)

class Recommender:
    
    
    def __init__(self):
        self.dbCon=self.connect()
        self.department_dist = {"departments":[], "orders":[]}
            
    def getVisuals(self):
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
        
        return {"aisles":aisles_dist,"doweek":dow_dist,"hour_of_day":hour_dist,
                "num_orders":num_orders, 
                "num_users":num_users,
                "num_products":num_products,
                "top_product":top_product}
        
    
    def sampleUsers(self):
        cursor = self.dbCon.cursor()
        cursor.execute("SELECT orders.order_dow, COUNT(*) as orders FROM orders GROUP BY orders.order_dow ORDER BY order_dow ASC")
        rows = cursor.fetchmany(20)
       
        return {"success":True, "data":rows}
    
    
    def recommend(self,user_id):
        cursor = self.dbCon.cursor()
        cursor.execute("SELECT products.product_id, " +  
                       "products.product_name, " + 
                       "departments.department, " + 
                       "aisles.aisle " + 
                       "FROM products " +
                       "INNER JOIN departments ON (departments.department_id = products.department_id) " +
                       "INNER JOIN aisles ON (aisles.aisle_id = products.aisle_id) " + 
                       "ORDER BY RAND() LIMIT 10")
        
        rows = cursor.fetchmany(10)
       
        return {"success":True, "data":rows}
        
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host="200.32.198.69", 
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

@app.route("/methodology")
def methodology():
    return render_template('methodology.html')

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