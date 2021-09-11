import requests
from config import config
from models.helpers.Headers import get_header


class Conversation:

    def __init__(self):
        self.base_url = config.api_url
        self.token = config.JWT

    def get_conversation_list(self):
        url = "{}/v0.1/conversations".format(self.base_url)
        header = get_header(self.token)
        response = requests.get(url, headers=header)
        return response

