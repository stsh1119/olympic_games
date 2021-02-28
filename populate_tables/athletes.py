import re
import csv
from .variables_mapping import (full_name_index, sex_index, age_index, game_year_index,
                                noc_team_index, height_index, weight_index, athlete_id_index)


def form_unique_athletes(teams):
    with open('athlete_events.csv') as athletes_file:
        quotes_removal_mask = r'".*"'
        brackets_removal_mask = r' \(.*?\)'
        reader = csv.reader(athletes_file)
        athletes = {}
        for row in reader:
            single_athlete = {}
            if reader.line_num == 1:
                continue
            athlete_id = int(row[athlete_id_index])
            full_name = row[full_name_index]
            if '"' in full_name:
                full_name = re.sub(quotes_removal_mask, '', full_name)
                full_name = full_name.replace('"', '')
            if '(' or ')' in full_name:
                full_name = re.sub(brackets_removal_mask, '', full_name)
            full_name = full_name.strip()
            sex = row[sex_index]
            if sex == 'NA':
                sex = None
            try:
                year_of_birth = int(row[game_year_index]) - int(row[age_index])
            except ValueError:
                year_of_birth = None
            team_id = teams[row[noc_team_index]]['id']
            try:
                height = float(row[height_index])
            except ValueError:
                height = None
            try:
                weight = float(row[weight_index])
            except ValueError:
                weight = None
            if weight and height is not None:
                params = {'height': height,
                          'weight': weight}
            elif height is None:
                params = {'weight': weight}
                if weight is None:
                    params = {}
            elif weight is None:
                params = {'height': height}
                if height is None:
                    params = {}
            else:
                params = {}
            athlete_id = row[athlete_id_index]

            # composing athlete object
            single_athlete['full_name'] = full_name
            single_athlete['sex'] = sex
            single_athlete['year_of_birth'] = year_of_birth
            single_athlete['params'] = params
            single_athlete['team_id'] = team_id
            single_athlete['id'] = athlete_id

            athletes[athlete_id] = single_athlete
        return athletes
