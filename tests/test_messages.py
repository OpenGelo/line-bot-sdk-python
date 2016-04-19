# -*- coding: utf-8 -*-

from linebot import messages


class TestMessages():
    def test_text_message(self):
        messages.TextMessage(text='')
