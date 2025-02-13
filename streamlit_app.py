import streamlit as st

# Set page configuration for a better look
st.set_page_config(page_title="🏀 NBA Match Predictor", page_icon="🏆", layout="centered")

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #ff1c1c;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with emoji
st.title("🏀 NBA Match Prediction & Betting Analyzer")

# Input fields with placeholder text
team1 = st.text_input("🏠 Enter Home Team Name:", placeholder="e.g., Lakers")
team2 = st.text_input("🚀 Enter Away Team Name:", placeholder="e.g., Warriors")

# Prediction button with better UI
if st.button("🔮 Predict Winner"):
    if team1 and team2:
        predicted_winner = team1 if len(team1) > len(team2) else team2
        st.success(f"🏆 **Predicted Winner:** {predicted_winner}")
    else:
        st.warning("⚠️ Please enter both team names!")

# Betting Analysis button
if st.button("📊 Analyze Betting Odds"):
    if team1 and team2:
        st.info(f"💰 **Suggested Bet:** {team1} (-3.5) vs {team2} (+3.5)")
    else:
        st.warning("⚠️ Please enter both team names!")

