class Team:
    def __init__(self, id, name, draw_location):
        self.id = id
        self.name = name
        self.seed = int(draw_location[1:3])
        self.draw_location = draw_location
        
class Matchup:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2
        self.winner = 0 # 1 for team 1, 2 for team 2, 0 for unsimulated
        
    def result(self):
        return self.winner
        
