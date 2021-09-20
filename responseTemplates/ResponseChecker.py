from trafaret.constructor import construct


def validate_json_response(schema, val):
    try:
        validator = construct(schema)
        validator(val)
        return True
    except Exception as e:
        raise e
