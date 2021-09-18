import pytest
from helpers.ResponseHandler import get_formatted_response


class TestGetConversations:
    @pytest.mark.parametrize('date_start, date_end, page_size, record_index, order, expected_response_status_code, '
                             'expected_number_of_conversations'
                             [
                                 ['2000-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200, ],
                                 ['2019-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200],
                                 ['2019-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200],
                                 ['2019-11-28T17:41:12+0200', '2019-11-29T17:41:12+0200', 10, 0, 'ASC', 200],
                             ])
    def test_get_conversation_list_by_dates(self, get_conversations, date_start, date_end, page_size, record_index,
                                            order, expected_response_status_code, expected_number_of_conversations):
        conversations_list_response_obj = get_conversations
        formatted_conversations_list = get_formatted_response(conversations_list_response_obj)
        conversations_count = formatted_conversations_list['count']
        assert conversations_list_response_obj.status_code == expected_response_status_code
        assert conversations_count == expected_number_of_conversations