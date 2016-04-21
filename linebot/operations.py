# -*- coding: utf-8 -*-


class BaseOperation(object):
    def __init__(self, **attrs):
        self.__attrs = attrs

    def __getitem__(self, key):
        return self.__attrs[key]


class AddedAsFriend(BaseOperation):
    pass


class BlockedAccount(BaseOperation):
    pass
