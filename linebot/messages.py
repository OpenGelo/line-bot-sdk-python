# -*- coding: utf-8 -*-


class MessageBase(object):
    def __init__(self, **attrs):
        self._attrs = attrs
        self.content = self._create_content()

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
            'contentType': 1,  # Fixed value
            'toType': 1,  # 1 => user
            'text': self._attrs['text'],
        }

    def is_valid(self):
        return self._attrs['text'] is not None


class ImageMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': 2,  # Fixed value
            'toType': 1,  # 1 => user
            'originalContentUrl': self._attrs['image_url'],
            'previewImageUrl': self._attrs['preview_url'],
        }

    def is_valid(self):
        return self._attrs['image_url'] and self._attrs['preview_url']


class VideoMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': 3,  # Fixed value
            'toType': 1,  # 1 => user
            'originalContentUrl': self._attrs['video_url'],
            'previewImageUrl': self._attrs['preview_url'],
        }

    def is_valid(self):
        return self._attrs['video_url'] and self._attrs['preview_url']


class AudioMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': 4,  # Fixed value
            'toType': 1,  # 1 => user
            'originalContentUrl': self._attrs['audio_url'],
            'contentMetadata': {
                'AUDLEN': str(self._attrs['duration']),
            },
        }

    def is_valid(self):
        return self._attrs['audio_url'] and self._attrs['duration']


class LocationMessage(MessageBase):
    def _create_content(self):
        address = self._attrs.get('address')
        return {
            'contentType': 7,  # Fixed value
            'toType': 1,  # 1 => user
            'text': address or self._attrs['title'],
            'location': {
                'title': self._attrs['title'],
                'address': address,
                'latitude': self._attrs['latitude'],
                'longitude': self._attrs['longitude'],
            },
        }

    def is_valid(self):
        return self._attrs['title'] and self._attrs['latitude'] and self._attrs['longitude']


class StickerMessage(MessageBase):
    def _create_content(self):
        return {
            'contentType': 8,  # Fixed value
            'toType': 1,  # 1 => user
            'contentMetadata': {
                'STKPKGID': str(self._attrs['stkpkgid']),
                'STKID': str(self._attrs['stkid']),
                'STKVER': str(self._attrs['stkver']),
            },
        }

    def is_valid(self):
        return self._attrs['stkpkgid'] and self._attrs['stkid'] and self._attrs['stkver']
