# -*- coding: utf-8 -*-

import json

from linebot import messages
from linebot.constants import ContentType


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
        self.__actions = {}
        self.__listeners = []
        self.__client = client

    @property
    def event_type(self):
        return '138311608800106203'

    @property
    def content(self):
        return {
            'contentType': ContentType.RICH_MESSAGE.value,
            'toType': 1,  # 1 => user
            'contentMetadata': {
                'DOWNLOAD_URL': self.__image_url,
                'SPEC_REV': 1,  # Fixed value
                'ALT_TEXT': self.__alt_text,
                'MARKUP_JSON': self.__create_markup_json(),
            },
        }

    def send(self, **attrs):
        self.__image_url = attrs['image_url']
        self.__alt_text = attrs['alt_text']
        return self.__client.send_message(attrs['to_mid'], self)

    def __create_markup_json(self):
        height = self.__determine_height()
        return json.dumps({
            'canvas': {
                'height': height,
                'width': 1040,  # Fixed value
                'initialScene': 'scene1',  # Fixed value
            },
            'images': {
                'image1': {
                    'x': 0,  # Fixed value
                    'y': 0,  # Fixed value
                    'w': 1040,  # Fixed value
                    'h': height,
                },
            },
            'actions': self.__actions,
            'scenes': {
                'scene1': {
                    'draws': [
                        {
                            'image': 'image1',
                            'x': 0,  # Fixed value
                            'y': 0,  # Fixed value
                            'w': 1040,  # This value must be same as the image width
                            'h': height
                        },
                    ],
                    'listeners': self.__listeners,
                },
            },
        })

    def __determine_height(self):
        height = 0
        for listener in self.__listeners:
            h = listener['params'][1] + listener['params'][3]  # params.y + params.height
            if height < h:
                height = h
        return 2080 if height > 2080 else height

    def set_action(self, **attrs):
        for key, value in attrs.items():
            self.__validate_action_attributes(value)
            self.__actions[str(key)] = {
                'type': value.get('type') or 'web',
                'text': str(value['text']),
                'params': {
                    'linkUri': str(value['link_url']),
                },
            }
        return self

    def __validate_action_attributes(self, attrs):
        if not (attrs['text'] and attrs['link_url']):
            raise ValueError('Invalid arguments, :text, :link_url keys.')

    def add_listener(self, **attrs):
        self.__validate_listener_attributes(attrs)
        listener = {
            'type': 'touch',  # Fixed value
            'params': [attrs['x'], attrs['y'], attrs['width'], attrs['height']],
            'action': attrs['action'],
        }
        self.__listeners.append(listener)
        return self

    def __validate_listener_attributes(self, attrs):
        if not (
            isinstance(attrs['action'], str) and
            isinstance(attrs['x'], int) and
            isinstance(attrs['y'], int) and
            isinstance(attrs['width'], int) and
            isinstance(attrs['height'], int)
        ):
            raise ValueError('Invalid arguments, :x [Fixnum], :y [Fixnum], :width [Fixnum], :height [Fixnum] keys.')
