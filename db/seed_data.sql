-- Dummy data to fill database tables 

-- Seed league name data 
INSERT INTO leagues (league_name, league_size) VALUES ('Scottish Premiership', 12);

--  Seed league teams into the league with league_id of 1
INSERT INTO teams (team_name, league_id) VALUES ('Rangers', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Celtic', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Aberdeen', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Hibernian', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Livingston', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Dundee United', 1);
INSERT INTO teams (team_name, league_id) VALUES ('St Mirren', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Kilmarnock', 1);
INSERT INTO teams (team_name, league_id) VALUES ('St Johnstone', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Motherwell', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Ross County', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Hamilton Academical', 1);

--  Seed some sample players into team with correct team_id
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Ranplayer', 'One', 1, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Ranplayer', 'Two', 1, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Ranplayer', 'Three', 1, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Ranplayer', 'Four', 1, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Celplayer', 'One', 2, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Celplayer', 'Two', 2, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Celplayer', 'Three', 2, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Celplayer', 'Four', 2, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Abeplayer', 'One', 3, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Abeplayer', 'Two', 3, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Abeplayer', 'Three', 3, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Abeplayer', 'Four', 3, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hibplayer', 'One', 4, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hibplayer', 'Two', 4, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hibplayer', 'Three', 4, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hibplayer', 'Four', 4, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Livplayer', 'One', 5, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Livplayer', 'Two', 5, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Livplayer', 'Three', 5, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Livplayer', 'Four', 5, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Dunplayer', 'One', 6, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Dunplayer', 'Two', 6, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Dunplayer', 'Three', 6, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Dunplayer', 'Four', 6, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stmplayer', 'One', 7, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stmplayer', 'Two', 7, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stmplayer', 'Three', 7, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stmplayer', 'Four', 7, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Kilplayer', 'One', 8, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Kilplayer', 'Two', 8, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Kilplayer', 'Three', 8, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Kilplayer', 'Four', 8, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stjplayer', 'One', 9, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stjplayer', 'Two', 9, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stjplayer', 'Three', 9, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Stjplayer', 'Four', 9, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Motplayer', 'One', 10, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Motplayer', 'Two', 10, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Motplayer', 'Three', 10, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Motplayer', 'Four', 10, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Rosplayer', 'One', 11, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Rosplayer', 'Two', 11, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Rosplayer', 'Three', 11, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Rosplayer', 'Four', 11, 0, 0, 0);

INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hamplayer', 'One', 12, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hamplayer', 'Two', 12, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hamplayer', 'Three', 12, 0, 0, 0);
INSERT INTO players (first_name, last_name, team_id, goals_scored, yellow_cards, red_cards) VALUES ('Hamplayer', 'Four', 12, 0, 0, 0);

--  Seed some sample fixtures into team with correct team_home_id, team_away_id and league_id
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (1, 2, '20-01-2021', '2-0', 1);
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (3, 4, '20-01-2021', '1-1', 1);
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (5, 6, '20-01-2021', '2-3', 1);
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (7, 8, '20-01-2021', '1-0', 1);
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (9, 10, '20-01-2021', '0-1', 1);
INSERT INTO fixtures (team_home_id, team_away_id, fixture_date, fixture_result, league_id) VALUES (11, 12, '20-01-2021', '2-2', 1);

