# Cleaned Data

This folder contains **cleaned and preprocessed datasets** ready for Exploratory Data Analysis (EDA).

## Description
Each dataset has been automatically cleaned by the [previous data preparation and cleaning pipeline](../../Data Cleaning/).  
The cleaning process included:
- Handling missing or inconsistent values.
- Converting columns to appropriate data types.
- Removing duplicates.
- Renaming columns for clarity.
- Aligning date formats and numerical representations.

## Files
Example:
- `GC=F_cleaned.csv` — cleaned and standardized dataset for the Gold Futures (ticker: GC=F).

## Usage
These datasets are the direct input for the EDA automation pipeline.  
Each file should follow the naming convention: `{TICKER}_cleaned.csv` and must be placed inside this folder before running the EDA script.

The EDA process reads these files automatically based on the list of tickers specified in `config.py`.

