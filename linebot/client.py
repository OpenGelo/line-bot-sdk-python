# -*- coding: utf-8 -*-

from linebot import constants
from linebot import messages
from linebot.requests import Request


class LineBotClient():
    def __init__(self, **credentials):
        self.credentials = {
            'X-Line-ChannelID': credentials['channel_id'],
            'X-Line-ChannelSecret': credentials['channel_secret'],
            'X-Line-Trusted-User-With-ACL': credentials['channel_mid'],
        }

    def send_message(self, to_mid, message):
        request = Request(**{
            'url': constants.API_URL_EVENTS,
            'credentials': self.credentials,
            'to_mid': to_mid,
            'message': message,
        })
        request.validate()
        return request.post()

    def send_text(self, **attrs):
        message = messages.TextMessage(text=attrs['text'])
        return self.send_message(attrs['to_mid'], message)
