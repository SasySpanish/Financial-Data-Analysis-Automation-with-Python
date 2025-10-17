# Financial Feature Engineering

## Overview
This repository automates the calculation of basic **financial indicators and features** from cleaned historical data. It is designed to extend the previous data cleaning workflow by generating new features for analysis and modeling.

## Main Features
- Daily, weekly, and monthly returns
- Simple and exponential moving averages
- Rolling volatility
- Technical indicators: RSI, MACD, Bollinger Bands


## How to Use
1. Place the cleaned CSV file(s) in the `data/` folder.
2. Run the main script in `src/` to calculate features.
3. The new CSV(s) with features will be saved in `data_features/`.



python src/main.py


## Requirements
- Python >= 3.8
- pandas
- numpy
- plotly (optional if adding interactive plots)
