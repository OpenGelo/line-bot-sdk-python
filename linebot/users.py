# -*- coding: utf-8 -*-


class UserProfile():
    def __init__(self, contact):
        self.__profile = {
            'mid': contact['mid'],
            'display_name': contact['displayName'],
            'picture_url': contact['pictureUrl'],
            'status_message': contact['statusMessage'],
        }

    def __getitem__(self, key):
        return self.__profile[key]
