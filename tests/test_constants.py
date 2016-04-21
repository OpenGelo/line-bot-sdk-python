# -*- coding: utf-8 -*-

from linebot import constants


class TestConstants():
    def test_constants(self):
        assert constants.API_URL_BASE == 'https://trialbot-api.line.me'
        assert constants.API_VERSION == 'v1'
        assert constants.TO_CHANNEL == 1383378250

    def test_content_type(self):
        assert constants.ContentType.TEXT.value == 1
        assert constants.ContentType.IMAGE.value == 2
        assert constants.ContentType.VIDEO.value == 3
        assert constants.ContentType.AUDIO.value == 4
        assert constants.ContentType.LOCATION.value == 7
        assert constants.ContentType.STICKER.value == 8
        assert constants.ContentType.CONTACT.value == 10
        assert constants.ContentType.RICH_MESSAGE.value == 12

    def test_op_type(self):
        assert constants.OpType.ADDED_AS_FRIEND == 4
        assert constants.OpType.BLOCKED_ACCOUNT == 8

    def test_receive_event_type(self):
        assert constants.ReceiveEventType.MESSAGE == 138311609000106303
        assert constants.ReceiveEventType.OPERATION == 138311609100106403
