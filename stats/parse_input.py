import sys
from stats.utils import convert_season, convert_medal, get_years_from_db, prettify_year, get_noc_from_db, prettify_noc


def parse_input():

    result = {}

    seasons = ['winter', 'summer']
    medals = ['gold', 'silver', 'bronze']
    chart_types = ['medals', 'top-teams']

    noc_names_raw = get_noc_from_db()
    noc_names = prettify_noc(noc_names_raw)

    game_years_raw = get_years_from_db()
    game_years = prettify_year(game_years_raw)

    current_noc = None
    current_season = None
    current_medal = None
    current_year = None

    try:
        chart_type = sys.argv[1]
        if chart_type in chart_types:
            result['chart'] = chart_type
        else:
            print('No such chart, try: medals or top-teams')
            sys.exit()
    except IndexError:
        print('No argument given')
        sys.exit()
    try:
        data = sys.argv[2:]
    except IndexError:
        print('No argument given')

    for elem in data:
        if elem.lower() in seasons:
            current_season = convert_season(elem.lower())
            result['season'] = current_season
        if elem.lower() in medals:
            current_medal = convert_medal(elem.lower())
            result['medal'] = current_medal
        if elem.upper() in noc_names:
            current_noc = elem.upper()
            result['noc'] = current_noc

        if elem in game_years:
            current_year = elem
            result['year'] = current_year

    return result
