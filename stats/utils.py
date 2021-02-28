from operator import itemgetter
import sys
from .db import get_noc_names, get_game_years


def parse_input() -> dict:
    """Takes user input, validates each parameter and returns a dict."""
    result = {}
    seasons = ['winter', 'summer']
    medals = ['gold', 'silver', 'bronze']
    chart_types = ['medals', 'top-teams']

    noc_names = get_noc_names()
    game_years = get_game_years()

    try:
        chart_type = sys.argv[1]
        if chart_type in chart_types:
            result['chart'] = chart_type
        else:
            print('No such chart, try: medals or top-teams')
            sys.exit()
    except IndexError:
        print('No chart type given')
        sys.exit()

    try:
        user_input = sys.argv[2:]
    except IndexError:
        print('No argument given')

    for input_element in user_input:
        if input_element.lower() in seasons:
            result['season'] = convert_season(input_element.lower())
        if input_element.lower() in medals:
            result['medal'] = convert_medal(input_element.lower())
        if input_element.upper() in noc_names:
            result['noc'] = input_element.upper()
        if input_element in game_years:
            result['year'] = input_element
    return result


def validate_mandatory_parameters(dict_user_input: dict) -> dict:
    """Depending on chart type, checks mandatory parameters, returns error in case such parameters is ommited."""
    if dict_user_input['chart'] == 'medals':
        if 'season' not in dict_user_input.keys():
            print('Season is mandatory parameter')
            sys.exit()
        if 'noc' not in dict_user_input.keys():
            print('NOC is mandatory parameter')
            sys.exit()
    elif dict_user_input['chart'] == 'top-teams':
        if 'season' not in dict_user_input.keys():
            print('Season is mandatory parameter')
            sys.exit()

    return dict_user_input


def convert_medal(input_medal: str) -> int:
    """Function that mapps medal string value for an corresponding int value, will return None if medal doesn't exist."""
    medals = {
        'gold': 1,
        'silver': 2,
        'bronze': 3,
    }
    medal = medals.get(input_medal, None)
    return medal


def convert_season(input_season: str) -> int:
    """Function that mapps season string value for an corresponding int value, will return None if medal doesn't exist."""
    seasons = {
        'winter': 1,
        'summer': 0,
    }
    season = seasons.get(input_season, None)
    return season


def build_chart(data, validated_data_dict):
    """Prints needed headers depending on 'chart' key in validated_data_dict,
       Builds charts using data, obtained from db using parameters from validated_data_dict.
    """
    symbol = '█'
    if validated_data_dict['chart'] == 'medals':
        print('YEAR AMOUNT')

    elif validated_data_dict['chart'] == 'top-teams':
        print('NOC AMOUNT')

    # * Uses index(1) of each tuple in the list as a key to sort elements so that, the 1st one is the largest
    results = sorted(data, key=itemgetter(1), reverse=True)

    highest = results[0][1]
    k = 200/highest
    for result in data:
        left_column = result[0]
        length = float(result[1])
        symbol_lenght = int(k * length) * symbol
        print(f'{left_column} {symbol_lenght}')
