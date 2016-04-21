# -*- coding: utf-8 -*-

from linebot.users import UserProfile


class TestUserProfile():
    def test_user_profile(self, fx_user_profiles):
        for profile in fx_user_profiles:
            p = UserProfile(profile)
            assert isinstance(p, UserProfile)
            assert p['mid'] == profile['mid']
            assert p['display_name'] == profile['displayName']
            assert p['picture_url'] == profile['pictureUrl']
            assert p['status_message'] == profile['statusMessage']
