# -*- coding: utf-8 -*-

from linebot.client import LineBotClient


class TestLineBotClient():
    def test_creating_instances(self, fx_channel_id, fx_channel_secret, fx_channel_mid):
        credentials = {
            'channel_id': fx_channel_id,
            'channel_secret': fx_channel_secret,
            'channel_mid': fx_channel_mid,
        }
        LineBotClient(**credentials)
