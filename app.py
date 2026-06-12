import streamlit as st
import pandas as pd
import joblib

# Loading Saved Objects
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
elo = joblib.load("elo.pkl")
form = joblib.load("form.pkl")
gd = joblib.load("gd.pkl")

# Custom CSS to increase font sizes of all metrics on the page
st.markdown(
    """
    <style>
    [data-testid="stMetricValue"] {
        font-size: 50px !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        font-size: 25px !important;
    }
    div[data-testid="stSelectbox"] div[role="button"] {
        font-size: 20px !important;
        padding-top: 6px !important;
        padding-bottom: 6px !important;
    }
    div[data-testid="stSelectbox"] > div:nth-child(1) {
        background-color: #1e222b !important;
        border: 2px solid #4a5568 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSelectbox"] label p {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dict with flags emojis
flags = {
    "Algeria": "🇩🇿",
    "Argentina": "🇦🇷",
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Belgium": "🇧🇪",
    "Brazil": "🇧🇷",
    "Bosnia and Herzegovina": "🇧🇦",
    "Canada": "🇨🇦",
    "Cape Verde": "🇨🇻",
    "Colombia": "🇨🇴",
    "Croatia": "🇭🇷",
    "Curaçao": "🇨🇼",
    "Czech Republic": "🇨🇿",
    "DR Congo": "🇨🇩",
    "Ecuador": "🇪🇨",
    "Egypt": "🇪🇬",
    "England": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "France": "🇫🇷",
    "Germany": "🇩🇪",
    "Ghana": "🇬🇭",
    "Haiti": "🇭🇹",
    "Iran": "🇮🇷",
    "Iraq": "🇮🇶",
    "Ivory Coast": "🇨🇮",
    "Japan": "🇯🇵",
    "Jordan": "🇯🇴",
    "Mexico": "🇲🇽",
    "Morocco": "🇲🇦",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Norway": "🇳🇴",
    "Panama": "🇵🇦",
    "Paraguay": "🇵🇾",
    "Portugal": "🇵🇹",
    "Qatar": "🇶🇦",
    "Saudi Arabia": "🇸🇦",
    "Scotland": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
    "Senegal": "🇸🇳",
    "South Africa": "🇿🇦",
    "South Korea": "🇰🇷",
    "Spain": "🇪🇸",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "Tunisia": "🇹🇳",
    "Turkey": "🇹🇷",
    "United States": "🇺🇸",
    "Uruguay": "🇺🇾",
    "Uzbekistan": "🇺🇿",
}

# Page Config
st.set_page_config(page_title="Football Match Predictor", page_icon="⚽", layout="wide")

# Reusing the match predictor
def predict_match(home, away):
    conditions = {
        "elo_diff": elo[home] - elo[away],
        "elo_gap": abs(elo[home] - elo[away]),
        "form_diff": sum(form[home]) - sum(form[away]),
        "weight": 5,
        "gd_diff": sum(gd[home]) - sum(gd[away]),
        "home_advantage": 0
    }
    x = scaler.transform(pd.DataFrame([conditions]))
    probs = model.predict_proba(x)[0]

    return {"home_win": probs[2], "draw": probs[1], "away_win": probs[0]}

# Match Predictor Page
st.title("⚽ Football Match Predictor")
teams = sorted(list(elo.keys()))

# Dropdowns
col1, col2 = st.columns(2)
with col1:
    home = st.selectbox("Team 1", teams)
with col2:
    away = st.selectbox("Team 2", teams, index=1)

# Implementing the function
if st.button("Predict Match"):
    if home == away:
        st.error("Please select two different teams.")
    else:
        probs = predict_match(home, away)
        st.header(f"{flags[home]} {home} vs {flags[away]} {away}")
        st.subheader(f"**{flags[home]} {home} Win:** {probs['home_win']:.1%}")
        st.progress(float(probs["home_win"]))
        st.subheader(f"**Draw:** {probs['draw']:.1%}")
        st.progress(float(probs["draw"]))
        st.subheader(f"**{flags[away]} {away} Win:** {probs['away_win']:.1%}")
        st.progress(float(probs["away_win"]))
        st.divider()

        # Analysis
        st.header("Current Team Strengths")
        strength_col1, strength_col2 = st.columns(2)
        with strength_col1:
            st.subheader(f"{flags[home]} {home}")
            st.metric("Custom Elo", f"{elo[home]:.0f}")
            st.metric("Recent Form", sum(form[home]))
            st.metric("Goal Difference", sum(gd[home]))
        with strength_col2:
            st.subheader(f"{flags[away]} {away}")
            st.metric("Custom Elo", f"{elo[away]:.0f}")
            st.metric("Recent Form", sum(form[away]))
            st.metric("Goal Difference", sum(gd[away]))
