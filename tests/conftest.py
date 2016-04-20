# -*- coding: utf-8 -*-

import pytest
import responses

from linebot import constants
from linebot import messages
from linebot.client import LineBotClient


@pytest.fixture
def fx_request_content():
    return "{\n  \"result\":[\n    {\n      \"from\":\"u206d25c2ea6bd87c17655609a1c37cb8\",\n      \"fromChannel\":\"1341301815\",\n      \"to\":[\"u0cc15697597f61dd8b01cea8b027050e\"],\n      \"toChannel\":\"1441301333\",\n      \"eventType\":\"138311609000106303\",\n      \"id\":\"ABCDEF-12345678901\",\n      \"content\":{\n        \"id\":\"325708\",\n        \"createdTime\":1332394961610,\n        \"from\":\"uff2aec188e58752ee1fb0f9507c6529a\",\n        \"to\":[\"u0a556cffd4da0dd89c94fb36e36e1cdc\"],\n        \"toType\":1,\n        \"contentType\":1,\n        \"text\":\"hello\"\n      }\n    },\n    {\n      \"from\":\"u206d25c2ea6bd87c17655609a1c37cb8\",\n      \"fromChannel\":\"1341301815\",\n      \"to\":[\"u0cc15697597f61dd8b01cea8b027050e\"],\n      \"toChannel\":\"1441301333\",\n      \"eventType\":\"138311609100106403\",\n      \"id\":\"ABCDEF-12345678902\",\n      \"content\":{\n        \"revision\":2469,\n        \"opType\":4,\n        \"params\":[\n          \"u0f3bfc598b061eba02183bfc5280886a\",\n          null,\n          null\n        ]\n      }\n    }\n  ]\n}\n"


@pytest.fixture
def fx_signature():
    return 'YdUyzEMBcQwsneRE8RkWm9/3AF+Zms+Mj1sh7d/biuc='


@pytest.fixture
def fx_channel_id():
    return 1234567890


@pytest.fixture
def fx_channel_secret():
    return 'testsecret'


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
