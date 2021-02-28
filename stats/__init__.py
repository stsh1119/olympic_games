from .utils import parse_input, validate_mandatory_parameters, build_chart
from .db import query_db


def stats():
    """"Combines other functions to:
    1. Get and validate CLI input
    2. Check, that mandatory parameters weren't skipped
    3. Query database, using previously validated data
    4. Build charts
    """
    input_data = parse_input()
    validated_dict = validate_mandatory_parameters(input_data)
    db_data = query_db(validated_dict)
    build_chart(db_data, validated_dict)
