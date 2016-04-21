# -*- coding: utf-8 -*-

from linebot.constants import ContentType


class MessageBase(object):
    def __init__(self, **attrs):
        self.__attrs = attrs
        self.__content = self._create_content()

    def __getitem__(self, key):
        return self.__content[key]

    @property
    def attrs(self):
        return self.__attrs

    @property
    def content(self):
        return self.__content

    @property
    def event_type(self):
        return '138311608800106203'

    def _create_content(self):
        raise NotImplementedError

    def is_valid(self):
        raise NotImplementedError


class TextMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': ContentType.TEXT.value,
            'toType': 1,  # 1 => user
            'text': self.attrs['text'],
        }

    def is_valid(self):
        return self.attrs['text'] is not None


class ImageMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': ContentType.IMAGE.value,
            'toType': 1,  # 1 => user
            'originalContentUrl': self.attrs['image_url'],
            'previewImageUrl': self.attrs['preview_url'],
        }

    def is_valid(self):
        return self.attrs['image_url'] and self.attrs['preview_url']


class VideoMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': ContentType.VIDEO.value,
            'toType': 1,  # 1 => user
            'originalContentUrl': self.attrs['video_url'],
            'previewImageUrl': self.attrs['preview_url'],
        }

    def is_valid(self):
        return self.attrs['video_url'] and self.attrs['preview_url']


class AudioMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': ContentType.AUDIO.value,
            'toType': 1,  # 1 => user
            'originalContentUrl': self.attrs['audio_url'],
            'contentMetadata': {
                'AUDLEN': str(self.attrs['duration']),
            },
        }

    def is_valid(self):
        return self.attrs['audio_url'] and self.attrs['duration']


class LocationMessage(MessageBase):
    def _create_content(self):
        address = self.attrs.get('address')
        return {
            'contentType': ContentType.LOCATION.value,
            'toType': 1,  # 1 => user
            'text': address or self.attrs['title'],
            'location': {
                'title': self.attrs['title'],
                'address': address,
                'latitude': self.attrs['latitude'],
                'longitude': self.attrs['longitude'],
            },
        }

    def is_valid(self):
        return self.attrs['title'] and self.attrs['latitude'] and self.attrs['longitude']


class StickerMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': ContentType.STICKER.value,
            'toType': 1,  # 1 => user
            'contentMetadata': {
                'STKPKGID': str(self.attrs['stkpkgid']),
                'STKID': str(self.attrs['stkid']),
                'STKVER': str(self.attrs['stkver']),
            },
        }

    def is_valid(self):
        return self.attrs['stkpkgid'] and self.attrs['stkid'] and self.attrs['stkver']
