-- File to create database tables by running "psql -d sports_scoring_app -f sports_scoring_app.sql"

DROP TABLE leagues;
DROP TABLE teams;
DROP TABLE players;
DROP TABLE fixtures;

CREATE TABLE leagues (
  id SERIAL PRIMARY KEY,
  league_name VARCHAR(255)
);

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255),
  league_id INT REFERENCES leagues(id)
);

CREATE TABLE players(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  team_id INT REFERENCES teams(id),
  goals_scored INT,
  yellow_cards INT,
  red_cards INT
);

CREATE TABLE fixtures(
  id SERIAL PRIMARY KEY,
  team_home_id INT REFERENCES teams(id),
  team_away_id INT REFERENCES teams(id),
  fixture_date DATE,
  fixture_result VARCHAR(7),
  league_id INT REFERENCES leagues(id)
);