from binance.client import Client
import pandas as pd
import time

# Define your Binance API credentials
api_key = 'HCrcAeAOhBHwaOg4qJXCYOl7PKUNwYfnqtdDBn7OrDQ99i9UEEXqAFLjQ3jGIdKH'
api_secret = 'LPDTAQmcjrkfXjkvOExzeUdCpcJFS6xKsmyyMMbfvyC2gb7lWlpBPiVJbaW2GDri'

# Initialize the Binance client
client = Client(api_key, api_secret)

# Function to get historical data
def get_historical_klines(symbol, interval, start_str, end_str=None):
    # Download historical klines from Binance
    klines = client.get_historical_klines(symbol, interval, start_str, end_str)

    # Define column names for the dataframe
    columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']

    # Convert the list of klines to a Pandas DataFrame
    df = pd.DataFrame(klines, columns=columns)

    # Convert time from timestamp to human-readable format
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')

    return df

# Specify the cryptocurrency symbol, interval, and date range
symbol = 'BTCUSDT'  # Bitcoin paired with USDT (Tether)
interval = Client.KLINE_INTERVAL_1DAY  # 1-day interval
start_date = '1 Jan 2020'  # Specify the start date
end_date = None  # Specify the end date or leave as None to get data up to the current date

# Get the historical data
df = get_historical_klines(symbol, interval, start_date, end_date)

# Save the data to a CSV file
df.to_csv('bitcoin_historical_data.csv', index=False)

print("Data downloaded and saved to 'bitcoin_historical_data.csv'")
