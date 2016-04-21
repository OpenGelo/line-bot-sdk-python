# -*- coding: utf-8 -*-

from linebot.receives import Receive


class TestReceive():
    def test_instance_creation_text_message(self, fx_json_request_content_text):
        receive = Receive(fx_json_request_content_text)
        assert isinstance(receive, Receive)
        assert receive[0]['id']
        assert receive[0]['from_mid']
        assert receive[0]['to_mid']
        assert receive[0]['from_channel_id']
        assert receive[0]['to_channel_id']
        assert receive[0]['event_type']
        assert receive[0]['created_time']
        assert receive[0]['content'] == {
            'contentType': 1,
            'text': 'hello',
            'toType': 1,
        }
