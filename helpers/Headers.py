"""helper to work with Request Header"""


def get_header(token):
    """returns a key: value row and adds to header part of the request."""
    headers = {}
    if token:
        headers['Authorization'] = 'Bearer {}'.format(token)
    return headers
