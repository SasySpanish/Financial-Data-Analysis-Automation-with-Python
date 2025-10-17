# Financial Feature Engineering

## Overview
This repository **automates** the calculation of basic **financial indicators and features** from cleaned historical data. It is designed to extend the previous data cleaning workflow by generating new features for analysis and modeling.

## Main Features
- Daily, weekly, and monthly returns
- Simple and exponential moving averages
- Rolling volatility
- Technical indicators: RSI, MACD, Bollinger Bands

## Features Description

### Returns
- **Return_Daily**: Daily percentage change of the selected price column.
- **Return_Weekly**: Percentage change over 5 trading days.
- **Return_Monthly**: Percentage change over 21 trading days.

### Moving Averages
- **SMA_X**: Simple Moving Average over X days.
- **EMA_X**: Exponential Moving Average over X days.

### Volatility
- **Volatility_X**: Rolling standard deviation of the selected price column over X days, used as a measure of price volatility.

### Technical Indicators
- **RSI_X**: Relative Strength Index over X days, measures the speed and change of price movements, indicating overbought or oversold conditions.
- **MACD**: Moving Average Convergence Divergence, calculated as the difference between fast and slow EMAs.
- **MACD_Signal**: Signal line of the MACD, usually a 9-day EMA of the MACD.
- **BB_Upper_X / BB_Lower_X**: Bollinger Bands over X days, calculated as SMA ± 2 standard deviations, representing dynamic price support and resistance levels.

### Notes
- X represents the window size (e.g., 5, 10, 20) used in rolling calculations.
- All indicators are calculated based on the `Close` price by default, unless specified otherwise.

## How to Use
1. Place the cleaned CSV file(s) in the `data/` folder.
2. Run the main script in `src/` to calculate features.
3. The new CSV(s) with features will be saved in `data_features/`.


## Requirements
- Python >= 3.8
- pandas
- numpy
- plotly (optional if adding interactive plots)
