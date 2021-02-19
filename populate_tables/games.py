import csv
from .convert_season import convert_season
from .variables_mapping import game_year_index, season_index, city_index


def form_unique_valid_games():
    with open('athlete_events.csv') as athletes_file:
        reader = csv.reader(athletes_file)
        unique_games = {}
        for row in reader:
            if reader.line_num == 1:
                continue

            game_year = int(row[game_year_index])
            if game_year == 1906:
                continue

            season = row[season_index]
            season = convert_season(season)
            city = row[city_index]
            g_id = reader.line_num
            game = {'game_year': game_year,
                    'season': season,
                    'city': city,
                    'id': g_id}

            key = str(game_year) + str(season)
            if key in unique_games.keys():
                if city not in unique_games[key]['city']:
                    unique_games[key]['city'] = unique_games[key]['city'] + ', ' + city
            else:
                unique_games[key] = game

        return unique_games
