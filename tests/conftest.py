# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def fx_channel_id():
    return 1234567890


@pytest.fixture
def fx_channel_secret():
    return 'abcdefghijklmnopqrstuvwxyz012345'


@pytest.fixture
def fx_channel_mid():
    return 'u0047556f2e40dba2456887320ba7c76d'
