import numpy as np
import pandas as pd
import json


SEED_LOCATIONS = {
    1: 0,
    16: 1,
    8: 2,
    9: 3,
    5: 4,
    12: 5,
    4: 6,
    13: 7,
    6: 8,
    11: 9,
    3: 10,
    14: 11,
    7: 12,
    10: 13,
    2: 14,
    15: 15,
}

class Team:
    def __init__(self, id, name, draw_location):
        self.id = id
        self.name = name
        self.seed = int(draw_location[1:3])
        self.draw_location = draw_location


# final four:
#   w -|
#      + - |
#   x -|   |
#          + - champion
#   y -|   |
#      + - |
#   z -|
def create_bracket():
    bracket_with_regions = {}
    regions = "WXYZ"

    for region in regions:
        bracket_with_regions[region] = ["" for i in range(0, 16)]

    tournament_teams_df = pd.read_csv("data/MNCAATourneySeeds.csv")
    tournament_teams_df = tournament_teams_df.loc[tournament_teams_df["Season"] == 2026]
    teams_df = pd.read_csv("data/MTeams.csv")
    for team in tournament_teams_df.itertuples(index=False):
        team_id = team[2]
        team_name = teams_df.loc[teams_df["TeamID"] == team_id]["TeamName"].squeeze()
        seed = team[1]
        bracket_with_regions[seed[0]][SEED_LOCATIONS[int(seed[1:3])]] = Team(
            team_id, team_name, seed
        )
        
    bracket = []
    for region in regions:
        bracket = bracket + bracket_with_regions[region]
    return bracket


# def get_team_statistics(teamId):
#     season_stats_df = pd.read_csv("data/MNCAATourneyDetailedResults").loc[]

def predict_matchup(team1: Team, team2: Team):
    """Returns True if team 1 wins, false if team 2 wins"""
    ### ADD GAME PREDICTION LOGIC BELOW

    # e.g.: always predict the higher (better) seeded team to win
    if team1.seed <= team2.seed:
        return True
    return False

    ### END GAME PREDICTION LOGIC


if __name__ == "__main__":
    bracket = create_bracket()
    
    # simulate the games using predict_matchup function
    game_id = 0
    game_results_json = []
    while len(bracket) > 1:
        team1_wins = predict_matchup(bracket[0], bracket[1])
        if(team1_wins):
            bracket.append(bracket[0])
            print("{} d. {}".format(bracket[0].name, bracket[1].name))
        else:
            bracket.append(bracket[1])
            print("{} d. {}".format(bracket[1].name, bracket[0].name))
        game_results_json.append([{"name": bracket[0].name}, {"name": bracket[1].name}])
        bracket = bracket[2:]
        game_id += 1
    print("Champion: {}".format(bracket[0].name))
    
    # write results to json file
    json_str = json.dumps(game_results_json, indent=4)
    with open("simulation_results.json", "w") as f:
        f.write(json_str)