# -*- coding: utf-8 -*-

import pytest
import responses

from linebot import constants
from linebot import messages
from linebot.client import LineBotClient


@pytest.fixture
def fx_channel_id():
    return 1234567890


@pytest.fixture
def fx_channel_secret():
    return 'abcdefghijklmnopqrstuvwxyz012345'


@pytest.fixture
def fx_channel_mid():
    return 'u0047556f2e40dba2456887320ba7c76d'


@pytest.fixture
def fx_client(fx_channel_id, fx_channel_secret, fx_channel_mid):
    credentials = {
        'channel_id': fx_channel_id,
        'channel_secret': fx_channel_secret,
        'channel_mid': fx_channel_mid,
    }
    client = LineBotClient(**credentials)
    return client


@pytest.fixture
def fx_message():
    return messages.TextMessage(text='')


@pytest.yield_fixture
def mocking():
    params = {
        'message_id': '123456789',
        'mid': 'u0047556f2e40dba2456887320ba7c76d',
    }
    responses.add(responses.POST, constants.API_URL_EVENTS, status=200)
    yield params
