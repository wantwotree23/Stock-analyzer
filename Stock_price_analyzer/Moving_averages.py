import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_updated_price(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period ="1d", interval ="1m")
    latest_row = data.tail(1)
    return float(latest_row["Close"].iloc[0])

def get_moving_averages(symbol: str, windows=[20, 50, 200]) -> pd.DataFrame:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1y", interval="1d")
    for window in windows:
        data[f'MA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def plot_moving_averages(data: pd.DataFrame, symbol: str):
    plt.figure(figsize=(12,6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    for column in data.columns:
        if 'MA_' in column:
            plt.plot(data[column], label=column)
    plt.title(f'Moving Averages for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

symbol = input("Enter stock symbol: ")
price = get_updated_price(symbol)
print(f"Price:{round(price,2)}")
ma_data = get_moving_averages(symbol)
plot_moving_averages(ma_data, symbol)