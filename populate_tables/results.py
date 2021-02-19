import csv
from .convert_season import convert_season
from .convert_medal import convert_medal
from .variables_mapping import (athlete_id_index, medal_index, sport_index,
                                event_index, game_year_index, season_index)


def form_results(games, events, sports):
    with open('athlete_events.csv') as athletes_file:
        reader = csv.reader(athletes_file)
        results = []
        for row in reader:
            if reader.line_num == 1:
                continue
            season = row[season_index]
            season = convert_season(season)
            if row[game_year_index] == '1906':
                continue
            athlete_id = row[athlete_id_index]
            medal = row[medal_index]
            event_id = events[row[event_index]]['id']
            game_hash = row[game_year_index] + str(season)
            game_id = games[game_hash]['id']
            sport_id = sports[row[sport_index]]['id']

            medal = convert_medal(medal)
            result = {'athlete_id': athlete_id,
                      'game_id': game_id,
                      'sport_id': sport_id,
                      'event_id': event_id,
                      'medal': medal}
            results.append(result)

        return results
