# Air Quality Analysis — Milan & Turin
**UGST4158 — Introduction to Public Policy 2025/26 Winter**
Central European University — Liza Drini · Benedek Szalma · Zeteny Cseresznyes

Time series analysis and policy evaluation of PM2.5 and PM10 air quality in Milan and Turin, using PurpleAir sensor data from 2022–2025. Includes SARIMAX forecasting and a difference-in-differences regression evaluating Milan's January 2025 smoking ban.

## Structure

```
├── API/          data collection notebooks (PurpleAir API pull, 2022–2025)
├── Data/         raw CSVs — milan_air_quality.csv, turin_air_quality.csv
├── Analysis/     city-level EDA, outlier treatment, SARIMAX forecasting
├── Regression/   DID regression, event study, results plot
└── Figures/      all output plots and sensor maps
```

## How to Run

1. **API/** — run `pp_api_req_milan.ipynb` and `pp_api_req_turin.ipynb` to fetch/refresh data
2. **Analysis/** — run `pp_analysis_milan.ipynb` and `pp_analysis_turin.ipynb` for EDA and forecasting
3. **Regression/** — run `pp_regression.ipynb` for the DID analysis

Each notebook saves its figures automatically to `Figures/`.

## Requirements

`pandas`, `numpy`, `matplotlib`, `statsmodels`, `scipy`, `requests`, `folium`

## Report

See `report.md` for a full description of the research question, data, methods, and limitations.
