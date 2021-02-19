import csv
from .variables_mapping import team_index, noc_team_index


def form_unique_team_list():
    with open('athlete_events.csv') as athletes_file:
        reader = csv.reader(athletes_file)
        teams_table = {}
        for row in reader:
            team = row[team_index]
            team_id = reader.line_num
            noc_team = row[noc_team_index]
            if '"' in team:
                team = team.replace('"', '')
            elif "'" in team:
                team = team.replace("'", '')
            if reader.line_num == 1:
                continue
            single_team = {'id': team_id,
                           'name': team,
                           'noc_name': noc_team}
            teams_table[noc_team] = single_team
        return teams_table
