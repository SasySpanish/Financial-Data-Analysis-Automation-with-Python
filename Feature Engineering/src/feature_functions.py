import pandas as pd
import numpy as np

# -------------------------
# Rendimenti
# -------------------------
def compute_returns(df, column="Close"):
    """
    Calcola i rendimenti giornalieri, settimanali e mensili.
    """
    df["Return_Daily"] = df[column].pct_change()
    df["Return_Weekly"] = df[column].pct_change(5)
    df["Return_Monthly"] = df[column].pct_change(21)
    return df

# -------------------------
# Medie mobili
# -------------------------
def compute_moving_averages(df, column="Close", windows=[5, 10, 20]):
    """
    Calcola SMA e EMA su finestre specificate.
    """
    for w in windows:
        df[f"SMA_{w}"] = df[column].rolling(window=w).mean()
        df[f"EMA_{w}"] = df[column].ewm(span=w, adjust=False).mean()
    return df

# -------------------------
# Volatilità
# -------------------------
def compute_volatility(df, column="Close", windows=[5, 10, 20]):
    """
    Calcola volatilità come rolling std.
    """
    for w in windows:
        df[f"Volatility_{w}"] = df[column].rolling(window=w).std()
    return df

# -------------------------
# Indicatori tecnici
# -------------------------
def compute_RSI(df, column="Close", window=14):
    """
    Calcola l'RSI su window giorni.
    """
    delta = df[column].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df[f"RSI_{window}"] = 100 - (100 / (1 + rs))
    return df

def compute_MACD(df, column="Close", fast=12, slow=26, signal=9):
    """
    Calcola il MACD e il segnale.
    """
    ema_fast = df[column].ewm(span=fast, adjust=False).mean()
    ema_slow = df[column].ewm(span=slow, adjust=False).mean()
    df["MACD"] = ema_fast - ema_slow
    df["MACD_Signal"] = df["MACD"].ewm(span=signal, adjust=False).mean()
    return df

def compute_bollinger_bands(df, column="Close", window=20, num_std=2):
    """
    Calcola le Bollinger Bands.
    """
    sma = df[column].rolling(window=window).mean()
    std = df[column].rolling(window=window).std()
    df[f"BB_Upper_{window}"] = sma + num_std * std
    df[f"BB_Lower_{window}"] = sma - num_std * std
    return df
