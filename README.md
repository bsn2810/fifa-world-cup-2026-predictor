# ⚽ FIFA World Cup 2026 Predictor

🚀 **Live Demo:** [Streamlit App](https://bsn2810-fifa-world-cup-2026-predictor-app.streamlit.app/)

📊 **Dataset:** [International Football Results Dataset](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017/code)

---

## Overview

The FIFA World Cup 2026 Predictor is a machine learning project that forecasts international football matches and simulates the FIFA World Cup 2026.

The project combines a custom-built Elo rating system with a Logistic Regression model trained on historical international football matches. These predictions are then used in a Monte Carlo tournament simulator to estimate each team's probability of winning the World Cup.

---

## Features

* ⚽ Match outcome prediction
* 📊 Team strength comparison dashboard
* 🏆 FIFA World Cup 2026 tournament simulation
* 📈 Monte Carlo championship probability estimation
* 🔢 Custom Elo rating system
* 🌐 Interactive Streamlit web application

---

## Model Performance

**Model:** Multinomial Logistic Regression

**Test Accuracy:** **60.16%**

### Classification Report

| Outcome  | Precision | Recall | F1-Score |
| -------- | --------- | ------ | -------- |
| Home Win | 0.57      | 0.69   | 0.63     |
| Draw     | 0.33      | 0.24   | 0.28     |
| Away Win | 0.73      | 0.74   | 0.74     |

### Features Used
* Elo Difference
* Absolute Elo Gap
* Recent Form Difference
* Recent Goal Difference Difference
* Tournament Importance Weight
* Home Advantage Indicator

---

## Methodology

### Custom Elo Rating System

A custom Elo rating system was implemented from scratch using international football matches played since 2000.

Unlike traditional Elo systems, match importance was incorporated through competition-specific weights, giving greater importance to World Cup matches and qualifiers while reducing the influence of friendlies.

### Tournament Simulation

World Cup matches are simulated using Monte Carlo methods.

After every simulated match:

* Elo ratings are updated
* Recent form is updated
* Goal difference metrics are updated

This allows team strengths to evolve dynamically throughout the tournament.

### Knockout Matches

Since knockout matches cannot end in draws, the model's predicted draw probability is removed and the remaining win probabilities are renormalized.

The Logistic Regression model predicts probabilities for:

* Home Win
* Draw
* Away Win

During knockout rounds, the draw probability is removed and the remaining probabilities are renormalized.

Example:

| Outcome    | Original Probability |
| ---------- | -------------------- |
| Team A Win | 45%                  |
| Draw       | 20%                  |
| Team B Win | 35%                  |

becomes

| Outcome    | Adjusted Probability |
| ---------- | -------------------- |
| Team A Win | 56.25%               |
| Team B Win | 43.75%               |

A winner is then sampled from the adjusted probabilities.

---

## Simulation Results

The tournament simulator was run thousands of times to estimate each nation's probability of winning the FIFA World Cup 2026.

| Team      | Win Probability |
| --------- | --------------- |
| Spain     | 27.16%          |
| Argentina | 15.45%          |
| France    | 7.56%           |
| England   | 7.16%           |
| Morocco   | 6.47%           |
| Colombia  | 5.56%           |
| Japan     | 3.41%           |
| Iran      | 2.71%           |
| Portugal  | 2.62%           |
| Brazil    | 2.57%           |

### Key Insights

* Spain emerged as the strongest team in the current model.
* Argentina remained one of the most likely champions due to its strong Elo rating and recent form.
* Morocco, Colombia, Japan, and Iran appeared as notable dark-horse contenders.
* Even the strongest teams rarely exceed a 30% chance of winning, highlighting the uncertainty of knockout football.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib
* Matplotlib

---

## Future Improvements

* Random Forest and XGBoost models
* Explicit modeling of extra time and penalty shootouts
* Player-level and squad-strength features
* Expected Goals (xG) based features
* Automated tournament bracket visualization

---

## Disclaimer

This project is intended for educational and analytical purposes. Football matches are inherently unpredictable, and actual tournament outcomes may differ significantly from model predictions.
