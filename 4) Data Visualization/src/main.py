import os
import pandas as pd
from viz_functions import (
    plot_close_price,
    plot_volume,
    plot_returns,
    plot_moving_averages,
    plot_bollinger_bands,
    plot_rsi,
    plot_macd,
    plot_cumulative_returns,
    plot_drawdown,
    plot_volatility,
    plot_return_distribution,
    plot_correlation_heatmap,
    interactive_candlestick,
    interactive_macd
)

# ============================================================
# PATH SETUP
# ============================================================

DATA_PATH = "../data/GC=F_features.csv"
STATIC_DIR = "../outputs/static_plots"
INTERACTIVE_DIR = "../outputs/interactive_plots"

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(INTERACTIVE_DIR, exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# ============================================================
# STATIC VISUALIZATIONS
# ============================================================

print("Generating static plots...")

plot_close_price(df, save_path=f"{STATIC_DIR}/close_price.png")
plot_volume(df, save_path=f"{STATIC_DIR}/volume.png")
plot_returns(df, save_path=f"{STATIC_DIR}/returns.png")
plot_moving_averages(df, save_path=f"{STATIC_DIR}/moving_averages.png")
plot_bollinger_bands(df, save_path=f"{STATIC_DIR}/bollinger_bands.png")
plot_rsi(df, save_path=f"{STATIC_DIR}/rsi.png")
plot_macd(df, save_path=f"{STATIC_DIR}/macd.png")
plot_cumulative_returns(df, save_path=f"{STATIC_DIR}/cumulative_returns.png")
plot_drawdown(df, save_path=f"{STATIC_DIR}/drawdown.png")
plot_volatility(df, save_path=f"{STATIC_DIR}/volatility.png")
plot_return_distribution(df, save_path=f"{STATIC_DIR}/return_distribution.png")
plot_correlation_heatmap(df, save_path=f"{STATIC_DIR}/correlation_heatmap.png")

print("Static plots saved in:", STATIC_DIR)

# ============================================================
# INTERACTIVE VISUALIZATIONS
# ============================================================

print("Generating interactive plots...")

interactive_candlestick(df, save_path=f"{INTERACTIVE_DIR}/candlestick.html")
interactive_macd(df, save_path=f"{INTERACTIVE_DIR}/macd.html")

print("Interactive plots saved in:", INTERACTIVE_DIR)
print("Visualization pipeline completed successfully!")
