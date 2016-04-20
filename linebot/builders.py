# -*- coding: utf-8 -*-

from linebot import messages


class MultipleMessage():
    def __init__(self, client):
        self.messages = []
        self.client = client

    @property
    def content(self):
        return {
            'messageNotified': 0,
            'messages': self.messages,
        }

    @property
    def event_type(self):
        return '140177271400161403'

    def push_message(self, message):
        if not message.is_valid():
            raise ValueError('Invalid value')
        self.messages.append(message)
        return self

    def add_text(self, **attrs):
        message = messages.TextMessage(text=attrs['text'])
        return self.push_message(message)
