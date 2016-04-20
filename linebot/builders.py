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

    def is_valid(self):
        return len(self.__messages) > 0

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

    def add_image(self, **attrs):
        message = messages.ImageMessage(
            image_url=attrs['image_url'],
            preview_url=attrs['preview_url'],
        )
        return self.push_message(message)

    def add_video(self, **attrs):
        message = messages.VideoMessage(
            video_url=attrs['video_url'],
            preview_url=attrs['preview_url'],
        )
        return self.push_message(message)

    def add_audio(self, **attrs):
        message = messages.AudioMessage(
            audio_url=attrs['audio_url'],
            duration=attrs['duration'],
        )
        return self.push_message(message)

    def add_location(self, **attrs):
        message = messages.LocationMessage(
            title=attrs['title'],
            latitude=attrs['latitude'],
            longitude=attrs['longitude'],
        )
        return self.push_message(message)

    def add_sticker(self, **attrs):
        message = messages.StickerMessage(
            stkpkgid=attrs['stkpkgid'],
            stkid=attrs['stkid'],
            stkver=attrs['stkver'],
        )
        return self.push_message(message)


class RichMessage():
    def __init__(self, client):
        self.__client = client

    @property
    def event_type(self):
        return '138311608800106203'
