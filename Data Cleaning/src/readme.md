This folder contains the Python source code used for the **Yahoo Finance Data Cleaning** project.  
The scripts here automate the download, cleaning, and saving of financial time series data.

---

## Files Overview

| File | Description |
|------|--------------|
| **main.py** | Main execution script that runs the data download and cleaning process. |
| **data_cleaning.py** | Contains the reusable function(s) for data cleaning (e.g., removing duplicates, missing values, resetting index). |

---

## How It Works

1. `main.py` imports the cleaning functions from `data_cleaning.py`.  
2. The script downloads a financial time series from **Yahoo Finance** using the `yfinance` API.  
3. Raw data is saved in the `data_raw/` folder.  
4. The cleaning function processes the dataset (removing duplicates, missing data, etc.).  
5. The cleaned dataset is saved in the `data_cleaned/` folder.

