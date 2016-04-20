# -*- coding: utf-8 -*-

import responses

from linebot.builders import MultipleMessage


class TestMultipleMessage():
    def test_instance_creation(self, fx_client):
        multiple_message = MultipleMessage(fx_client)
        assert isinstance(multiple_message, MultipleMessage)

    def test_invalid_multiple_message(self, fx_multiple_message):
        assert not fx_multiple_message.is_valid()

    @responses.activate
    def test_send(self, fx_multiple_message, mocking):
        response = fx_multiple_message.add_text(text='').send(to_mid=[mocking['mid']])
        assert response.status_code == 200

    def test_add_text(self, fx_multiple_message):
        multiple_message = fx_multiple_message.add_text(text='')
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()

    def test_add_image(self, fx_multiple_message):
        multiple_message = fx_multiple_message.add_image(
            image_url='image_url',
            preview_url='preview_url',
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()

    def test_add_video(self, fx_multiple_message):
        multiple_message = fx_multiple_message.add_video(
            video_url='video_url',
            preview_url='preview_url',
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
