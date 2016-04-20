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

    def send_image(self, **attrs):
        message = messages.ImageMessage(
            image_url=attrs['image_url'],
            preview_url=attrs['preview_url'],
        )
        return self.send_message(attrs['to_mid'], message)

    def send_video(self, **attrs):
        message = messages.VideoMessage(
            video_url=attrs['video_url'],
            preview_url=attrs['preview_url'],
        )
        return self.send_message(attrs['to_mid'], message)

    def send_audio(self, **attrs):
        message = messages.AudioMessage(
            audio_url=attrs['audio_url'],
            duration=attrs['duration'],
        )
        return self.send_message(attrs['to_mid'], message)
