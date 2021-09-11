"""conversation model with API to conversation entity."""
import requests
from config import config
from helpers.Headers import get_header


class Conversation:
    """Conversation entity methods to work with it's API."""
    def __init__(self):
        self.base_url = config.API_URL
        self.token = config.JWT

    def get_conversation_list(self):
        """function to get all conversations."""
        url = "{}/v0.1/conversations".format(self.base_url)
        header = get_header(self.token)
        response = requests.get(url, headers=header)
        return response

    def create_conversation(self, name: str, display_name: str, image_url: str, ttl: int):
        """function to create a conversations with specifying:
             @name (str) - Unique name for a conversation
             @display name (str) - The display name for the conversation. It does not have to be unique
             @url to image (str) - A link to an image for conversations' and users' avatars
             @properties (object) - Conversation properties
             @ttl (number) - Time to leave. After how many seconds an empty conversation is deleted."""
        url = "{}/v0.1/conversations".format(self.base_url)
        header = get_header(self.token)
        data = {
            "name": name,
            "display_name": display_name,
            "image_url": image_url,  # https://example.com/image.png
            "properties": {
                "ttl": ttl
            }
        }
        response = requests.post(url, json=data, headers=header)
        return response

    def update_conversation(self, conversation_id: str, name: str, display_name: str, image_url: str,
                            ttl: int):
        """function to update a conversations with specifying:
            @name (str) - Unique name for a conversation
            @display name (str) - The display name for the conversation. It does not have to be unique
            @url to image (str) - A link to an image for conversations' and users' avatars
            @properties (object) - Conversation properties
            @ttl (number) - Time to leave. After how many seconds an empty conversation is deleted."""
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        data = {
            "name": name,
            "display_name": display_name,
            "image_url": image_url,  # https://example.com/image.png
            "properties": {
                "ttl": ttl
            }
        }
        response = requests.put(url, json=data, headers=header)
        return response

    def get_conversation_by_id(self, conversation_id: str):
        """function to get a conversation by id."""
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        response = requests.get(url, headers=header)
        return response

    def delete_conversation(self, conversation_id: str):
        """function to delete a ccoonversation by id."""
        url = "{}/v0.1/conversations/{}".format(self.base_url, conversation_id)
        header = get_header(self.token)
        response = requests.delete(url, headers=header)
        return response

    def record_conversation(self, conversation_id: str, event_url: str, event_method: str, split: str,
                            audio_format: str):
        """function to record a conversation."""
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
