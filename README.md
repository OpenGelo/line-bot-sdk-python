# line-bot-sdk-python [![PyPI version](https://badge.fury.io/py/linebot.svg)](https://badge.fury.io/py/linebot) [![Build Status](https://travis-ci.org/studio3104/line-bot-sdk-python.svg?branch=master)](https://travis-ci.org/studio3104/line-bot-sdk-python)

## Configuration

```python
from linebot.client import LineBotClient

credentials = {
    'channel_id': 'YOUR LINE BOT Channel ID',
    'channel_secret': 'YOUR LINE BOT Channel Secret',
    'channel_mid': 'YOUR LINE BOT MID',
}
client = LineBotClient(**credentials)
```

## Usage

### Sending messages

After configuring a client, you can start sending messages as the following reference.

- [https://developers.line.me/bot-api/api-reference#sending_message](https://developers.line.me/bot-api/api-reference#sending_message)

Sending message APIs requires the following parameter.

- `:to_mid` String or Array

```python
client.send_text(
    to_mid='12345678',
)

client.send_text(
    to_mid=['12345678', '23456789'],
)
```

#### send_text

```python
client.send_text(
    to_mid=to_mid,
    text='Hello',
)
```

#### send_image

```python
client.send_image(
    to_mid=to_mid,
    image_url='http://example.com/image.jpg',            # originalContentUrl
    preview_url='http://example.com/image_preview.jpg',  # previewImageUrl
)
```

#### send_video

```python
client.send_video(
    to_mid=to_mid,
    video_url='http://example.com/video.mp4',            # originalContentUrl
    preview_url='http://example.com/video_preview.jpg'   # previewImageUrl
)
```

#### send_audio

```python
client.send_audio(
    to_mid=to_mid,
    audio_url='http://example.com/audio.mp3',            # originalContentUrl
    duration=120000
)
```

#### send_location

```python
client.send_location(
    to_mid=to_mid,
    title='LINE Corporation.',
    address='Hikarie  Shibuya-ku Tokyo 151-0002',        # location.address
    latitude=35.61823286112982,                          # location.latitude
    longitude=139.72824096679688,                        # location.longitude
)
```

#### send_sticker

See online documentation to find which sticker's you can send.

- [https://developers.line.me/bot-api/api-reference#sending_message_sticker](https://developers.line.me/bot-api/api-reference#sending_message_sticker)

```python
client.send_sticker(
    to_mid=to_mid,
    stkpkgid=2,                                          # contentMetadata.STKPKGID
    stkid=144,                                           # contentMetadata.STKID
    stkver=100                                           # contentMetadata.STKVER
)
```

### Sending multiple message

Support on sending multiple message.
- [https://developers.line.me/bot-api/api-reference#sending_multiple_messages](https://developers.line.me/bot-api/api-reference#sending_multiple_messages)

```python
(
    client.multiple_message
    .add_text(text=text)
    .add_image(image_url=image_url, preview_url=preview_url)
    .add_video(video_url=video_url, preview_url=preview_url)
    .add_audio(audio_url=audio_url, duration=duration)
    .add_location(title=title, latitude=latitude, longitude=longitude)
    .add_sticker(stkpkgid=stkpkgid, stkid=stkid, stkver=stkver)
    .send(to_mid=to_mid)
)
```

### Sending rich message

Support on sending rich message.

See also a online document.
- [https://developers.line.me/bot-api/api-reference#sending_rich_content_message](https://developers.line.me/bot-api/api-reference#sending_rich_content_message)

```python
(
    client.rich_message
    .set_action(MANGA={'text': text, 'link_url': link_url})
    .add_listener(action=action, x=x, y=y, width=w, height=h)
    .send(to_mid=[mocking['mid']], image_url=image_url, alt_text=alt_text)
)
```

### Signature validation

```python
if not client.validate_signature(request.headers.get('X-Line-Channelsignature'), request.get_data()):
    # Handle an error
```

### Receiving request

```python
receive = Receive(request.get_data())
for r in receive:
    if isinstance(r['content'], messages.TextMessage):
        response_text = 'Hmm? Did you say "{}" ?'.format(r['content']['text'].encode('utf-8'))
```

### Getting message content

Get the original file which was sent by user.

### Getting preview of message content

Get the preview image file which was sent by user.

### Getting user profile information

```python
client.get_user_profile('1234567', '8910112')
#=> [<linebot.users.UserProfile instance at 0x000000000000>, <linebot.users.UserProfile instance at 0x000000000000>]
```
