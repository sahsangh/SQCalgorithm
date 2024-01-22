import yfinance as yf
import os

stocks = ["VZ"]
start_date = "2013-12-31"
end_date = "2022-12-31"

for stock in stocks:
    data = yf.download(stock, start=start_date, end=end_date)
    data.to_csv(stock+".csv")
