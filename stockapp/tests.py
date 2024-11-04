import yfinance as yf
import datetime


def fetch_stock_data():
  
  # Get user input for ticker symbol, start date, and end date
  ticker = input("Enter the stock ticker symbol: ")
  start_date_str = input("Enter the start date (YYYY-MM-DD): ")
  end_date_str = input("Enter the end date (YYYY-MM-DD): ")

  # Convert string dates to  datetime objects
  start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
  end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

  # Fetch stock data using yfinance
  stock_data = yf.download(ticker, start=start_date, end=end_date)

  # Print the open and close prices
  print(stock_data[['Open', 'Close']])




if __name__ == "__main__":
  fetch_stock_data()

