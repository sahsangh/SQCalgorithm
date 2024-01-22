import pandas as pd
import numpy as np
import os
import glob

def calculate_mvwap(prices, volumes, period=20):
    vwap = (prices * volumes).rolling(window=period).sum() / volumes.rolling(window=period).sum()
    return vwap

def calculate_std_dev_mvwap(prices, mvwap, period=20):
    deviation = (prices - mvwap)**2
    return np.sqrt(deviation.rolling(window=period).sum() / period)

def calculate_bollinger_bands(mvwap, std_dev):
    upper_band = mvwap + (2 * std_dev)
    lower_band = mvwap - (2 * std_dev)
    return upper_band, lower_band

def calculate_mean_reversion_score(stock_data, period=20):
    mvwap = calculate_mvwap(stock_data['Close'], stock_data['Volume'], period)
    std_dev = calculate_std_dev_mvwap(stock_data['Close'], mvwap, period)
    upper_band, lower_band = calculate_bollinger_bands(mvwap, std_dev)

    touches = ((stock_data['Close'] > upper_band) | (stock_data['Close'] < lower_band))
    revert_to_mean = ((stock_data['Close'].shift(-1) - mvwap.shift(-1)).abs() < (stock_data['Close'] - mvwap).abs()) & touches
    score = revert_to_mean.sum() / touches.sum() if touches.sum() else 0

    exits_counter = touches.sum()

    return score, exits_counter

def select_stocks(stock_data_files):
    threshold = .6
    exit_threshold = 40
    price = 150
    selected_stocks = []

    for file in stock_data_files:
        stock_data = pd.read_csv(file)
        score, exits_counter = calculate_mean_reversion_score(stock_data)
        highest_price = stock_data['Close'].max()
        symbol = os.path.basename(file).split('.')[0]
        print(f"{symbol}: Score={round(score, 3)}, Exits={exits_counter}, Highest Price={round(highest_price)}")

        if score > threshold:
            if exits_counter >= exit_threshold:
                if highest_price >= price:
                    selected_stocks.append((symbol,round(score,2) ,exits_counter, round(highest_price)))

    return selected_stocks
path = 'newCSV'  # Update to your CSV files directory
all_files = glob.glob(os.path.join(path, "*.csv"))
#stock_data_files = ["AMZN.csv","AAPL.csv","TSLA.csv","GOOGL.csv","KO.csv","MSFT.csv","PG.csv","SPY.csv","VTI.csv","XLP.csv", "XLU.csv","BURL.csv","DKS.csv","ORCL.csv","JPM.csv","WMT.csv"]
selected_stocks = select_stocks(all_files)
print("Selected Stocks:", selected_stocks)
