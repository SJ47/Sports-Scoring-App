class Team:
    def __init__(self, team_name, league_id, id = None):
        self.team_name = team_name
        self.league_id = league_id
        self.id = id
        self.players = []

