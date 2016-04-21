# -*- coding: utf-8 -*-

import json
import responses

from linebot.builders import MultipleMessage, RichMessage


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
        text = 'TEST TEXT MESSAGE'
        multiple_message = fx_multiple_message.add_text(text=text)
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 1,
                    'text': text,
                    'toType': 1,
                },
            ],
        }

    def test_add_image(self, fx_multiple_message):
        image_url = 'image_url'
        preview_url = 'preview_url'
        multiple_message = fx_multiple_message.add_image(
            image_url=image_url,
            preview_url=preview_url,
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 2,
                    'originalContentUrl': image_url,
                    'previewImageUrl': preview_url,
                    'toType': 1,
                },
            ],
        }

    def test_add_video(self, fx_multiple_message):
        video_url = 'video_url'
        preview_url = 'preview_url'
        multiple_message = fx_multiple_message.add_video(
            video_url=video_url,
            preview_url=preview_url,
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 3,
                    'originalContentUrl': video_url,
                    'previewImageUrl': preview_url,
                    'toType': 1,
                },
            ],
        }

    def test_add_audio(self, fx_multiple_message):
        audio_url = 'audio_url'
        duration = 240000
        multiple_message = fx_multiple_message.add_audio(
            audio_url=audio_url,
            duration=duration,
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 4,
                    'originalContentUrl': audio_url,
                    'contentMetadata': {
                        'AUDLEN': str(duration)
                    },
                    'toType': 1,
                },
            ],
        }

    def test_add_location(self, fx_multiple_message):
        title = 'Convention center'
        latitude = 35.61823286112982
        longitude = 139.72824096679688
        multiple_message = fx_multiple_message.add_location(
            title=title,
            latitude=latitude,
            longitude=longitude,
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 7,
                    'text': title,
                    'location': {
                        'title': title,
                        'address': None,
                        'latitude': latitude,
                        'longitude': longitude,
                    },
                    'toType': 1,
                },
            ],
        }

    def test_add_sticker(self, fx_multiple_message):
        stkpkgid = 332
        stkid = 3
        stkver = 100
        multiple_message = fx_multiple_message.add_sticker(
            stkpkgid=stkpkgid,
            stkid=stkid,
            stkver=stkver,
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 8,
                    'contentMetadata': {
                        'STKPKGID': str(stkpkgid),
                        'STKID': str(stkid),
                        'STKVER': str(stkver),
                    },
                    'toType': 1,
                },
            ],
        }

    @responses.activate
    def test_send_after_adding_everything_one_by_one(self, fx_multiple_message, mocking):
        text = 'TEST TEXT MESSAGE'
        preview_url = 'preview_url'
        image_url = 'image_url'
        video_url = 'video_url'
        audio_url = 'audio_url'
        duration = 240000
        title = 'Convention center'
        latitude = 35.61823286112982
        longitude = 139.72824096679688
        stkpkgid = 332
        stkid = 3
        stkver = 100
        multiple_message = (
            fx_multiple_message
            .add_text(text=text)
            .add_image(image_url=image_url, preview_url=preview_url)
            .add_video(video_url=video_url, preview_url=preview_url)
            .add_audio(audio_url=audio_url, duration=duration)
            .add_location(title=title, latitude=latitude, longitude=longitude)
            .add_sticker(stkpkgid=stkpkgid, stkid=stkid, stkver=stkver)
        )
        assert isinstance(multiple_message, MultipleMessage)
        assert id(fx_multiple_message) == id(multiple_message)
        assert multiple_message.is_valid()
        assert multiple_message.event_type == '140177271400161403'
        assert multiple_message.content == {
            'messageNotified': 0,
            'messages': [
                {
                    'contentType': 1,
                    'text': text,
                    'toType': 1,
                },
                {
                    'contentType': 2,
                    'originalContentUrl': image_url,
                    'previewImageUrl': preview_url,
                    'toType': 1,
                },
                {
                    'contentType': 3,
                    'originalContentUrl': video_url,
                    'previewImageUrl': preview_url,
                    'toType': 1,
                },
                {
                    'contentType': 4,
                    'originalContentUrl': audio_url,
                    'contentMetadata': {
                        'AUDLEN': str(duration)
                    },
                    'toType': 1,
                },
                {
                    'contentType': 7,
                    'text': title,
                    'location': {
                        'title': title,
                        'address': None,
                        'latitude': latitude,
                        'longitude': longitude,
                    },
                    'toType': 1,
                },
                {
                    'contentType': 8,
                    'contentMetadata': {
                        'STKPKGID': str(stkpkgid),
                        'STKID': str(stkid),
                        'STKVER': str(stkver),
                    },
                    'toType': 1,
                },
            ],
        }

        response = multiple_message.send(to_mid=[mocking['mid']])
        assert response.status_code == 200


class TestRichMessage():
    def test_instance_creation(self, fx_client):
        rich_message = RichMessage(fx_client)
        assert isinstance(rich_message, RichMessage)

    @responses.activate
    def test_send_setting_action_and_adding_listener(self, fx_rich_message, mocking):
        text = 'manga'
        action = 'MANGA'
        x, y, w, h = 0, 0, 520, 520
        link_url = 'link_url'
        image_url = 'image_url'
        alt_text = 'alt_text'
        response = (
            fx_rich_message
            .set_action(MANGA={'text': text, 'link_url': link_url})
            .add_listener(action=action, x=x, y=y, width=w, height=h)
            .send(to_mid=[mocking['mid']], image_url=image_url, alt_text=alt_text)
        )
        assert response.status_code == 200
        assert fx_rich_message.event_type == '138311608800106203'
        assert fx_rich_message.content['contentType'] == 12
        assert fx_rich_message.content['toType'] == 1
        assert fx_rich_message.content['contentMetadata']['DOWNLOAD_URL'] == image_url
        assert fx_rich_message.content['contentMetadata']['SPEC_REV'] == 1
        assert fx_rich_message.content['contentMetadata']['ALT_TEXT'] == alt_text
        assert json.loads(fx_rich_message.content['contentMetadata']['MARKUP_JSON']) == {
            'images': {'image1': {'y': 0, 'x': 0, 'w': 1040, 'h': h}},
            'canvas': {'initialScene': 'scene1', 'width': 1040, 'height': h},
            'scenes': {
                'scene1': {
                    'listeners': [{'action': action, 'params': [x, y, w, h], 'type': 'touch'}],
                    'draws': [{'y': 0, 'x': 0, 'image': 'image1', 'w': 1040, 'h': h}],
                },
            },
            'actions': {action: {'text': text, 'type': 'web', 'params': {'linkUri': link_url}}},
        }
