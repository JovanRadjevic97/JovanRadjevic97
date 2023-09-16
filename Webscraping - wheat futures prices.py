import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as t

# Define time
now = t.datetime.today()

# Define the ticker symbol for wheat futures market
ticker_symbol = ['ZW=F','KE=F']

# Define the date range for historical data
start_date = '2021-06-01'
end_date = now.strftime("%G-%m-%d")

#conversion bushel into kg
konversion = 27.2155
#official exchange rate
middle_exchange_rate = 109.9703

# Fetch historical data using yfinance
wheat_data = yf.download(ticker_symbol, start=start_date, end=end_date)*middle_exchange_rate/100
wheat_data_kg = yf.download(ticker_symbol, start=start_date, end=end_date)/konversion*middle_exchange_rate/100

# Plot the Close price using pandas and matplotlib
wheat_data['Close'].plot()
plt.title('Wheat futures prices (RSD/bushel)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(visible=True)
plt.show()

wheat_data_kg['Close'].plot()
plt.title('Wheat futures prices (RSD/kg)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(visible=True)
plt.show()
