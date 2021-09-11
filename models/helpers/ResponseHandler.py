"""module to work with Request Response object."""


def get_formatted_response(response):
    """return the response object into readable json data."""
    formatted_response = response.json()
    return formatted_response


def get_token(response):
    return response.json()['token']


def get_response_code(response):
    """:returns status code number from the request"""
    return response.status_code


def get_error_validation_message(response):
    return get_formatted_response(response)[0]['message']


def get_data_from_response(response):
    """runs through the response object and gets the value of specified key."""
    for element in response:
        return element
