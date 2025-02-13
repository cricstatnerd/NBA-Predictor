import streamlit as st

# Set page configuration
st.set_page_config(page_title="🏀 NBA Match Predictor", page_icon="🏆", layout="centered")

# Function to get team logos
def get_team_logo(team_name):
    team_logos = {
        "Lakers": "https://cdn.nba.com/logos/nba/1610612747/primary/L/logo.svg",
        "Warriors": "https://cdn.nba.com/logos/nba/1610612744/primary/L/logo.svg",
        "Celtics": "https://cdn.nba.com/logos/nba/1610612738/primary/L/logo.svg",
        "Bulls": "https://cdn.nba.com/logos/nba/1610612741/primary/L/logo.svg",
        "Heat": "https://cdn.nba.com/logos/nba/1610612748/primary/L/logo.svg",
        "Nets": "https://cdn.nba.com/logos/nba/1610612751/primary/L/logo.svg",
        "Knicks": "https://cdn.nba.com/logos/nba/1610612752/primary/L/logo.svg",
        "Suns": "https://cdn.nba.com/logos/nba/1610612756/primary/L/logo.svg",
        "Bucks": "https://cdn.nba.com/logos/nba/1610612749/primary/L/logo.svg",
        "76ers": "https://cdn.nba.com/logos/nba/1610612755/primary/L/logo.svg"
    }
    return team_logos.get(team_name, None)  # Return logo URL if found, else None

# Title
st.title("🏀 NBA Match Prediction & Betting Analyzer")

# Input fields (Initialize empty variables first)
team1 = st.text_input("🏠 Enter Home Team Name:", placeholder="e.g., Lakers")
team2 = st.text_input("🚀 Enter Away Team Name:", placeholder="e.g., Warriors")

# Only fetch logos if a team name is entered
if team1:
    team1_logo = get_team_logo(team1)
    if team1_logo:
        st.image(team1_logo, width=100, caption=team1)
    else:
        st.warning(f"❌ No logo found for {team1}. Try another team name.")

if team2:
    team2_logo = get_team_logo(team2)
    if team2_logo:
        st.image(team2_logo, width=100, caption=team2)
    else:
        st.warning(f"❌ No logo found for {team2}. Try another team name.")


