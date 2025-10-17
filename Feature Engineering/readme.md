# Financial Feature Engineering

## Overview
This repository **automates** the calculation of basic **[financial indicators and features](features/)** from cleaned historical data. It is designed to extend the previous data cleaning workflow by generating new features for analysis and modeling.

## Main Features ([better descripted here](features/))
- **Returns**
  - Daily, weekly, and monthly percentage changes
- **Moving Averages**
  - Simple (SMA) and exponential (EMA) over multiple window sizes
- **Volatility**
  - Rolling standard deviation of prices over multiple windows
- **Technical Indicators**
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence) and MACD signal line
  - Bollinger Bands (upper and lower bands around SMA)

## How to Use
1. Place the cleaned CSV file(s) in the `data/` folder.
2. Run the main script in `src/` to calculate features.
3. The new CSV(s) with features will be saved in `data_features/`.


## Requirements
- Python >= 3.8
- pandas
- numpy
- plotly (optional if adding interactive plots)
