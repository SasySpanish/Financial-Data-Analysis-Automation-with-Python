import os
import pandas as pd
from eda_functions import (
    load_data,
    convert_numeric,
    summary_statistics,
    plot_price_trend,
    plot_distribution,
    correlation_heatmap,
)
from jinja2 import Environment, FileSystemLoader
from config import RAW_DATA_DIR, REPORTS_DIR, TICKERS

# --------------------------
# Funzione per generare solo report HTML (nessun PDF)
# --------------------------
def generate_html_report(ticker, df, summary_csv, trend_plot, distribution_plot, correlation_plot):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("report_template.html")
    
    # Legge il summary (CSV) per passarlo al template
    summary = pd.read_csv(summary_csv, index_col=0)
    
    html_out = os.path.join(REPORTS_DIR, f"{ticker}_report.html")
    
    html_content = template.render(
        ticker=ticker,
        summary=summary,
        # Nel template ci aspettiamo solo i nomi dei file delle immagini (basename)
        trend_plot=os.path.basename(trend_plot),
        distribution_plot=os.path.basename(distribution_plot),
        correlation_plot=os.path.basename(correlation_plot)
    )
    
    # Salva HTML
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ HTML report generated: {html_out}")
    return html_out

# --------------------------
# Script principale
# --------------------------
def main():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    for ticker in TICKERS:
        file_path = os.path.join(RAW_DATA_DIR, f"{ticker}_cleaned.csv")
        if not os.path.exists(file_path):
            print(f"File for {ticker} not found, skipping.")
            continue
        
        df = load_data(file_path)
        df = convert_numeric(df)
        
        # Summary stats
        stats = summary_statistics(df)
        summary_csv = os.path.join(REPORTS_DIR, f"{ticker}_summary.csv")
        stats.to_csv(summary_csv)
        print(f"✅ Summary CSV saved: {summary_csv}")
        
        # Plots (i nomi con cui li salviamo nella directory REPORTS_DIR)
        trend_plot = os.path.join(REPORTS_DIR, f"{ticker}_trend.png")
        distribution_plot = os.path.join(REPORTS_DIR, f"{ticker}_distribution.png")
        correlation_plot = os.path.join(REPORTS_DIR, f"{ticker}_correlation.png")
        
        # Chiamate alle funzioni di plotting — si assume che queste funzioni
        # salvino i file nelle paths che passiamo (REPORTS_DIR + filename).
        plot_price_trend(df, ticker, REPORTS_DIR)        # dovrebbe salvare ticker_trend.png
        plot_distribution(df, ticker, REPORTS_DIR)      # dovrebbe salvare ticker_distribution.png
        correlation_heatmap(df, ticker, REPORTS_DIR)    # dovrebbe salvare ticker_correlation.png
        
        # Genera solo HTML (senza conversione PDF)
        generate_html_report(ticker, df, summary_csv, trend_plot, distribution_plot, correlation_plot)

if __name__ == "__main__":
    main()
