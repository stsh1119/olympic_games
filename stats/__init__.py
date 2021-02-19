from .parse_input import parse_input
from stats.utils import validate_input, get_from_db, build_chart


def stats():
    input_data = parse_input()
    data = validate_input(input_data)
    query_result = get_from_db(data)
    build_chart(query_result, data)
