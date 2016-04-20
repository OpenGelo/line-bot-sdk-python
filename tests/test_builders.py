# -*- coding: utf-8 -*-

from linebot.builders import MultipleMessage


class TestMultipleMessage():
    def test_instance_creation(self, fx_client):
        multiple_message = MultipleMessage(fx_client)
        assert isinstance(multiple_message, MultipleMessage)
