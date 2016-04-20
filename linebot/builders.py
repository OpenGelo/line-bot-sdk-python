# -*- coding: utf-8 -*-


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
