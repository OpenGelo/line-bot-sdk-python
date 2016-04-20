# -*- coding: utf-8 -*-

from linebot.builders import MultipleMessage


class TestMultipleMessage():
    def test_instance_creation(self, fx_client):
        multiple_message = MultipleMessage(fx_client)
        assert isinstance(multiple_message, MultipleMessage)

    def test_add_text(self, fx_multiple_message):
        multiple_message = fx_multiple_message.add_text(text='')
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
