# Smoking Ban in Milan: Policy Review and Short-Term Effects on Air Quality
**UGST4158 — Introduction to Public Policy 2025/26 Winter**
Central European University — Quantitative Methods Seminar
Liza Drini · Benedek Szalma · Zeteny Cseresznyes

---

## Introduction

Milan is among the most air-polluted cities in Europe, situated in the Po Valley where topography and meteorology trap particulate matter year-round. Against this backdrop, the Municipality of Milan adopted a comprehensive Air Quality Regulation in November 2020 (Resolution No. 56), imposing restrictions on heating systems, construction sites, commercial generators, and outdoor combustion. A phased outdoor smoking ban — introduced for parks, playgrounds, bus stops, and sports areas from January 2021 — culminated in a full citywide ban on all public outdoor spaces effective January 2, 2025, with fines of €40–€240. This report reviews the policy, examines existing literature, and evaluates whether the ban produced a measurable reduction in ambient particulate matter in its first year.

---

## The Policy

Milan's 2020 Air Quality Regulation frames outdoor smoking restrictions explicitly as an air quality measure, citing recurring exceedances of EU PM and NOx concentration limits and the "polluter pays" principle of the Consolidated Environmental Act (D.lgs. 152/2006). Article 9 of the Regulation imposed area-specific bans from 2021, with the January 2025 extension (Art. 9.2) applying to all public and publicly accessible outdoor areas. Enforcement is entrusted to the Polizia Locale, though early implementation saw very few fines issued. The stated environmental goal is to reduce locally generated particulate matter and improve ambient air quality across the city. The regulation sits within a broader package that also targets biomass combustion, diesel generators, and construction dust — sources that contribute far more to urban PM than outdoor smoking.

The ban is better understood as a symptomatic response than a solution to root causes. The official framing is dominated by the environmental rationale, with a secondary moral dimension — protecting vulnerable groups such as children and pregnant women from passive smoke exposure — remaining largely implicit. The principal policy entrepreneur is Mayor Giuseppe Sala, who championed the measure as part of the city's Air and Climate Plan. Key opposing interests include tobacco producers, retailers, and hospitality operators, who contested both the jurisdictional basis and the implementation rules. For a detailed analysis of the policy frame, actors, institutions, and decision mode, see `policy_frame_report.md`.

---

---

## Literature and Articles Review

Italy's most significant tobacco control measure to date was the 2005 Sirchia Law banning indoor smoking in public places. Gallus et al. (2006) found an approximately 8% short-term reduction in cigarette consumption following that ban, especially among young smokers. Despite this, Italy's Tobacco Control Scale ranking fell from 8th to 18th in Europe between 2006 and 2021, and Possenti et al. (2025) report that 26.6% of Italian adults were current smokers in 2024 — a reversal of the long-term declining trend. Asta et al. (2025) further show that the spread of e-cigarettes and heated tobacco products did not reduce overall nicotine use. La Vecchia et al. (2025) contextualise Milan's 2025 ban as the first major Italian tobacco control step in two decades and argue it offers a replicable model for other European cities. Media coverage has highlighted both public health support (reduced secondhand smoke, cigarette butt pollution) and criticism from business associations and hospitality operators over enforcement and implementation ambiguity. The ban's entry into force also coincides with the lead-up to the Milan–Cortina 2026 Winter Olympics, raising its international profile.

---

## Data

Air quality data were sourced from the **PurpleAir API** at daily resolution (January 2022 – December 2025). Variables used: PM2.5 and PM10 atmospheric concentrations, temperature, and humidity. Milan was covered by **7 low-cost optical sensors**; Turin (the control city) by **1 sensor** (ID 133001). Raw data contained physically implausible extremes (Milan PM2.5 max: 2,043 µg/m³), typical of uncalibrated consumer-grade sensors operating under high-humidity conditions. For Milan, readings outside mean ± 3σ of two reference sensors (IDs 6540 and 31569) were flagged and linearly interpolated. For Turin's single sensor, a rolling median ± 2×MAD filter (30-day window) was applied. After cleaning, series were aggregated to one daily observation per city and further to weekly averages for the regression.

---

## Methodology

Two analytical approaches were used. First, **SARIMAX(1,1,1)(1,1,1,7)** models with annual Fourier terms (K=3 pairs, period=365.25 days) were fitted separately for PM2.5 and PM10 in each city to characterise seasonal dynamics and produce out-of-sample forecasts for 2025. Second, a **difference-in-differences (DID)** regression estimated the causal effect of the ban:

> **PM_it = α + δ · (treat × post)_it + β · temperature_it + γ · humidity_it + μ_i + λ_t + ε_it**

where Milan is the treated unit (ban from Jan 2, 2025), Turin the control, with city and week fixed effects absorbing baseline level differences and common seasonal shocks. HC1 robust standard errors were used; city-level clustering is infeasible with two units. Parallel trends were tested graphically and via a pre-period treat×time interaction (p = 0.837, supporting the assumption). An event study with monthly bins traced the dynamic treatment path.

---

## Findings

The DID coefficient is positive and statistically insignificant for both pollutants: **δ = +1.70 µg/m³ for PM2.5** (SE = 1.26, p = 0.175) and **δ = +1.92 µg/m³ for PM10** (SE = 1.51, p = 0.202). Overall model fit is high (R² ≈ 0.949), reflecting strong city and week fixed effects, but the ban itself explains none of the variation. The event study shows no systematic pre-trend and no post-treatment break. SARIMAX forecasts for 2025 track the observed seasonal cycle but show no anomalous post-ban dip relative to predicted levels. In short, no measurable reduction in PM2.5 or PM10 attributable to the January 2025 outdoor smoking ban is detected in the first year of data.

---

## Conclusions and Policy Advice

The absence of a detectable effect is not surprising given what we know about urban PM sources: outdoor cigarette smoke is a negligible contributor to ambient PM2.5 relative to road traffic, industrial emissions, and residential heating — the dominant sources in the Po Valley. Two concrete recommendations follow.

**1. Invest in better monitoring infrastructure.** The analysis was severely constrained by sensor quality and coverage. Five of Milan's seven PurpleAir sensors produced systematically erratic data; Turin relied on a single consumer-grade device. A robust policy evaluation — and credible enforcement — requires regulatory-grade reference monitors co-located with low-cost sensors, broader geographic coverage across city districts, and continuous cross-calibration. Without this, it is impossible to detect small pollution signals or identify enforcement hotspots.

**2. Reframe the policy rationale.** Framing the outdoor smoking ban primarily as an air quality measure is scientifically weak and leaves the policy vulnerable to legal and public legitimacy challenges. The genuine benefits of the ban — protecting non-smokers from secondhand smoke exposure in shared outdoor spaces, reducing cigarette butt waste, and supporting a broader public health norm shift — are well-supported by evidence and would constitute a more robust justification. The air quality framework is appropriate and effective for the regulation's other provisions (heating systems, construction machinery, diesel generators); it is the wrong lens for outdoor smoking. Repositioning the smoking article within a public health ordinance, rather than an environmental one, would better reflect the evidence and improve policy coherence.
