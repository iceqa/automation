import pytest

from helpers.DataGenerators import get_str_with_length, get_current_time_without_tzinfo
from helpers.ResponseHandler import get_formatted_response
from models.Conversation import Conversation


class TestGetConversations:

    @pytest.mark.parametrize('date_start, date_end, page_size, record_index, order, expected_response_status_code, '
                             'expected_number_of_conversations',
                             [
                                 ['2000-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200, 0]
                             ])
    def test_get_count_conversation_by_dates(self, get_conversations, date_start, date_end, page_size, record_index,
                                             order, expected_response_status_code, expected_number_of_conversations):
        conversations_list_response_obj = get_conversations
        formatted_conversations_list = get_formatted_response(conversations_list_response_obj)
        conversations_count = formatted_conversations_list['count']
        assert conversations_list_response_obj.status_code == expected_response_status_code
        assert conversations_count == expected_number_of_conversations


class TestsCreateConversation:

    @pytest.mark.parametrize('name, display_name, image_url, ttl, expected_response_status_code',
                             [
                                 ['conv-{}'.format(get_current_time_without_tzinfo()), "happy pass case", "https://demo.img",
                                  60, 200],
                                 ["some super conversation", "dp-{}".format(get_current_time_without_tzinfo()), "https://demo.img",
                                  60, 200],
                                 ["{}".format(get_str_with_length(255)), "disp name3", "https://demo.img",
                                  10, 200],
                                 ["conv with google link", "gogole disp name", "https://google.com", 60, 200],
                                 ["conv with http link", "http disp name", "http://google.com", 60, 200],
                                 ["conv with big ttl", "bit ttl disp name", "https://google.com", 86400, 200],
                                 ["name-long1", "dn-{}".format(get_str_with_length(255)), "https://demo.img",
                                  10, 200],
                                 ["name-{}".format(get_str_with_length(255)), "disp name3", "https://demo.img",
                                  10, 200],

                             ])
    def test_create_conversation_with_positive_values_and_check_status_code(self, get_new_conversation, name,
                                                                            display_name, image_url, ttl,
                                                                            expected_response_status_code):
        conversation_response_obj = get_new_conversation
        assert conversation_response_obj.status_code == expected_response_status_code, "POSITIVE - create " \
                                                                                       "conversation response " \
                                                                                       "status code mismatches"

    conv_name_with_current_date = 'conv-{}'.format(get_current_time_without_tzinfo())

    @pytest.mark.parametrize('name, display_name, image_url, ttl, expected_response_status_code',
                             [
                                 [conv_name_with_current_date, "conv-name negative case", "https://demo.img",
                                  60, 200],
                                 [conv_name_with_current_date, "conv-name negative case", "https://demo.img",
                                  60, 400],
                                 ["name-{}".format(get_str_with_length(5000)), "disp name3", "https://demo.img",
                                  10, 413],
                                 ["name-long1", "dn-{}".format(get_str_with_length(4000)), "https://demo.img",
                                  10, 413],
                                 [{}, "gogole disp name", "https://google.com", 10, 400],
                                 ["conv with http link", "", "http://google.com", 10, 400],
                                 ["conv with big ttl", "bit ttl disp name", {}, 1, 400],
                                 ["conv with big ttl", "bit ttl disp name", "http://google.com", "", 400],
                                 ["", "", "", {}, 400],
                                 [{}, {}, {}, {}, 400],
                                 ["", "", "", "", 400]
                             ])
    def test_create_conversation_with_negative_values_and_check_status_code(self, get_new_conversation, name,
                                                                            display_name, image_url, ttl,
                                                                            expected_response_status_code):
        conversation_response_obj = get_new_conversation
        assert conversation_response_obj.status_code == expected_response_status_code, "NEGATIVE - create " \
                                                                                       "conversation response status " \
                                                                                       "code mismatches"

    current_time = get_current_time_without_tzinfo()[:16]
    conv_name = 'conv-{}'.format(current_time)

    @pytest.mark.parametrize('name, display_name, image_url, ttl, expected_response_status_code, expected_name, '
                             'expected_creation_date',
                             [
                                 [conv_name, "disp name", "https://demo.img", 3600, 200,
                                  conv_name, current_time]
                             ])
    def test_create_conversation_and_verify_data(self, get_new_conversation, name, display_name, image_url, ttl,
                                                 expected_response_status_code, expected_name, expected_creation_date):
        conversation_response_obj = get_new_conversation
        conversation_id = get_formatted_response(conversation_response_obj)['id']
        conversation_object = Conversation().get_conversation_by_id(conversation_id)
        conversation_json = get_formatted_response(conversation_object)
        conversation_name = conversation_json['name']
        conversation_display_name = conversation_json['display_name']
        conversation_created_date = (conversation_json['timestamp']['created'])[:16]
        assert conversation_response_obj.status_code == expected_response_status_code, "Wrong status code"
        assert conversation_name == expected_name, "conversation name mismatch to input"
        assert conversation_display_name == display_name, "display name mismatch to input"
        assert conversation_created_date == expected_creation_date, "conversation create date mismatch"

    @pytest.mark.parametrize('name, display_name, image_url, ttl, expected_response_status_code, expected_name',
                             [
                                 ['conv-{}'.format(get_current_time_without_tzinfo()), 'disp name', "https://demo.img", 3600, 200,
                                  'conv-{}'.format(get_current_time_without_tzinfo())]
                             ])
    def test_create_conversation(self, get_new_conversation, name, display_name, image_url, ttl,
                                 expected_response_status_code, expected_name):
        conversation_response_obj = get_new_conversation
        conversation_id = get_formatted_response(conversation_response_obj)['id']
        conversation_object = Conversation().get_conversation_by_id(conversation_id)
        conversation_name = get_formatted_response(conversation_object)['name']
        assert conversation_response_obj.status_code == expected_response_status_code
        assert conversation_name == expected_name
