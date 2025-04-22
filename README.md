
# Stock Analysis Tool

A powerful desktop application built with Python and PyQt5 for performing technical stock analysis and investment strategy simulations. It utilizes real-time market data, financial indicators, and visualization tools to offer recommendations and backtest investment strategies.

## Features

- Real-Time Stock Analysis with support for MA, RSI, MACD, and Bollinger Bands
- Investment Recommendations based on technical signals and risk tolerance
- Interactive UI with multiple tabs for charts, indicators, and simulation
- Strategy Backtesting (Buy & Hold, MA Crossover, RSI Strategy)
- Candlestick & Line Charts using Matplotlib and mplfinance
- Custom Date Ranges and simulation parameters
- Risk Profile Settings (Low, Moderate, High)
- Historical Ticker Management

## Project Structure

```
stock_analysis/
│
├── main.py                  # Entry point - launches the PyQt5 app
├── requirements.txt         # Required Python packages
│
├── models/
│   ├── __init__.py
│   └── stock_analysis.py    # Stock data processing and analysis logic
│
├── views/
│   ├── __init__.py
│   ├── main_window.py       # Main application window
│   ├── analysis_tab.py      # Recommendation & summary tab
│   ├── charts_tab.py        # Candlestick and line chart tab
│   ├── indicators_tab.py    # RSI, MACD visualization tab
│   └── simulation_tab.py    # Investment simulation tools
│
├── controllers/
│   ├── __init__.py
│   ├── data_controller.py   # Data download and preprocessing
│   └── simulation.py        # Backtesting logic for investment strategies
│
└── utils/
    ├── __init__.py
    ├── charting.py          # Chart rendering utilities
    └── styles.py            # UI themes and palette settings
```

## Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/aalmaweri12/FinalCIS298.git
   cd stock_analysis
   ```

2. Create a Virtual Environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install Requirements
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Application
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- PyQt5
- matplotlib
- yfinance
- pandas
- numpy
- mplfinance
- ta (Technical Analysis library)

All dependencies are listed in requirements.txt.

## Contributors

| Name         | Role                                     |
|--------------|------------------------------------------|
| Abdulmajeed  | UI Design, Simulation Tab, Main Window   |
| Sami         | Indicators Logic, Models, Utils          |
| Almo         | Charts Tab, Data Controllers, Styling    |

#  Commit History - FinalCIS298
## April 19, 2025  
- Commit by **Almo** - Updated the README file

##  April 18, 2025
- Commit by **aalmaweri12** – Merged changes from main branch  
- Commit by **aalmaweri12** – Created the team evaluation document  
- Commit by **Almo** – Updated the README file
- Commit by **alharharasami** – Updated the README file
- Commit by **Almo** – Additional tweaks to the README  

##  April 15, 2025
- Commit by **Almo** – Merged feature branch: dark mode styling  
- Commit by **Almo** – Changed entire app styling to dark mode  
- Commit by **aalmaweri12** – Created `main.py` and initial `README.md`
-  Commit by **alharharasami** – Added `indicators_tab.py` 
- Commit by **alharharasami** – Updated `indicators_tab.py`  
- Commit by **alharharasami** – Additional changes to `indicators_tab.py`  
- Commit by **alharharasami** – Uploaded project files (1st batch)  
- Commit by **alharharasami** – Uploaded project files (2nd batch)  

##  April 14, 2025
- Commit by **aalmaweri12** – Updated `README.md`  
- Commit by **alharharasami** – Updated `stock_analysis.py`
- Commit by **alharharasami** – Added `charting.py`

##  April 11, 2025
- Commit by **alharharasami** – Added `__init__.py`
- Commit by **alharharasami** – Added `stock_model.py`
- Commit by **alharharasami** – Renamed `stock_model.py` to `stock_analysis.py`  
- Commit by **alharharasami** – Uploaded additional files  

##  April 10, 2025
- Commit by **Almo** – Merged styling branch into main  
- Commit by **Almo** – Added light theme styling  

##  April 8, 2025
- Commit by **aalmaweri12** – Merged latest main changes  
- Commit by **aalmaweri12** – Added analysis and simulation tabs  

##  April 7, 2025
- Commit by **Almo** – Using previous branch / Improved simulation controller  
- Commit by **Almo** – Merged improved simulation controller  

##  April 5, 2025
- Commit by **Almo** – Setup simulation controller  
- Commit by **Almo** – Merged simulation setup branch  

##  April 4, 2025
- Commit by **aalmaweri12** – Merged changes from main  
- Commit by **aalmaweri12** – Created main view page  

##  April 3, 2025
- Commit by **Almo** – Finished fetching and processing stock data  
- Commit by **Almo** – Merged data-fetching feature branch  

##  April 1, 2025
- Commit by **aalmaweri12** – Created initial file structure  
- Commit by **aalmaweri12** – Initial commit  



## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational purposes only. The stock recommendations provided are based on technical indicators and are not financial advice. Always do your own research or consult with a financial advisor.
