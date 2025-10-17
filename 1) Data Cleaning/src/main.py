import os
import yfinance as yf
from data_cleaner import clean_financial_data

def main():
    """
    Scarica dati storici da Yahoo Finance, li pulisce e salva un CSV pronto per l'analisi.
    """
    ticker = "GC=F"  # Oro
    start_date = "2001-01-01"
    end_date = "2025-06-01"

    print(f"📥 Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        print("❌ Nessun dato trovato. Controlla il ticker o le date.")
        return

    print("🧹 Cleaning data...")
    cleaned_data = clean_financial_data(data)

    # Crea le cartelle di output
    os.makedirs("../data_raw", exist_ok=True)
    os.makedirs("../cleaned_data", exist_ok=True)

    # Salva i file
    raw_path = f"../data_raw/{ticker}_raw.csv"
    clean_path = f"../cleaned_data/{ticker}_cleaned.csv"

    data.to_csv(raw_path)
    cleaned_data.to_csv(clean_path, index=False)

    print(f"✅ Dati puliti salvati in: {clean_path}")

if __name__ == "__main__":
    main()
