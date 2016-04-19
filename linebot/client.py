# -*- coding: utf-8 -*-


class LineBotClient():
    def __init__(self, **credentials):
        self.credentials = {
            'X-Line-ChannelID': credentials['channel_id'],
            'X-Line-ChannelSecret': credentials['channel_secret'],
            'X-Line-Trusted-User-With-ACL': credentials['channel_mid'],
        }
