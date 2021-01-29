class League:
    def __init__(self, league_name, league_size, id = None):
        self.league_name = league_name
        self.league_size = league_size
        self.id = id
        self.league_teams = []

    def add_team_to_league(self):
        pass

    def remove_team_from_league(self):
        pass

    def edit_team_in_league(self):
        pass

    def display_league_table(self):
        pass

    
    # Return true if the correct number of teams are in the league otherwise return false
    def check_correct_number_of_teams_for_league_size(self):
        return len(self.league_teams) == self.league_size

