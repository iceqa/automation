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

    def create_conversation(self, name: str, display_name: str, image_url: str, conv_prop_time_exist: int):
        url = "{}/v0.1/conversations".format(self.base_url)
        header = get_header(self.token)
        data = {
            "name": name,
            "display_name": display_name,
            "image_url": image_url,  # https://example.com/image.png
            "properties": {
                "ttl": conv_prop_time_exist
            }
        }
        response = requests.post(url, json=data, headers=header)
        return response

    def update_conversation(self, conversation_id: str, name: str, display_name: str, image_url: str,
                            conv_prop_time_exist: int):
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        data = {
            "name": name,
            "display_name": display_name,
            "image_url": image_url,  # https://example.com/image.png
            "properties": {
                "ttl": conv_prop_time_exist
            }
        }
        response = requests.put(url, json=data, headers=header)
        return response

    def get_conversation_by_id(self, conversation_id: str):
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        response = requests.get(url, headers=header)
        return response

    def delete_conversation(self, conversation_id: str):
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        response = requests.delete(url, headers=header)
        return response

    def record_conversation(self, conversation_id: str, event_url: str, event_method: str, split: str, audio_format: str):
        url = "{}/v0.1/conversations/{}/record".format(self.base_url, conversation_id)
        header = get_header(self.token)
        data = {
            "action": "start",
            "event_url": [
                event_url
            ],
            "event_method": event_method,
            "split": split,
            "format": audio_format
        }
        response = requests.delete(url, json=data, headers=header)
        return response
