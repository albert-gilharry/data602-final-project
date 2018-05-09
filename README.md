This application builds on the previous app by integrating ARIMA and Random Forest Regressor predictions for the first 4 stocks. 

When Trading, you are presented with optimized allocation in a pie chart. This was generated using scipy's minimize function, but maximized by using the negative of the objective function. 

There is now a Visualizations page to access dynamic visualizations. You may access the updated Blotter and the P/L (Profit/Loss) table by visiting their respective menu items in the upper left. 

The cryptocurrencies were sourced from Bittrex's API (https://bittrex.com/api). The US Dollar is used as the base trading currency. All prices are in USD. This was acheived by converting the base currency of a given cryptocurrency to US Dollars, using CoinMarketCap's API (https://api.coinmarketcap.com/). 

The historical data were acquired using CryptoCompare's API (https://min-api.cryptocompare.com/data/). The plots were produced using Python's Matplotlib library. 

The main data structures used in this application are Pandas dataframes, Numpy arrays, and lists. The blotter data is stored in a MongoDB instance on mLab (https://mlab.com). Dictionaries were used to facilitate MongoDB operations and AJAX requests. 

This web application was built using Python's Flask framework. 

The interface was designed using Bootstrap from https://getbootstrap.com/. 

The Dockerfile is configured to expose port 5000.

Docker Hub link: https://hub.docker.com/r/albertgilharry/trader-app3/. 

To pull the image, please use the following command: docker pull albertgilharry/trader-app3 

To start the application, use the following Docker command: docker run -p 5000:5000 albertgilharry/trader-app3 

To access the application, please visit this URL in your browser: http://localhost:5000 

Happy trading!


