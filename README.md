# Air Quality Analysis for Public Policy in Milan & Turin
**UGST4158 — Introduction to Public Policy 2025/26 Winter**
Central European University 

Liza Drini · Benedek Szalma · Zeteny Cseresznyes

Time series analysis and policy evaluation of PM2.5 and PM10 air quality in Milan and Turin, using PurpleAir sensor data from 2022–2025. Includes SARIMAX forecasting and a difference-in-differences regression evaluating Milan's January 2025 smoking ban.

## Structure

```
├── Data Analysis/
│   ├── API/          data collection notebooks (PurpleAir API, 2022–2025)
│   ├── Data/         raw data — milan_air_quality.csv, turin_air_quality.csv
│   ├── Analysis/     city-level EDA, outlier treatment, SARIMAX forecasting
│   ├── Regression/   DID regression, event study, results plot
│   ├── Figures/      all output plots
│   └── Maps/         folium sensor location maps
├── Reports/
│   ├── abstract.md
│   ├── data_analysis_report.md   (time series methods, DID design, limitations)
│   ├── report.md                 (full policy report — review, findings, advice)
│   ├── policy_frame_report.md   (detailed frame analysis — actors, institutions)
│   └── presentation_outline.md  (slide-by-slide presentation outline)
│   ├── data_analysis_report.md       (time series methods, DID design, limitations)
│   ├── report.md                     (full policy report — review, findings, advice)
│   └── policy_frame_report.md        (detailed frame analysis — actors, institutions)
└── Sources/
    ├── bibliography.md            (exisiting literature, articles, sensor reports)
    ├── milan-policy-english.md    (policy text translated by Anthropic's Claude)
    └── milan-policy-italian.md    (original policy text)
```

## How to Run

1. **Data Analysis/API/** — run `pp_api_req_milan.ipynb` and `pp_api_req_turin.ipynb` to fetch/refresh data
2. **Data Analysis/Analysis/** — run `pp_analysis_milan.ipynb` and `pp_analysis_turin.ipynb` for EDA and forecasting
3. **Data Analysis/Regression/** — run `pp_regression.ipynb` for the DID analysis

Each notebook saves its figures automatically to `Data Analysis/Figures/`.

## Requirements

`pandas`, `numpy`, `matplotlib`, `statsmodels`, `scipy`, `requests`, `folium`

## Reports

See `Reports/` for the full report, presentation, the full data analysis and policy framing reports, and the pre-proposed abstract.
