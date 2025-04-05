#Simulation controller for running investment strategies

import pandas as pd
import ta

def run_strategy_simulation(data, initial_investment, strategy):
    """
    Run different investment strategies simulation
    
    Args:
        data (pandas.DataFrame): Stock price data
        initial_investment (float): Initial investment amount
        strategy (str): Strategy name to simulate
        
    Returns:
        dict: Dictionary containing simulation results
    """
    result = {
        'strategy': strategy,
        'initial_investment': initial_investment,
        'start_date': data.index[0],
        'end_date': data.index[-1],
        'positions': [],
        'portfolio_value': []
    }

    cash = initial_investment
    shares = 0
    
    trades = []
    
    portfolio_values = []
    dates = []

    if strategy == "Buy and Hold":
        start_price = data['Close'].iloc[0]
        shares = cash / start_price
        cash = 0

        trades.append({
            'date': data.index[0],
            'action': 'BUY',
            'price': start_price,
            'shares': shares,
            'value': shares * start_price
        })

        for date, row in data.iterrows():
            portfolio_value = shares * row['Close']
            portfolio_values.append(portfolio_value)
            dates.append(date)

        end_price = data['Close'].iloc[-1]
        trades.append({
            'date': data.index[-1],
            'action': 'SELL',
            'price': end_price,
            'shares': shares,
            'value': shares * end_price
        })
        
    elif strategy == "Moving Average Crossover":
        if 'MA20' not in data.columns or 'MA50' not in data.columns:
            data['MA20'] = data['Close'].rolling(window=20).mean()
            data['MA50'] = data['Close'].rolling(window=50).mean()
        
        position = 'OUT'
        
        for i, (date, row) in enumerate(data.iterrows()):
            if i < 50:
                portfolio_values.append(cash)
                dates.append(date)
                continue
            if row['MA20'] > row['MA50'] and position == 'OUT':
                shares = cash / row['Close']
                cash = 0
                position = 'IN'
                
                trades.append({
                    'date': date,
                    'action': 'BUY',
                    'price': row['Close'],
                    'shares': shares,
                    'value': shares * row['Close']
                })
            
            elif row['MA20'] < row['MA50'] and position == 'IN':
                cash = shares * row['Close']
                
                trades.append({
                    'date': date,
                    'action': 'SELL',
                    'price': row['Close'],
                    'shares': shares,
                    'value': cash
                })
                
                shares = 0
                position = 'OUT'

            portfolio_value = cash + (shares * row['Close'])
            portfolio_values.append(portfolio_value)
            dates.append(date)
    
    elif strategy == "RSI Strategy":
        if 'RSI' not in data.columns:
            data['RSI'] = ta.momentum.RSIIndicator(data['Close']).rsi()
        
        position = 'OUT' 
        
        for i, (date, row) in enumerate(data.iterrows()):
            if i < 14 or pd.isna(row['RSI']):
                portfolio_values.append(cash)
                dates.append(date)
                continue

            if row['RSI'] < 30 and position == 'OUT':
                shares = cash / row['Close']
                cash = 0
                position = 'IN'
                
                trades.append({
                    'date': date,
                    'action': 'BUY',
                    'price': row['Close'],
                    'shares': shares,
                    'value': shares * row['Close']
                })
            
            elif row['RSI'] > 70 and position == 'IN':
                cash = shares * row['Close']
                
                trades.append({
                    'date': date,
                    'action': 'SELL',
                    'price': row['Close'],
                    'shares': shares,
                    'value': cash
                })
                
                shares = 0
                position = 'OUT'
            
            portfolio_value = cash + (shares * row['Close'])
            portfolio_values.append(portfolio_value)
            dates.append(date)
    
    final_portfolio_value = cash + (shares * data['Close'].iloc[-1])

    initial_price = data['Close'].iloc[0]
    final_price = data['Close'].iloc[-1]
    buy_hold_return = (final_price / initial_price - 1) * 100
    strategy_return = (final_portfolio_value / initial_investment - 1) * 100
    
    days = (data.index[-1] - data.index[0]).days
    years = days / 365.25
    annualized_return = ((1 + strategy_return/100) ** (1/years) - 1) * 100 if years > 0 else 0
    
    result['final_value'] = final_portfolio_value
    result['return_pct'] = strategy_return
    result['annualized_return'] = annualized_return
    result['buy_hold_return'] = buy_hold_return
    result['trades'] = trades
    result['portfolio_values'] = portfolio_values
    result['dates'] = dates
    
    return result