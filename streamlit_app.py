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

# Display Team Logos if found
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

# Prediction button
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
# Function to get team logos based on full name, short forms, and location
def get_team_logo(team_name):
    team_logos = {
        "Los Angeles Lakers": ["Lakers", "LAL", "Los Angeles"],
        "Golden State Warriors": ["Warriors", "GSW", "Golden State"],
        "Boston Celtics": ["Celtics", "BOS", "Boston"],
        "Chicago Bulls": ["Bulls", "CHI", "Chicago"],
        "Miami Heat": ["Heat", "MIA", "Miami"],
        "Brooklyn Nets": ["Nets", "BKN", "Brooklyn"],
        "New York Knicks": ["Knicks", "NYK", "New York"],
        "Phoenix Suns": ["Suns", "PHX", "Phoenix"],
        "Milwaukee Bucks": ["Bucks", "MIL", "Milwaukee"],
        "Philadelphia 76ers": ["76ers", "PHI", "Philadelphia"],
        "Toronto Raptors": ["Raptors", "Toronto", "TR"],
        "Dallas Mavericks": ["Mavericks", "Mavs", "DAL", "Dallas"],
        "Denver Nuggets": ["Nuggets", "DEN", "Denver"],
        "Houston Rockets": ["Rockets", "HOU", "Houston"],
        "Los Angeles Clippers": ["Clippers", "LAC", "Los Angeles"],
        "Memphis Grizzlies": ["Grizzlies", "MEM", "Memphis"],
        "Minnesota Timberwolves": ["Timberwolves", "Wolves", "MIN", "Minnesota"],
        "New Orleans Pelicans": ["Pelicans", "NOP", "New Orleans"],
        "Oklahoma City Thunder": ["Thunder", "OKC", "Oklahoma City"],
        "Orlando Magic": ["Magic", "ORL", "Orlando"],
        "Portland Trail Blazers": ["Trail Blazers", "Blazers", "POR", "Portland"],
        "Sacramento Kings": ["Kings", "SAC", "Sacramento"],
        "San Antonio Spurs": ["Spurs", "SAS", "San Antonio"],
        "Utah Jazz": ["Jazz", "UTA", "Utah"],
        "Washington Wizards": ["Wizards", "WAS", "Washington"],
        "Indiana Pacers": ["Pacers", "IND", "Indiana"],
        "Cleveland Cavaliers": ["Cavaliers", "Cavs", "CLE", "Cleveland"],
        "Charlotte Hornets": ["Hornets", "CHA", "Charlotte"],
        "Detroit Pistons": ["Pistons", "DET", "Detroit"],
        "Atlanta Hawks": ["Hawks", "ATL", "Atlanta"],
    }

    nba_logo_base_url = "https://cdn.nba.com/logos/nba"

    # Convert user input to lowercase for better matching
    team_name = team_name.lower()

    # Loop through team_logos dictionary to find a match
    for full_name, aliases in team_logos.items():
        if team_name in [full_name.lower()] + [alias.lower() for alias in aliases]:
            team_id = list(team_logos.keys()).index(full_name) + 1610612737  # NBA Team IDs start from 1610612737
            return f"{nba_logo_base_url}/{team_id}/primary/L/logo.svg"

    return None  # Return None if no match found


