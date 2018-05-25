

## Project Title:
### Instacart Market Basket Analysis

This project is final course work for DATA602 (Advanced programming Techniques).
Instacart market basket analysis is kaggle competition launched to use the anonymized data gathered by Instacart on 
customer orders over time to predict which previously purchased products will be in a user’s next order. 
source link : https://www.kaggle.com/c/instacart-market-basket-analysis

## Pre-requisites:

#### Libraries: 
numpy

matplotlib

flask

pandas

requests

mysql-connector-python

## Installations:
1) MySQL

For Windows:

https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html

For MacOS:

https://sequelpro.com/docs/ref/mysql/install-on-osx

2) Graphlab:

Details on Graphlab and how to install:

https://www.analyticsvidhya.com/blog/2015/12/started-graphlab-python/


## Url for App:

http://54.172.68.230:5000

## How it works:

The app is designed with two tabs:

### 1) Dashboard:
Dashboard mentions details three visuals and summary of dataset provided.

a) Orders by time of day.
b) Orders by time of week
c) Popular aisles in customers
 

### 2) Product Recommendations:
 Offers five recommended products(with product ID,Product,Department,Aisle) for customer selected from drop down tab.
 
 
## Prediction model:

![Item Descriptive Stats](https://github.com/albert-gilharry/data602-final-project/blob/master/images/des_stats.jpg "Description goes here")

![Items Distribution](https://github.com/albert-gilharry/data602-final-project/blob/master/images/item_distribution.jpg "Description goes here")

![User To Item Heat Map](https://github.com/albert-gilharry/data602-final-project/blob/master/images/heat_map.jpg "Description goes here")


## Built with:

Python 3.0 Flask Framework

Web Framework : Bootstrap(https://getbootstrap.com/. )

Handling requests(Flask Application) : JQuery and custom Javascript

Plots :Javascript library Highcharts.js(https://www.highcharts.com/)

Data storage: MySQL

## Deployment

#### To run the App: 

docker run -p 5000:5000 albertgilharry/data602-final-project

#### Docker image : 

docker pull albertgilharry/data602-final-project

#### url to access the app from the docker image:

http://localhost:5000

#### Github files: 

https://github.com/albert-gilharry/data602-final-project

## License:

CUNY DATA602 Final Project

## Development:

Albert Gilharry

Harpreet Shocker

Jagruti Solao




