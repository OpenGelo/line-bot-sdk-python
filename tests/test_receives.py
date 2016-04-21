# -*- coding: utf-8 -*-

from linebot import messages
from linebot import operations
from linebot.receives import Receive


class TestReceive():
    def test_instance_creation_text_message(self, fx_json_request_content_text):
        receive = Receive(fx_json_request_content_text)
        assert isinstance(receive, Receive)
        receive = receive[0]
        assert receive['id']
        assert receive['from_mid']
        assert receive['to_mid']
        assert receive['from_channel_id']
        assert receive['to_channel_id']
        assert receive['event_type']
        assert receive['created_time']
        content = receive['content']
        assert isinstance(content, messages.TextMessage)
        assert content['contentType'] == 1
        assert content['text'] == 'hello'
        assert content['toType'] == 1


class TestReceiveOperation():
    def test_receive_operation(self, fx_json_request_content_operation):
        receive = Receive(fx_json_request_content_operation)
        assert isinstance(receive, Receive)
        receive = receive[0]
        assert receive['id']
        assert receive['from_mid']
        assert receive['to_mid']
        assert receive['from_channel_id']
        assert receive['to_channel_id']
        assert receive['event_type']
        content = receive['content']
        assert isinstance(content, operations.AddedAsFriend)
        assert content['revision']
        assert content['op_type']
        assert content['params']
