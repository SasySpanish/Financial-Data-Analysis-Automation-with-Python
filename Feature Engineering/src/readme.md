# Source Scripts

## Overview
This folder contains the Python scripts used to calculate financial features from cleaned datasets.

## Scripts

### main.py
- Loads the cleaned dataset from `data/`.
- Calls functions from `feature_functions.py` to compute financial indicators.
- Saves the output CSV with calculated features in `data_features/`.

### feature_functions.py
- Contains all functions for feature calculation, including:
  - Returns (daily, weekly, monthly)
  - Moving averages (SMA, EMA)
  - Rolling volatility
  - Technical indicators (RSI, MACD, Bollinger Bands)

