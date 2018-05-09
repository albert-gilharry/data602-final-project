# -*- coding: utf-8 -*-
"""
DATA 602 Assignment Final Project: Crypto Trading
Authors: 
    Jagruit Salao
    Harpreet Shocker
    Albert Gilharry
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import datetime
import time
from flask import Flask, render_template, request
import pandas as pd
from requests import get
import json
import pymongo
from pymongo import MongoClient
import urllib.parse
import numpy as np
import random
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima_model import ARIMA
from scipy.optimize import minimize
import warnings
import itertools

app = Flask(__name__)

class Recommender:
    

    def __init__(self):
        return 0
        
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

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)