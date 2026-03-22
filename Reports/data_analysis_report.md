# Air Quality in Italian Cities: Time Series Analysis and Policy Evaluation
**UGST4158 — Introduction to Public Policy 2025/26 Winter**
Central European University — Quantitative Methods Seminar
Liza Drini · Benedek Szalma · Zeteny Cseresznyes

---

## 1. Research Question

Two questions are addressed. First, how do PM2.5 and PM10 concentrations evolve in Milan and Turin, and can they be forecast? Second, did Milan's January 2, 2025 smoking ban produce a measurable reduction in ambient PM levels? The first is answered with city-level time series models; the second with a difference-in-differences (DID) regression.

---

## 2. Data

Data come from the **PurpleAir API** (`api.purpleair.com/v1/sensors`), queried month by month from January 2022 through December 2025 at daily resolution (`average=1440`). Variables retrieved: `pm2.5_atm`, `pm10.0_atm`, `temperature` (°F), `humidity` (%), `pressure` (hPa).

Sensors were identified via bounding-box queries:

- **Milan** — 45.55°N–45.35°N, 8.95°E–9.40°E → **7 sensors**, 4,319 sensor-days, Jan 2022 – Dec 2025
- **Turin** — 45.17°N–44.95°N, 7.55°E–7.85°E → **1 sensor** (ID 133001), 1,357 days, Feb 2022 – Dec 2025

---

## 3. Sensors and Outlier Treatment

Raw values reached physically implausible extremes (Milan PM2.5 max: 2,043 µg/m³; Turin: 1,303 µg/m³), typical of low-cost optical counters affected by drift and miscalibration.

**Milan.** Five of the seven sensors (IDs 188041, 188043, 188049, 256425, 264579) produced systematically erratic readings. Two — **6540 (Piazza Sempione)** and **31569 (Gaggiano MI)** — were designated reference sensors. Readings across all seven sensors outside **mean ± 3σ** of the reference distribution were replaced with `NaN` and linearly interpolated, applied per sensor before aggregating to a daily city mean.

**Turin.** With a single sensor, a **rolling median ± 2 × MAD** filter was used instead (30-day centred window). Median and MAD are robust to outliers, unlike mean and standard deviation. K = 2.0 was chosen to be strict given the high noise level. Flagged values were interpolated as above.

---

## 4. Time Series Modelling — SARIMAX

After cleaning, sensor readings were averaged to one daily series per city. ADF tests confirmed stationarity for both PM2.5 (p = 0.00023) and PM10 (p = 0.00039) in Milan. Seasonal decomposition (additive, period = 7) revealed a clear weekly cycle and a longer annual pattern.

A **SARIMAX(1,1,1)(1,1,1,7)** model was fitted for PM2.5 and PM10 in each city: AR(1) and MA(1) for short-run dynamics, one difference for trend removal, and seasonal terms at lag 7 for the weekly cycle. Annual seasonality — computationally intractable at lag 365 in SARIMAX — was captured via **K = 3 Fourier pairs** (sin₁–sin₃, cos₁–cos₃ at period = 365.25 days) as exogenous regressors, alongside temperature and humidity.

Train/test split: pre-2025 (~3 years) for training, 2025 for out-of-sample evaluation. Forecasts and confidence intervals were clipped at zero.

---

## 5. Policy Evaluation — Difference-in-Differences

**Design.** Treatment group: Milan (ban from Jan 2, 2025). Control group: Turin (no equivalent policy). Pre-period: Jan 2022 – Jan 1, 2025. Post-period: Jan 2 – Dec 2025.

Turin shares the same Po Valley airshed and regional meteorology as Milan, and had no equivalent policy — making it a plausible counterfactual. Its weaknesses: a different industrial profile (automotive-heavy), a noticeably lower baseline PM2.5, and only one sensor versus Milan's seven.

**Specification.** Both series were aggregated to weekly averages to reduce noise, then estimated as:

> **PM_it = α + δ · DID_it + β · temperature_it + γ · humidity_it + μ_i + λ_t + ε_it**

where DID_it = treat_i × post_t. City fixed effects (μ_i) absorb baseline level differences; week fixed effects (λ_t) absorb common seasonal shocks. HC1 robust standard errors are used — city-level clustering is infeasible with two units. δ is the ATT under the parallel trends assumption, tested graphically and via a treat × time interaction in the pre-period. An **event study** with monthly relative-time bins further checks pre-trend behaviour and traces the dynamic treatment effect.

---

## 6. Reproducibility

```
ppp/
├── API/          pp_api_req_milan.ipynb, pp_api_req_turin.ipynb
├── Data/         milan_air_quality.csv, turin_air_quality.csv
├── Analysis/     pp_analysis_milan.ipynb, pp_analysis_turin.ipynb
├── Regression/   pp_regression.ipynb
└── Figures/      all output plots (.png, .html)
```

Running the API notebooks regenerates the CSVs; running the analysis and regression notebooks regenerates all figures.

---

## 7. Limitations

**Sensor quality.** PurpleAir devices over-report under high humidity and drift over time. No cross-calibration against a regulatory monitor was performed; results are indicative, not precise.

**Residual noise.** The reference-sensor filter assumes sensors 6540 and 31569 are themselves well-calibrated, which cannot be verified. The rolling MAD filter for Turin may remove genuine pollution peaks alongside noise.

**Interpolation.** Linear interpolation over flagged values introduces artificial smoothness and, over consecutive flagged days, effectively fabricates data.

**DID design.** One treated and one control city makes city-level clustering infeasible and the estimate sensitive to any idiosyncratic shock to Turin's single sensor.

**Short post-treatment window.** Under twelve months of post-ban data limits statistical power and makes it hard to separate the policy effect from seasonal variation.

**Missing weather controls.** Wind speed and precipitation — key drivers of PM dispersion — are unavailable from PurpleAir, leaving a potential source of omitted variable bias.

**Effect size.** Cigarette smoke is a small fraction of urban PM2.5 relative to traffic and heating. A detectable signal from an outdoor ban using noisy low-cost sensors is inherently challenging.
