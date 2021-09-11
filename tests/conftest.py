import pytest

from models.Conversation import Conversation


@pytest.fixture
def get_conversations_object():
    conversations_list = Conversation().get_conversation_list()
    return conversations_list


@pytest.fixture
def get_new_conversation(name, display_name, image_url, ttl):
    conversation = Conversation().create_conversation(name=name, display_name=display_name,
                                                      image_url=image_url, ttl=ttl)
    return conversation


@pytest.fixture
def get_updated_conversation(conversation_id, name, display_name, image_url, ttl):
    updated_conversation = Conversation().update_conversation(conversation_id=conversation_id, name=name,
                                                              display_name=display_name, image_url=image_url, ttl=ttl)
    return updated_conversation
