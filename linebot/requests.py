# -*- coding: utf-8 -*-

from __future__ import absolute_import

import copy
import json
import requests

from linebot import constants


class Request():
    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.headers = self.__create_headers(kwargs['credentials'])
        self.payload = self.__create_payload(kwargs['to_mid'], kwargs['message'])

    def validate(self):
        pass

    def post(self):
        response = requests.post(
            self.url,
            data=self.payload,
            headers=self.headers,
        )
        return response

    def __create_payload(self, to_mid, message):
        payload = {
            'to': to_mid,
            'toChannel': constants.TO_CHANNEL,
            'eventType': message.event_type,
            'content': message.content,
        }
        return json.dumps(payload)

    def __create_headers(self, credentials):
        headers = copy.deepcopy(credentials)
        headers['Content-Type'] = 'application/json; charset=UTF-8'
        return headers
