"""
Stock data fetcher module for the stock analyzer application.
This module handles retrieving stock data from Yahoo Finance,
cleaning it, and preparing it for analysis.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_live_stock_price(ticker_symbol):
    """
    Get the current (live) stock price for the given ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL')
        
    Returns:
        dict: Dictionary containing current price data and metadata
              or None if an error occurs
    """
    try:
        logger.info(f"Fetching live price data for {ticker_symbol}")
        ticker = yf.Ticker(ticker_symbol)
        
        # Get the live price data
        live_data = ticker.info
        
        # Extract relevant information
        price_data = {
            'symbol': ticker_symbol,
            'current_price': live_data.get('currentPrice', live_data.get('regularMarketPrice')),
            'previous_close': live_data.get('previousClose'),
            'open': live_data.get('open', live_data.get('regularMarketOpen')),
            'day_low': live_data.get('dayLow', live_data.get('regularMarketDayLow')),
            'day_high': live_data.get('dayHigh', live_data.get('regularMarketDayHigh')),
            'volume': live_data.get('volume', live_data.get('regularMarketVolume')),
            'market_cap': live_data.get('marketCap'),
            'company_name': live_data.get('shortName', live_data.get('longName', ticker_symbol)),
            'currency': live_data.get('currency'),
            'exchange': live_data.get('exchange'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Calculate daily change and percent change
        if price_data['current_price'] and price_data['previous_close']:
            price_data['daily_change'] = price_data['current_price'] - price_data['previous_close']
            price_data['daily_change_percent'] = (price_data['daily_change'] / price_data['previous_close']) * 100
            
        return price_data
        
    except Exception as e:
        logger.error(f"Error fetching live price for {ticker_symbol}: {str(e)}")
        return None

def get_historical_data(ticker_symbol, period='7d', interval='1d'):
    """
    Get historical stock data for the given ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL')
        period (str): The time period to retrieve (default: '7d')
                     Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval (str): The data interval (default: '1d')
                     Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        
    Returns:
        pandas.DataFrame: DataFrame containing historical stock data
                         or None if an error occurs
    """
    try:
        logger.info(f"Fetching historical data for {ticker_symbol} with period={period}, interval={interval}")
        ticker = yf.Ticker(ticker_symbol)
        hist_data = ticker.history(period=period, interval=interval)
        
        # Make sure the DataFrame has the expected columns
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        if not all(col in hist_data.columns for col in required_columns):
            missing = [col for col in required_columns if col not in hist_data.columns]
            logger.warning(f"Missing columns in historical data: {missing}")
            return None
            
        # Reset index to make Date a column
        hist_data = hist_data.reset_index()
        
        # Convert Date to string if it's a datetime object
        if 'Date' in hist_data.columns and pd.api.types.is_datetime64_any_dtype(hist_data['Date']):
            hist_data['Date'] = hist_data['Date'].dt.strftime('%Y-%m-%d')
            
        # Ensure all columns have valid values (replace NaN with None)
        hist_data = hist_data.where(pd.notnull(hist_data), None)
        
        return hist_data
        
    except Exception as e:
        logger.error(f"Error fetching historical data for {ticker_symbol}: {str(e)}")
        return None

def get_data_for_analysis(ticker_symbol, days=30):
    """
    Get a combined dataset for stock analysis, including both current
    and historical data with additional metrics for analysis.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL')
        days (int): Number of days of historical data to retrieve
        
    Returns:
        tuple: (live_data, hist_data) containing current and historical data
               or (None, None) if an error occurs
    """
    try:
        # Get live price data
        live_data = get_live_stock_price(ticker_symbol)
        if not live_data:
            return None, None
            
        # Get historical data
        period = f"{days}d"
        hist_data = get_historical_data(ticker_symbol, period=period)
        if hist_data is None or hist_data.empty:
            return live_data, None
            
        # Calculate additional metrics for analysis
        if 'Close' in hist_data.columns:
            # Calculate daily returns
            hist_data['Daily_Return'] = hist_data['Close'].pct_change() * 100
            
            # Calculate moving averages
            hist_data['MA5'] = hist_data['Close'].rolling(window=5).mean()
            hist_data['MA10'] = hist_data['Close'].rolling(window=10).mean()
            hist_data['MA20'] = hist_data['Close'].rolling(window=min(20, len(hist_data))).mean()
            
            # Calculate volatility (standard deviation of returns)
            if len(hist_data) >= 5:
                hist_data['Volatility'] = hist_data['Daily_Return'].rolling(window=5).std()
            
        return live_data, hist_data
        
    except Exception as e:
        logger.error(f"Error preparing analysis data for {ticker_symbol}: {str(e)}")
        return None, None

def validate_ticker(ticker_symbol):
    """
    Validate if a ticker symbol exists and can be fetched.
    
    Args:
        ticker_symbol (str): The stock ticker symbol to validate
        
    Returns:
        bool: True if the ticker is valid, False otherwise
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        
        # Check if we got valid information back
        if 'symbol' in info or 'shortName' in info:
            return True
        return False
        
    except Exception as e:
        logger.error(f"Error validating ticker {ticker_symbol}: {str(e)}")
        return False

# Additional utility functions can be added below as needed
