# -*- coding: utf-8 -*-

from linebot import messages


class TestMessages():
    def test_text_message(self):
        test_text = 'TEST TEXT MESSAGE'
        message = messages.TextMessage(text=test_text)
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 1,
            'toType': 1,
            'text': test_text,
        }

    def test_image_message(self):
        image_url = 'image_url'
        preview_url = 'preview_url'
        message = messages.ImageMessage(
            image_url=image_url,
            preview_url=preview_url,
        )
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 2,
            'toType': 1,
            'originalContentUrl': image_url,
            'previewImageUrl': preview_url,
        }

    def test_video_message(self):
        video_url = 'video_url'
        preview_url = 'preview_url'
        message = messages.VideoMessage(
            video_url=video_url,
            preview_url=preview_url,
        )
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 3,
            'toType': 1,
            'originalContentUrl': video_url,
            'previewImageUrl': preview_url,
        }

    def test_audio_message(self):
        audio_url = 'audio_url'
        duration = 240000
        message = messages.AudioMessage(
            audio_url=audio_url,
            duration=duration,
        )
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 4,
            'toType': 1,
            'originalContentUrl': audio_url,
            'contentMetadata': {
                'AUDLEN': str(duration),
            },
        }
