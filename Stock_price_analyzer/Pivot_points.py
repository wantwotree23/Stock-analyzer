import pandas as pd
import yfinance as yf

def get_updated_price(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period ="1d", interval ="1m")
    latest_row = data.tail(1)
    return float(latest_row["Close"].iloc[0])

def get_price_data(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="5d", interval = "1d")
    yesterday = data.iloc[-2]
    return {
        'High': float(yesterday['High']),
        'Low': float(yesterday['Low']),
        'Close': float(yesterday['Close'])
    }

def pivot_point(price):
    P = (price['High'] + price['Low'] + price['Close']) / 3
    R1 = (P * 2) - price['Low']
    R2 = P + (price['High'] - price['Low'])
    S1 = (P * 2) - price['High']
    S2 = P - (price['High'] - price['Low'])
    return {
        'Pivot': round(P,2), 
        'Resistance 1': round(R1,2), 
        'Resistance 2': round(R2,2), 
        'Support 1': round(S1,2), 
        'Support 2': round(S2,2)}

symbol = input("Enter stock symbol: ")
price = get_updated_price(symbol)
print(f"Price:{round(price,2)}")
price_data = get_price_data(symbol)
print(f'Pivot Points:{pivot_point(price_data)}')