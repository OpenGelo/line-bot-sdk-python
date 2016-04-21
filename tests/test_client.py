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


class TestSignatureValidation():
    def test_validate_signature_valid(self, fx_client, fx_signature, fx_request_content):
        result = fx_client.validate_signature(fx_signature, fx_request_content)
        assert result is True

    def test_validate_signature_invalid(self, fx_client, fx_request_content):
        result = fx_client.validate_signature('', fx_request_content)
        assert result is False


class TestLineBotClientGetMessageContent():
    @responses.activate
    def test_get_message_content(self, fx_client, fx_message_id, mocking):
        response = fx_client.get_message_content(fx_message_id)
        assert response.status_code == 200


class TestLineBotClientGetMessageContentPreview():
    @responses.activate
    def test_get_message_content_preview(self, fx_client, fx_message_id, mocking):
        response = fx_client.get_message_content_preview(fx_message_id)
        assert response.status_code == 200


class TestLineBotClientSendMessages():
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


class TestLineBotClientSendMultipleMessages():
    @responses.activate
    def test_send(self, fx_client, mocking):
        response = (
            fx_client.multiple_message
            .add_text(text='')
            .send(to_mid=[mocking['mid']])
        )
        assert response.status_code == 200


class TestLineBotClientSendRichMessages():
    @responses.activate
    def test_send(self, fx_client, mocking):
        response = (
            fx_client.rich_message
            .set_action(MANGA={'text': 'manga', 'link_url': 'link_url'})
            .add_listener(action='MANGA', x=0, y=0, width=520, height=520)
            .send(to_mid=[mocking['mid']], image_url='image_url', alt_text='alt_text')
        )
        assert response.status_code == 200
