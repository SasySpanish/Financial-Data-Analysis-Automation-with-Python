# Raw Data

## Overview
This folder contains the cleaned dataset(s) used as input for feature calculation.

- The cleaned dataset is the output from the [previous data preparation and cleaning pipeline](../../Data%20Cleaning/).
- The main script in `src/` will read the CSV(s) from this folder to generate new features.

### Notes
- Ensure the dataset is cleaned and formatted correctly, with numeric columns (e.g., Close, Open, High, Low, Volume) as floats.
- The cleaned CSV file should be named consistently (e.g., `GC=F_cleaned.csv`) for the main script to work without modifications.

