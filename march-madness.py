from helpers import Matchup, Team
import numpy as np
import pandas as pd



def get_teams():
    teams = []
    tournament_teams_df = pd.read_csv("data/MNCAATourneySeeds.csv")
    tournament_teams_df = tournament_teams_df.loc[tournament_teams_df["Season"] == 2026]
    teams_df = pd.read_csv("data/MTeams.csv")
    for team in tournament_teams_df.itertuples(index=False):
        print(team)
        team_id = team[2]
        team_name = teams_df.loc[teams_df["TeamID"] == team_id]["TeamName"].squeeze()
        seed = team[1]
        teams.append(Team(id=team_id, draw_location=seed, name=team_name))

    return teams


def predict_matchup(matchup: Matchup):
    """Returns True if team 1 wins, false if team 2 wins"""
    ###
    # ADD TOURNAMENT PREDICTION LOGIC BELOW
    
    # e.g.: always predict the higher seeded team to win
    if matchup.team1.seed <= matchup.team2.seed:
        return True
    return False

    # END TOURNAMENT PREDICTION LOGIC
    ###

def create_first_round_matchups():
    regions = "WXYZ"
    

if __name__ == "__main__":
    teams = get_teams()

    # simulate each game

    # send to mm api endpoint
