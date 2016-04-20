# -*- coding: utf-8 -*-

from linebot import messages


class MultipleMessage():
    def __init__(self, client):
        self.__messages = []
        self.__client = client

    @property
    def content(self):
        return {
            'messageNotified': 0,
            'messages': self.__messages,
        }

    @property
    def event_type(self):
        return '140177271400161403'

    def send(self, to_mid):
        return self.__client.send_message(to_mid, self)

    def push_message(self, message):
        if not message.is_valid():
            raise ValueError('Invalid value')
        self.__messages.append(message.content)
        return self

    def add_text(self, **attrs):
        message = messages.TextMessage(text=attrs['text'])
        return self.push_message(message)
