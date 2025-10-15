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
