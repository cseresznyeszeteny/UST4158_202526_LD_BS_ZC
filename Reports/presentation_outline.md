# Presentation Outline: Smoking Ban in Milan

---

## 1. Title

- **Title:** Smoking Ban in Milan: Policy Review and Short-Term Effects on Air Quality
- Subtitle: A difference-in-differences analysis using PurpleAir sensor data, 2022–2025
- UGST4158 — Introduction to Public Policy 2025/26 Winter, Central European University — Quantitative Methods Seminar
- Liza Drini · Benedek Szalma · Zeteny Cseresznyes

---

## 2. Policy and Framing

- Milan sits in the Po Valley — one of the most persistently air-polluted regions in Europe due to topography and meteorology that trap particulate matter year-round; it has repeatedly exceeded EU PM and NOx concentration limits
- In response, the Municipality of Milan adopted the **Air Quality Regulation** (Resolution No. 56, November 2020) — a comprehensive package targeting heating systems, biomass combustion, diesel generators at markets, construction site dust, and outdoor combustion
- **Smoking provisions (Art. 9):**
  - 2021: ban in parks, playgrounds, bus stops, sports areas, dog areas, cemeteries
  - **January 2, 2025:** full ban extended to all public outdoor spaces — streets, squares, any publicly accessible area — with a 10-metre isolation exception
  - Fines: €40–€240 · enforcement by Polizia Locale
- **Dominant frame:** environmental — the regulation explicitly cites the "polluter pays" principle and PM emission reduction as the primary justification; smoking is positioned as an air quality problem
- **Secondary frame:** moral — protecting vulnerable groups (children, pregnant women, non-smokers) from passive smoke exposure, though this remains implicit in the official text
- **Policy entrepreneur:** Mayor Giuseppe Sala, championing the measure as part of the city's Air and Climate Plan
- **Opposing actors:** tobacco producers and retailers (contested jurisdictional basis in regional courts), hospitality sector (unclear rules for outdoor terraces, enforcement responsibility)
- **Instrument:** deterrence — fines designed to make smoking in public costlier than compliance
- **Enforcement gap:** very few fines issued in early months; the ban has been described as "symbolic" by business federation president Lino Stoppani
- The ban gained additional international visibility as Milan prepares to host the **Milan–Cortina 2026 Winter Olympics**

---

## 3. Literature and Articles

**Research:**

- Italy's Tobacco Control Scale ranking: 8th → 18th in Europe between 2006 and 2021 (La Vecchia et al., 2025)
- Smoking prevalence rising again — 26.6% of Italian adults in 2024, reversing the long-term decline (Possenti et al., 2025)
- Last major national measure: 2005 Sirchia indoor ban → ~8% short-term reduction in consumption, especially youth (Gallus et al., 2006)
- Nothing comparable at national level in two decades
- E-cigarettes and heated tobacco failed to reduce overall nicotine use (Asta et al., 2025)
- Milan's 2025 ban: most significant Italian tobacco control step in a generation; argued as replicable model for other European cities (La Vecchia et al., 2025)

**Media — significant international attention:**

- *New York Times*: examined compliance on Milan streets one month after the ban
- *Euronews*: framed it as the strictest urban smoking measure to date
- *Anadolu Agency*: public health advocates (passive smoking deaths, cigarette butt pollution) vs. retailers contesting on jurisdictional grounds
- Trade press (*Hospitality Inside*): enforcement confusion, unclear rules for outdoor terraces, described as largely symbolic
- *Italian American Herald*: ban applies to all **Milan–Cortina 2026 Winter Olympics** venues

---

## 4. Intro to Our Approach

- Research question: did the January 2025 ban produce a measurable reduction in ambient PM2.5 and PM10?
- Two-part approach:
  - **Time series (SARIMAX):** model seasonal dynamics, forecast 2025
  - **Causal inference (DID):** Milan (treated) vs. Turin (control), pre/post Jan 2, 2025
- Why Turin? Same Po Valley airshed, similar regional meteorology, no equivalent policy
- Turin's limitations: automotive-heavy industry, lower baseline PM, only one sensor
- Parallel trends assumption tested graphically + pre-trend interact. (p = 0.837 ✓)

---

## 5. GitHub Structure

- Project fully reproducible and version-controlled on GitHub
- `README.md` as entry point — see structure below:

```
├── Data Analysis/
│   ├── API/          data collection notebooks (PurpleAir API pull, 2022–2025)
│   ├── Data/         raw CSVs — milan_air_quality.csv, turin_air_quality.csv
│   ├── Analysis/     city-level EDA, outlier treatment, SARIMAX forecasting
│   ├── Regression/   DID regression, event study, results plot
│   ├── Figures/      all output plots and sensor maps
│   └── Maps/         folium sensor location maps
├── Reports/
│   ├── abstract.md
│   ├── data_analysis_report.md   (time series methods, DID design, limitations)
│   ├── report.md                 (full policy report — review, findings, advice)
│   ├── policy_frame_report.md   (detailed frame analysis — actors, institutions)
│   └── presentation_outline.md  (slide-by-slide presentation outline)
└── Sources/
    ├── bibliography.md
    ├── milan-policy-english.md
    └── milan-policy-italian.md
```

