import datetime

import pytest
from helpers.ResponseHandler import get_formatted_response
from models.Conversation import Conversation


class TestGetConversations:

    @pytest.mark.parametrize('date_start, date_end, page_size, record_index, order, expected_response_status_code, '
                             'expected_number_of_conversations',
                             [
                                 ['2000-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200, 0]
                             ])
    def test_get_conversation_list_by_dates(self, get_conversations, date_start, date_end, page_size, record_index,
                                            order, expected_response_status_code, expected_number_of_conversations):
        conversations_list_response_obj = get_conversations
        formatted_conversations_list = get_formatted_response(conversations_list_response_obj)
        conversations_count = formatted_conversations_list['count']
        assert conversations_list_response_obj.status_code == expected_response_status_code
        assert conversations_count == expected_number_of_conversations


class TestsCreateConversation:
    conv_name = 'conv-{}'.format(datetime.datetime.now())

    @pytest.mark.parametrize('name, display_name, image_url, ttl, expected_response_status_code, expected_name',
                             [
                                 [conv_name, 'disp name', "https://demo.img", 3600, 200, conv_name]
                             ])
    def test_create_conversation(self, get_new_conversation, name, display_name, image_url, ttl,
                                 expected_response_status_code, expected_name):
        conversation_response_obj = get_new_conversation
        conversation_id = get_formatted_response(conversation_response_obj)['id']
        conversation_object = Conversation().get_conversation_by_id(conversation_id)
        conversation_name = get_formatted_response(conversation_object)['name']
        assert conversation_response_obj.status_code == expected_response_status_code
        assert conversation_name == expected_name


