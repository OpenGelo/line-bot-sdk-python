# -*- coding: utf-8 -*-

import responses

from linebot.client import LineBotClient


class TestLineBotClient():
    def test_client_instance_creation(self, fx_channel_id, fx_channel_secret, fx_channel_mid):
        credentials = {
            'channel_id': fx_channel_id,
            'channel_secret': fx_channel_secret,
            'channel_mid': fx_channel_mid,
        }
        LineBotClient(**credentials)

    @responses.activate
    def test_send_text(self, fx_client, mocking):
        response = fx_client.send_text(to_mid=[mocking['mid']], text='')
        assert response.status_code == 200

    @responses.activate
    def test_send_image(self, fx_client, mocking):
        response = fx_client.send_image(
            to_mid=[mocking['mid']],
            image_url='',
            preview_url='',
        )
        assert response.status_code == 200

    @responses.activate
    def test_send_video(self, fx_client, mocking):
        response = fx_client.send_video(
            to_mid=[mocking['mid']],
            video_url='',
            preview_url='',
        )
        assert response.status_code == 200

    @responses.activate
    def test_send_audio(self, fx_client, mocking):
        response = fx_client.send_audio(
            to_mid=[mocking['mid']],
            audio_url='audio_url',
            duration=240000,
        )
        assert response.status_code == 200

    @responses.activate
    def test_send_location(self, fx_client, mocking):
        response = fx_client.send_location(
            to_mid=[mocking['mid']],
            title='Convention center',
            latitude=35.61823286112982,
            longitude=139.72824096679688,
        )
        assert response.status_code == 200

    @responses.activate
    def test_send_sticker(self, fx_client, mocking):
        response = fx_client.send_sticker(
            to_mid=[mocking['mid']],
            stkpkgid=332,
            stkid=3,
            stkver=100,
        )
        assert response.status_code == 200
