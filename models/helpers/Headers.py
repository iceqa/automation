"""helper to work with Request Header"""


def get_header(token):
    headers = {}
    if token:
        headers['Authorization'] = 'Bearer {}'.format(token)
    return headers
