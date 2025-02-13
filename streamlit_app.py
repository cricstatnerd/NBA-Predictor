import streamlit as st

st.title("🏀 NBA Match Prediction & Betting Analysis")

team1 = st.text_input("Enter Home Team Name")
team2 = st.text_input("Enter Away Team Name")

if st.button("Predict Winner"):
    st.write(f"🏆 Predicted Winner: {team1 if len(team1) > len(team2) else team2}")

if st.button("Analyze Betting Odds"):
    st.write(f"📊 Suggested Bet: {team1} (-3.5) vs {team2} (+3.5)")
