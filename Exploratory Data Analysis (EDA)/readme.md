# Exploratory Data Analysis (EDA)

This folder contains the automation pipeline for the **Exploratory Data Analysis (EDA)** phase.  
The process loads the cleaned dataset(s), performs descriptive statistical analysis, generates visualizations, and produces an automated HTML report for each asset or ticker.

## Overview
The EDA automation script:
1. Loads the cleaned dataset(s) from the `data` directory.
2. Converts all numeric columns into a consistent numerical format.
3. Generates descriptive statistics (mean, standard deviation, min, max, etc.).
4. Creates visualizations such as:
   - Price trends over time  
   - Variable distributions  
   - Correlation heatmaps  
5. Saves all generated outputs (summary CSV, plots, and HTML report) in the `reports` directory.

## Output
For each ticker (e.g., `GC=F`), the following files are created inside `reports/`:
- `{ticker}_summary.csv` — dataset summary statistics
- `{ticker}_trend.png` — price trend visualization
- `{ticker}_distribution.png` — distribution of main numeric features
- `{ticker}_correlation.png` — correlation matrix heatmap
- `{ticker}_report.html` — full HTML report combining summary and plots

## Purpose
This automation allows for a fast, reproducible, and consistent analysis workflow across multiple datasets or financial assets.

