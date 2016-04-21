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
        self.__attrs = kwargs

    def validate(self):
        pass

    def get(self):
        return requests.get(self.url, headers=self.headers)

    def post(self):
        response = requests.post(
            self.url,
            data=self.__create_payload(),
            headers=self.headers,
        )
        return response

    def __create_to_mid(self):
        to_mid = self.__attrs['to_mid']
        return to_mid if isinstance(to_mid, list) else [to_mid]

    def __create_payload(self):
        message = self.__attrs['message']
        payload = {
            'to': self.__create_to_mid(),
            'toChannel': constants.TO_CHANNEL,
            'eventType': message.event_type,
            'content': message.content,
        }
        return json.dumps(payload)

    def __create_headers(self, credentials):
        headers = copy.deepcopy(credentials)
        headers['Content-Type'] = 'application/json; charset=UTF-8'
        return headers
