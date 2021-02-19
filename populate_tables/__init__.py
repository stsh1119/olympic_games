from .sports import form_unique_sports_list
from .teams import form_unique_team_list
from .events import form_unique_events_list
from .games import form_unique_valid_games
from .athletes import form_unique_athletes
from .results import form_results
from .insert_to_db import insert_to_db

teams = form_unique_team_list()
games = form_unique_valid_games()
events = form_unique_events_list()
sports = form_unique_sports_list()
athletes = form_unique_athletes(teams)
results = form_results(games, events, sports)


def populate_db():
    insert_to_db(teams, games, events, sports, athletes, results)
    print('Tables are populated with the data.')
