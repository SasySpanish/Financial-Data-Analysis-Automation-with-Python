# Source Code (`src`)

This folder contains the core scripts used for the automated exploratory data analysis.

## Files Overview

### `eda_functions.py`
Contains reusable functions for:
- Loading and cleaning datasets.
- Converting columns to numeric format.
- Computing summary statistics.
- Creating and saving plots (price trend, distribution, correlation heatmap).
- Generating descriptive summaries of the dataset.

### `config.py`
Defines configuration variables used across the project:
- `RAW_DATA_DIR`: path to the folder containing cleaned datasets ready for EDA.
- `REPORTS_DIR`: path where all generated reports and plots are stored.
- `TICKERS`: list of asset tickers to analyze.
- `PLOT_STYLE`: defines the visual style for plots.

### `main.py`
Main automation script that orchestrates the EDA pipeline:
1. Iterates through all tickers defined in `config.py`.
2. Loads and preprocesses the cleaned data.
3. Generates summary statistics and plots.
4. Produces an HTML report (no PDF conversion).
5. Saves all results into the `reports` directory.

### Dependencies
- `pandas`  
- `matplotlib`  
- `seaborn`  
- `jinja2`  
- `os`  

All scripts are modular and can be reused or extended for different datasets or analytical objectives.

