# -*- coding: utf-8 -*-

import json

from linebot.constants import ReceiveEventType


class Receive():
    def __init__(self, content_json):
        parsed_json = json.loads(content_json)
        result = parsed_json['result']
        self.__data = [self.__generate_data(datum) for datum in result]

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
        pass


class Operation():
    def __init__(self, datum):
        pass