---

## 6. Data

- Source: **PurpleAir API** (`api.purpleair.com/v1/sensors`), daily resolution (`average=1440`)
- Variables: PM2.5, PM10, temperature, humidity, pressure
- **Milan:** 7 sensors, bounding box 45.35–45.55°N / 8.95–9.40°E, Jan 2022 – Dec 2025
- **Turin:** 1 sensor (ID 133001), Feb 2022 – Dec 2025
- Weekly aggregation used for DID to reduce day-to-day noise
- Missing weather controls (wind, precipitation) — potential omitted variable bias

---

## 7. Sensor Outliers — Treatment and Story

- **The story:** raw data contained physically implausible extremes — Milan PM2.5 max: **2,043 µg/m³**; Turin: **1,303 µg/m³** — typical of low-cost optical counters under humidity and drift
- **Milan — 5 of 7 sensors erratic** (IDs 188041, 188043, 188049, 256425, 264579)
  - Two reference sensors identified: **6540 (Piazza Sempione)** and **31569 (Gaggiano MI)**
  - Readings outside **mean ± 3σ** of reference distribution → flagged, linearly interpolated
  - Applied per sensor before aggregating to daily city mean
- **Turin — single sensor**
  - No cross-reference possible → **rolling median ± 2×MAD** (30-day centred window)
  - K = 2.0 chosen to be strict given high noise; flagged values linearly interpolated
- Key limitation: reference sensors assumed well-calibrated — cannot be verified without regulatory monitor co-location

---

## 8. Findings

- **SARIMAX(1,1,1)(1,1,1,7)** + K=3 Fourier pairs for annual seasonality + temperature & humidity
  - ADF tests confirm stationarity; clear weekly and annual cycles in both cities
  - 2025 forecasts track observed seasonal patterns — no anomalous post-ban dip
- **DID results:**

| | PM2.5 | PM10 |
|---|---|---|
| DID coefficient (δ) | +1.70 µg/m³ | +1.92 µg/m³ |
| Std. error (HC1) | 1.26 | 1.51 |
| p-value | 0.175 | 0.202 |
| R² | 0.949 | 0.949 |

- **No statistically significant effect** — the ban explains none of the variation
- Event study: no pre-trend, no post-treatment break
- Not surprising: outdoor cigarette smoke is a negligible fraction of urban PM relative to traffic, heating, and industry

---

## 9. Conclusion and Suggestions

- **Bottom line:** no measurable reduction in PM2.5 or PM10 attributable to the January 2025 ban in its first year
- The environmental framing of the ban is scientifically weak — smoking is the wrong target for an air quality regulation
- The genuine case for the ban rests on public health grounds (secondhand smoke, cigarette butt pollution, norm shift) — this should be the primary justification

**Suggestions:**

1. **Better sensors**
   - invest in regulatory-grade reference monitors co-located with low-cost devices
   - broader geographic coverage across city districts
   - continuous cross-calibration
   - without this: small signals undetectable, enforcement hotspots unidentifiable

2. **Better policy framing**
   - reposition outdoor smoking article within a public health ordinance, not an environmental regulation
   - air quality framework fits other provisions (biomass, diesel generators, construction dust)
   - wrong lens for smoking

---

## 10. Thanks

- Thank you
- Repository: `https://github.com/cseresznyeszeteny/UST4158_202526_LD_BS_ZC`
- Contact: drini_liza@student.ceu.edu, szalma_benedek@student.ceu.edu, cseresznyes_zeteny@student.ceu.edu

---

**References**

Asta, F., et al. "New Tobacco Products and Smoking Prevalence in Italy: A Double-Intervention Time Series Analysis." *European Journal of Public Health* 35, Supplement 4 (2025).

Gallus, S., et al. "Effects of New Smoking Regulations in Italy." *Annals of Oncology* 17, no. 2 (2006): 346–347.

La Vecchia, C., et al. "Milan, Italy: New Smoking Regulation in Public Places, Effective January 2025." *Journal of Health Inequalities* 11, no. 1 (2025): 1–3.

Possenti, I., et al. "Prevalence of Cigarette Smoking and Secondhand Smoke Exposure in Italy in 2024." *Tumori Journal* (2025).

Anadolu Agency. "Milan to Ban Smoking in Public Places Starting 2025." December 2024.

Anadolu Agency. "Smoke-Free Milan? New Ban Ignites Debate on Liberties." January 2025.

Euronews. "Milan Cracks Down on Outdoor Smoking in Toughest Ban to Date." January 1, 2025.

*Hospitality Inside.* "Milan Struggles with Outdoor Smoking Ban." 2025.

*Italian American Herald.* "Milan's Rules on Smoking Extend to Venues at 2026 Winter Olympics." January 19, 2026.

*The New York Times.* "Milan's Outdoor Smoking Ban." February 5, 2025.
