import sqlite3


def insert_to_db(teams, games, events, sports, athletes, results):
    conn = sqlite3.connect('olympic_history.db')
    cursor = conn.cursor()

    # Inserting teams
    for k, v in teams.items():
        team_id = v['id']
        name = v['name']
        noc_name = v['noc_name']
        cursor.execute("INSERT INTO TEAMS(ID, NAME, NOC_NAME) VALUES (?, ?, ?)", (team_id, name, noc_name))
    conn.commit()

    # Inserting games
    for key, value in games.items():
        g_id = value['id']
        game_year = value['game_year']
        season = value['season']
        city = value['city']
        cursor.execute("INSERT INTO GAMES(ID, YEAR, SEASON, CITY) VALUES(?, ?, ?, ?)", (g_id, game_year, season, city))
    conn.commit()

    # Inserting events
    for v in events.values():
        event_id = v['id']
        event_name = v['event_name']
        cursor.execute("INSERT INTO EVENTS(ID, NAME) VALUES (?, ?)", (event_id, event_name))
    conn.commit()

    # Inserting sports
    for value in sports.values():
        sport_id = value['id']
        sport_name = value['name']
        cursor.execute("INSERT INTO SPORTS(ID, NAME) VALUES (?, ?)", (sport_id, sport_name))
    conn.commit()

    # Inserting athletes
    for k, v in athletes.items():
        name = v['full_name']
        sex = v['sex']
        params = v['params']
        team_id = v['team_id']
        year_of_birth = v['year_of_birth']
        athlete_id = v['id']
        cursor.execute("INSERT INTO ATHLETES(ID, FULL_NAME, YEAR_OF_BIRTH, SEX, PARAMS, TEAM_ID) VALUES (?, ?, ?, ?, ?, ?)",
                       (athlete_id, name, year_of_birth, sex, str(params), team_id))
    conn.commit()

    # Inserting results
    for result in results:
        athlete_id = result['athlete_id']
        game_id = result['game_id']
        sport_id = result['sport_id']
        event_id = result['event_id']
        medal = result['medal']
        cursor.execute("insert into results(athlete_id, game_id, sport_id, event_id, medal) values(?, ?, ?, ?, ?)",
                       (athlete_id, game_id, sport_id, event_id, medal))

    conn.commit()
    conn.close()
