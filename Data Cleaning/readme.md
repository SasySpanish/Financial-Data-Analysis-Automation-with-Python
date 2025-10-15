# Automated Data Cleaning from Yahoo Finance

This project automates the process of downloading, cleaning, and saving financial time series data from **Yahoo Finance** using Python.  
It is designed as a simple and reusable data-cleaning workflow for data analysis or portfolio projects.

---

## Project Overview

The script performs the following tasks:

1. **Downloads** time series data (e.g., Gold, S&P 500, etc.) from Yahoo Finance.  
2. **Cleans** the dataset by removing duplicates and missing values.  
3. **Saves** two versions of the file:
   - `data_raw/` → raw data as downloaded  
   - `data_cleaned/` → cleaned and analysis-ready data

---

## Folder Structure

```
project_root/
│
├── data_raw/          # Unprocessed Yahoo Finance data (CSV)
├── data_cleaned/      # Cleaned data (CSV)
├── src/               # Python scripts
│   └── data_cleaning.py
└── README.md
```

---

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SasySpanish/Data-Cleaning-YahooFinance.git
   cd Data-Cleaning-YahooFinance
   ```

2. **Install dependencies:**
   ```bash
   pip install yfinance pandas
   ```

3. **Run the script:**
   ```bash
   python src/data_cleaning.py
   ```

4. **Check the output:**
   - Raw data will be saved in `data_raw/`
   - Cleaned data will be saved in `data_cleaned/`

---

## Example: Gold Futures

Example ticker used in this project:  
**Gold Futures (`GC=F`)** – Historical gold prices from Yahoo Finance.  
You can change the ticker in the script to download another asset.

---

## Popular Yahoo Finance Tickers

| Asset | Ticker |
|-------|---------|
| S&P 500 Index | `^GSPC` |
| NASDAQ 100 | `^NDX` |
| Dow Jones | `^DJI` |
| Gold Futures | `GC=F` |
| Silver Futures | `SI=F` |
| Crude Oil WTI | `CL=F` |
| Brent Oil | `BZ=F` |
| EUR/USD | `EURUSD=X` |
| Bitcoin (USD) | `BTC-USD` |
| Apple Inc. | `AAPL` |

Full list of available tickers:  
[https://finance.yahoo.com/lookup/](https://finance.yahoo.com/lookup/)

---

## Data Description

### **data_raw/**
This folder contains **unprocessed** time series data downloaded directly from Yahoo Finance.  
Each file follows the naming convention:

```
TICKER_raw.csv
```

Example:
```
GC=F_raw.csv
```

Each CSV file includes:
- Date  
- Open  
- High  
- Low  
- Close  
- Adj Close  
- Volume  

These files may contain:
- Missing values (`NaN`)  
- Duplicated rows  
- Non-trading days or incomplete data  

Use the cleaned files instead for your analysis.

---

### **data_cleaned/**
This folder contains the **cleaned and ready-to-use** version of the data.  

**Cleaning steps applied:**
1. Removal of duplicate rows  
2. Removal of missing values (`NaN`)  
3. Resetting of the index  
4. Saving as a clean CSV file ready for analysis

Each file follows this naming convention:
```
TICKER_cleaned.csv
```

Example:
```
GC=F_cleaned.csv
```

---

## Technologies Used

- Python 3.x  
- pandas  
- yfinance  
- pathlib / os  

---

## Author

**Sasy Spanish**  
[GitHub Profile](https://github.com/SasySpanish)
