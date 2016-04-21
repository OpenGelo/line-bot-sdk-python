# -*- coding: utf-8 -*-

import json

from linebot import constants
from linebot.requests import Request


class TestRequest():
    def test_request_instance_creation(self, fx_client, fx_message, mocking):
        url = 'https://trialbot-api.line.me/v1/events'
        request = Request(
            url=url,
            credentials=fx_client.credentials,
            to_mid=[mocking['mid']],
            message=fx_message,
        )
        assert request.url == url
        assert request.headers == {
            'Content-Type': 'application/json; charset=UTF-8',
            'X-Line-ChannelID': fx_client.credentials['X-Line-ChannelID'],
            'X-Line-ChannelSecret': fx_client.credentials['X-Line-ChannelSecret'],
            'X-Line-Trusted-User-With-ACL': fx_client.credentials['X-Line-Trusted-User-With-ACL'],
        }
