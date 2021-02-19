import csv


def form_unique_sports_list():
    with open('athlete_events.csv') as athletes_file:
        sports_list = {}
        reader = csv.reader(athletes_file)
        for row in reader:
            if reader.line_num == 1:
                continue
            sport = row[12]
            sport_id = reader.line_num

            single_sport = {'name': sport,
                            'id': sport_id}

            sports_list[sport] = single_sport

        return sports_list
