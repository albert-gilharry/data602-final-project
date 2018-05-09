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
        cursor.execute("SELECT * FROM departments_distribution")
        rows = cursor.fetchall()

        department_dist = {"success":True,"departments":[], "orders":[]}
        for row in rows:
            department_dist['departments'].append(row[1])
            department_dist['orders'].append(row[2])
            
        dow_dist = {"success":True,"dow":["Sunday",
                                          "Monday",
                                          "Tuesday",
                                          "Wednesday",
                                          "Thursday",
                                          "Friday",
                                          "Saturday"], "orders":[]}
        for row in rows:
            department_dist['departments'].append(row[1])
            department_dist['orders'].append(row[2])
            
       
            
        return {"dept":department_dist}
        
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)