# -*- coding: utf-8 -*-

from linebot import constants


class TestConstants():
    def test_constants(self):
        assert constants.API_URL_BASE == 'https://trialbot-api.line.me'
        assert constants.API_VERSION == 'v1'
        assert constants.API_URL_EVENTS == 'https://trialbot-api.line.me/v1/events'

        assert constants.TO_CHANNEL == 1383378250
