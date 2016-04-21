# -*- coding: utf-8 -*-

import json

from linebot import messages
from linebot.constants import ContentType, ReceiveEventType


class Receive():
    def __init__(self, content_json):
        parsed_json = json.loads(content_json)
        result = parsed_json['result']
        self.__data = [self.__generate_data(datum) for datum in result]

    def __getitem__(self, index):
        return self.__data[index]

    def __generate_data(self, datum):
        event_type = int(datum['eventType'])
        if event_type == ReceiveEventType.MESSAGE:
            return Message(datum)
        elif event_type == ReceiveEventType.OPERATION:
            return Operation(datum)
        else:
            raise ValueError('Invalid event type.')


class Message():
    def __init__(self, datum):
        self.__data = {
            'id': datum['content']['id'],
            'from_mid': datum['content']['from'],
            'to_mid': datum['content']['to'],
            'from_channel_id': datum['fromChannel'],
            'to_channel_id': datum['toChannel'],
            'event_type': datum['eventType'],
            'created_time': datum['content']['createdTime'],
            'content': self.__generate_content(datum['content']).content,
        }

    def __getitem__(self, key):
        return self.__data[key]

    def __generate_content(self, attrs):
        content_type = attrs['contentType']
        if content_type == ContentType.TEXT:
            return messages.TextMessage(
                text=attrs['text'],
            )
        elif content_type == ContentType.IMAGE:
            return messages.ImageMessage(
                image_url=attrs['originalContentUrl'],
                preview_url=attrs['previewImageUrl'],
            )
        elif content_type == ContentType.VIDEO:
            return messages.VideoMessage(
                video_url=attrs['originalContentUrl'],
                preview_url=attrs['previewImageUrl'],
            )
        elif content_type == ContentType.AUDIO:
            return messages.AudioMessage(
                audio_url=attrs['originalContentUrl'],
                duration=attrs['contentMetadata']['duration'],
            )
        elif content_type == ContentType.Location:
            return messages.LocationMessage(
                title=attrs['location']['title'],
                address=attrs['location']['address'],
                latitude=attrs['location']['latitude'],
                longitude=attrs['location']['longitude'],
            )
        elif content_type == ContentType.STICKER:
            return messages.StickerMessage(
                stkpkgid=attrs['contentMetadata']['STKPKGID'],
                stkid=attrs['contentMetadata']['STKID'],
                stkver=attrs['contentMetadata']['STKVER'],
            )
        else:
            raise ValueError('Invalid content type.')


class Operation():
    def __init__(self, datum):
        pass
