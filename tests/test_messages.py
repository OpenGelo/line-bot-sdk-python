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

    def test_location_message(self):
        title = 'Convention center'
        latitude = 35.61823286112982
        longitude = 139.72824096679688
        message = messages.LocationMessage(
            title=title,
            latitude=latitude,
            longitude=longitude,
        )
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 7,
            'toType': 1,
            'text': title,
            'location': {
                'title': title,
                'address': None,
                'latitude': latitude,
                'longitude': longitude,
            },
        }

    def test_sticker_message(self):
        stkpkgid = 332
        stkid = 3
        stkver = 100
        message = messages.StickerMessage(
            stkpkgid=stkpkgid,
            stkid=stkid,
            stkver=stkver,
        )
        assert message.event_type == '138311608800106203'
        assert message.content == {
            'contentType': 8,
            'toType': 1,
            'contentMetadata': {
                'STKPKGID': str(stkpkgid),
                'STKID': str(stkid),
                'STKVER': str(stkver),
            },
        }
