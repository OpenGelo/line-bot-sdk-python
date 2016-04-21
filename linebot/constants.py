# -*- coding: utf-8 -*-

import enum

API_URL_BASE = 'https://trialbot-api.line.me'
API_VERSION = 'v1'
TO_CHANNEL = 1383378250


class ContentType(enum.IntEnum):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    LOCATION = 7
    STICKER = 8
    CONTACT = 10
    RICH_MESSAGE = 12


class OpType(enum.IntEnum):
    ADDED_AS_FRIEND = 4
    BLOCKED_ACCOUNT = 8


class ReceiveEventType(enum.IntEnum):
    MESSAGE = 138311609000106303
    OPERATION = 138311609100106403
