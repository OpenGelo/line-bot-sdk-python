# -*- coding: utf-8 -*-

from linebot.receives import Receive


class TestReceive():
    def test_instance_creation(self, fx_json_request_content_text):
        receive = Receive(fx_json_request_content_text)
        assert isinstance(receive, Receive)
