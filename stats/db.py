import sqlite3


def get_noc_names() -> list:
    """Functions returns a list of existing NOC names to check whether NOC given by user is valid."""
    noc_names = []
    with sqlite3.connect('olympic_history.db') as conn:
        cursor = conn.cursor()
        noc_name_tuples = cursor.execute('select noc_name from teams').fetchall()
    for team in noc_name_tuples:
        noc_names.append(team[0])

    return noc_names


def get_game_years() -> list:
    """Function returns a list of existing olympic games years to check whether year given by user is valid."""
    olympic_games_years = []
    with sqlite3.connect('olympic_history.db') as conn:
        cursor = conn.cursor()
        game_years_raw = cursor.execute('select year from games').fetchall()
    for year_tuple in game_years_raw:
        olympic_games_years.append(str(year_tuple[0]))

    return olympic_games_years


def query_db(input_data: dict) -> list:
    """Depending on keys in the input data dict, queries db for needed info and returns a list."""
    connection = sqlite3.connect('olympic_history.db')
    cursor = connection.cursor()

    if input_data['chart'] == 'medals':

        if 'medal' in input_data.keys():
            result = cursor.execute('''select g.year, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and t.noc_name = ?
            and g.season = ?
            and r.medal = ?
            group by g.year
            order by g.year''',  (input_data.get('noc'), input_data.get('season'), input_data.get('season'))).fetchall()

        else:
            result = cursor.execute('''select g.year, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and t.noc_name = ?
            and g.season = ?
            group by g.year
            order by g.year''', (input_data.get('noc'), input_data.get('season'))).fetchall()

    elif input_data['chart'] == 'top-teams':

        if 'year' in input_data.keys() and 'medal'not in input_data.keys():

            result = cursor.execute('''select t.noc_name, count(r.medal) medals
        from teams t, results r, athletes a, games g
        where r.athlete_id = a.id
        and a.team_id = t.id
        and g.id = r.game_id
        and g.season = ?
        and g.year = ?
        group by t.noc_name
        order by medals desc''', (input_data.get('season'), input_data.get('year')))

        if 'year' not in input_data.keys() and 'medal' in input_data.keys():

            result = cursor.execute('''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = ?
            and r.medal = ?
            group by t.noc_name
            order by medals desc''', (input_data.get('season'), input_data.get('medal'))).fetchall()

        elif 'year' and 'medal' in input_data.keys():
            result = cursor.execute('''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = ?
            and r.medal = ?
            and g.year = ?
            group by t.noc_name
            order by medals desc''', (input_data.get('season'), input_data.get('medal'), input_data.get('year'))).fetchall()

        else:
            result = cursor.execute('''select t.noc_name, count(r.medal) medals
            from teams t, results r, athletes a, games g
            where r.athlete_id = a.id
            and a.team_id = t.id
            and g.id = r.game_id
            and g.season = ?
            group by t.noc_name
            order by medals desc''', (input_data.get('season'),)).fetchall()

    connection.close()

    return result


def truncate_db_tables() -> None:
    """Truncates all tables in the olympic_history.db"""
    with sqlite3.connect('olympic_history.db') as conn:
        cursor = conn.cursor()
        cursor.executescript("""
            delete from teams;
            delete from games;
            delete from events;
            delete from sports;
            delete from athletes;
            delete from results;
        """)
