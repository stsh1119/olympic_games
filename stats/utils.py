from operator import itemgetter
import sqlite3
import sys


def build_chart(data, obj):
    r = '█'
    if obj['chart'] == 'medals':
        print('YEAR AMOUNT')

    elif obj['chart'] == 'top-teams':
        print('NOC AMOUNT')

    # * Uses index in list to sort elements so that, where 1st is the biggest
    results = sorted(data, key=itemgetter(1), reverse=True)
    # print(results)
    highest = results[0][1]
    k = 200/highest
    for result in data:
        country = result[0]
        length = float(result[1])
        symbol_lenght = int(k * length)
        symbol_lenght = symbol_lenght * r
        print(f'{country} {symbol_lenght}')


def convert_medal(medal):
    if medal == 'gold':
        medal = 1
    elif medal == 'silver':
        medal = 2
    elif medal == 'bronze':
        medal = 3

    return medal


def convert_season(season):
    if season == 'winter':
        season = '1'
    else:
        season = '0'

    return season


def get_from_db(input_data):
    connection = sqlite3.connect('olympic_history.db')
    cursor = connection.cursor()

    if input_data['chart'] == 'medals':

        if 'medal' in input_data.keys():
            result = cursor.execute(f'''select g.year, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and t.noc_name = '{input_data["noc"]}'
            and g.season = {input_data["season"]}
            and r.medal = {input_data["medal"]}
            group by g.year
            order by g.year;''').fetchall()

        else:
            result = cursor.execute(f'''select g.year, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and t.noc_name = '{input_data["noc"]}'
            and g.season = {input_data["season"]}
            group by g.year
            order by g.year;''').fetchall()

    elif input_data['chart'] == 'top-teams':

        if 'year' in input_data.keys() and 'medal'not in input_data.keys():

            result = cursor.execute(f'''select t.noc_name, count(r.medal) medals
        from teams t, results r, athletes a, games g
        where r.athlete_id = a.id
        and a.team_id = t.id
        and g.id = r.game_id
        and g.season = {input_data["season"]}
        and g.year = {input_data["year"]}
        group by t.noc_name
        order by medals desc;''')

        if 'year' not in input_data.keys() and 'medal' in input_data.keys():

            result = cursor.execute(f'''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = {input_data["season"]}
            and r.medal = {input_data["medal"]}
            group by t.noc_name
            order by medals desc;''').fetchall()

        elif 'year' and 'medal' in input_data.keys():
            result = cursor.execute(f'''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = {input_data["season"]}
            and r.medal = {input_data["medal"]}
            and g.year = {input_data["year"]}
            group by t.noc_name
            order by medals desc;''').fetchall()

        else:
            result = cursor.execute(f'''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = {input_data["season"]}
            group by t.noc_name
            order by medals desc;''').fetchall()

    connection.close()

    return result


def get_noc_from_db():
    connection = sqlite3.connect('olympic_history.db')
    cursor = connection.cursor()
    noc_names_raw = cursor.execute('select noc_name from teams;').fetchall()

    return noc_names_raw


def get_years_from_db():
    connection = sqlite3.connect('olympic_history.db')
    cursor = connection.cursor()
    game_years_raw = cursor.execute('select year from games;').fetchall()

    return game_years_raw


def prettify_year(raw_output):
    years = []
    years_str = []
    for year in raw_output:
        years.append(year[0])  # takes first element from tuple

    for year in years:
        years_str.append(str(year))  # converts int list to str list

    return years_str


def prettify_noc(raw_output):
    noc_names = []
    for team in raw_output:
        noc_names.append(team[0])

    return noc_names


def validate_input(raw_input):
    if raw_input['chart'] == 'medals':
        if 'season' not in raw_input.keys():
            print('Season is mandatory parameter')
            sys.exit()
        if 'noc' not in raw_input.keys():
            print('NOC is mandatory parameter')
            sys.exit()
    elif raw_input['chart'] == 'top-teams':
        if 'season' not in raw_input.keys():
            print('Season is mandatory parameter')
            sys.exit()

    return raw_input
