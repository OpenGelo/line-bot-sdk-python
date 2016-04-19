# -*- coding: utf-8 -*-

from linebot import messages


class TestMessages():
    def test_text_message(self):
        test_text = 'TEST TEXT MESSAGE'
        message = messages.TextMessage(text=test_text)
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 1,
            'toType': 1,
            'text': test_text,
        }
