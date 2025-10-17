import os
import pandas as pd
from feature_functions import (
    compute_returns, compute_moving_averages, compute_volatility,
    compute_RSI, compute_MACD, compute_bollinger_bands
)
from config import DATA_RAW_DIR, DATA_FEATURES_DIR

INPUT_FILE = os.path.join(DATA_RAW_DIR, "GC=F_cleaned.csv")
OUTPUT_FILE = os.path.join(DATA_FEATURES_DIR, "GC=F_features.csv")


# Carica il dataset
df = pd.read_csv(INPUT_FILE)

# Converte colonne in str
for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '').str.strip(), errors='coerce')


# Calcolo delle features
df = compute_returns(df)
df = compute_moving_averages(df)
df = compute_volatility(df)
df = compute_RSI(df)
df = compute_MACD(df)
df = compute_bollinger_bands(df)

# Salva il CSV con le features
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Features generated and saved in: {OUTPUT_FILE}")

df1 = pd.read_csv(OUTPUT_FILE)
