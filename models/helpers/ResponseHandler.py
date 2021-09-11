

def get_formatted_response(response):
    formatted_response = response.json()
    return formatted_response


def get_token(response):
    return response.json()['token']


def get_response_code(response):
    return response.status_code


def get_error_validation_message(response):
    return get_formatted_response(response)[0]['message']


def get_data_from_response(response):
    for element in response:
        return element
