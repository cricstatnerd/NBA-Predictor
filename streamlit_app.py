import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="🏀 NBA Match Predictor & Betting Insights", page_icon="🏆", layout="centered")

# Function to get accurate team logos based on full name, short forms, and city names
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
        "Los Angeles Clippers": ["Clippers", "LAC", "Los Angeles Clippers"],
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

    nba_team_ids = {
        "Los Angeles Lakers": "1610612747",
        "Golden State Warriors": "1610612744",
        "Boston Celtics": "1610612738",
        "Chicago Bulls": "1610612741",
        "Miami Heat": "1610612748",
        "Brooklyn Nets": "1610612751",
        "New York Knicks": "1610612752",
        "Phoenix Suns": "1610612756",
        "Milwaukee Bucks": "1610612749",
        "Philadelphia 76ers": "1610612755",
        "Toronto Raptors": "1610612761",
        "Dallas Mavericks": "1610612742",
        "Denver Nuggets": "1610612743",
        "Houston Rockets": "1610612745",
        "Los Angeles Clippers": "1610612746",
        "Memphis Grizzlies": "1610612763",
        "Minnesota Timberwolves": "1610612750",
        "New Orleans Pelicans": "1610612740",
        "Oklahoma City Thunder": "1610612760",
        "Orlando Magic": "1610612753",
        "Portland Trail Blazers": "1610612757",
        "Sacramento Kings": "1610612758",
        "San Antonio Spurs": "1610612759",
        "Utah Jazz": "1610612762",
        "Washington Wizards": "1610612764",
        "Indiana Pacers": "1610612754",
        "Cleveland Cavaliers": "1610612739",
        "Charlotte Hornets": "1610612766",
        "Detroit Pistons": "1610612765",
        "Atlanta Hawks": "1610612737",
    }

    nba_logo_base_url = "https://cdn.nba.com/logos/nba"

    # Convert user input to lowercase for better matching
    team_name = team_name.lower()

    for full_name, aliases in team_logos.items():
        if team_name in [full_name.lower()] + [alias.lower() for alias in aliases]:
            team_id = nba_team_ids[full_name]
            return f"{nba_logo_base_url}/{team_id}/primary/L/logo.svg"

    return None


# Function to fetch live betting odds safely
def get_live_odds(team1, team2):
    api_key = "ff792c945f4baf64646ddec57299ca60"  # Replace with your actual API key
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds?apiKey={api_key}&regions=us&markets=h2h,spreads&oddsFormat=decimal"

    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP failures
        data = response.json()

        # Debugging: Print out the entire API response to understand its structure
        st.write("API Response:", data)

        odds_found = False  # Flag to check if we find odds

        for game in data:
            if "teams" in game and isinstance(game["teams"], list):
                game_teams = game["teams"]
                if team1 in game_teams and team2 in game_teams:
                    if "bookmakers" in game and len(game["bookmakers"]) > 0:
                        outcomes = game["bookmakers"][0].get("markets", [{}])[0].get("outcomes", [])
                        if len(outcomes) >= 2:
                            odds_found = True
                            return f"🏀 **Odds for {team1} vs {team2}:**\n🔹 **{team1}:** {outcomes[0].get('price', 'N/A')}x\n🔹 **{team2}:** {outcomes[1].get('price', 'N/A')}x"

        # If no odds are found
        if not odds_found:
            return "⚠️ No live odds available for this match."

    except requests.exceptions.RequestException as e:
        return f"❌ API Error: {e}"
    except (KeyError, IndexError, TypeError):
        return "⚠️ Error retrieving betting odds. Please try again later."
