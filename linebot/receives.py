# -*- coding: utf-8 -*-

import json

from linebot import messages
from linebot import operations
from linebot.constants import ContentType, OpType, ReceiveEventType


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
        content = datum['content']
        self.__data = {
            'id': content['id'],
            'from_mid': content['from'],
            'to_mid': content['to'],
            'from_channel_id': datum['fromChannel'],
            'to_channel_id': datum['toChannel'],
            'event_type': datum['eventType'],
            'created_time': content['createdTime'],
            'content': self.__generate_content(content),
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
                image_url=attrs.get('originalContentUrl'),
                preview_url=attrs.get('previewImageUrl'),
            )
        elif content_type == ContentType.VIDEO:
            return messages.VideoMessage(
                video_url=attrs.get('originalContentUrl'),
                preview_url=attrs.get('previewImageUrl'),
            )
        elif content_type == ContentType.AUDIO:
            meta = attrs.get('contentMetadata')
            duration = meta.get('duration') if meta else None
            return messages.AudioMessage(
                audio_url=attrs.get('originalContentUrl'),
                duration=duration,
            )
        elif content_type == ContentType.LOCATION:
            location = attrs['location']
            return messages.LocationMessage(
                title=location['title'],
                address=location['address'],
                latitude=location['latitude'],
                longitude=location['longitude'],
            )
        elif content_type == ContentType.STICKER:
            meta = attrs['contentMetadata']
            return messages.StickerMessage(
                stkpkgid=meta['STKPKGID'],
                stkid=meta['STKID'],
                stkver=meta['STKVER'],
            )
        else:
            raise ValueError('Invalid content type.')


class Operation():
    def __init__(self, datum):
        self.__data = {
            'id': datum['id'],
            'from_mid': datum['content']['params'][0],
            'to_mid': datum['to'],
            'from_channel_id': datum['fromChannel'],
            'to_channel_id': datum['toChannel'],
            'event_type': datum['eventType'],
            'content': self.__generate_content(datum['content']),
        }

    def __getitem__(self, key):
        return self.__data[key]

    def __generate_content(self, attrs):
        op_type = attrs['opType']
        if op_type == OpType.ADDED_AS_FRIEND:
            return operations.AddedAsFriend(
                revision=attrs['revision'],
                op_type=attrs['opType'],
                params=attrs['params'],
            )
        elif op_type == OpType.BLOCKED_ACCOUNT:
            return operations.BlockedAccount(
                revision=attrs['revision'],
                op_type=attrs['opType'],
                params=attrs['params'],
            )
        else:
            raise ValueError('Invalid op type.')
