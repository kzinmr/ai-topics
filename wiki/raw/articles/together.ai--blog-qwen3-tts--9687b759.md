---
title: "Qwen3 TTS is now available on Together AI"
url: "https://www.together.ai/blog/qwen3-tts"
fetched_at: 2026-11-21T10:01:11.572316+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Qwen3 TTS is now available on Together AI

Source: https://www.together.ai/blog/qwen3-tts

Starting today, developers can run
Qwen3 TTS
on Together AI, with first audio in as little as 97ms.
Qwen3 TTS is an open text-to-speech model that separates who is speaking from how they speak. You choose one of nine preset voices, and that voice stays the same while you change its delivery with a plain-language instruction, such as "excited and upbeat," or move it between 10 languages.
Together AI's inference team tuned the serving stack for Qwen3 TTS so that speech starts streaming quickly enough for real-time conversation. The model is available now on Together Serverless Inference and on dedicated endpoints.
Tell it how to say the line
The same sentence can land as good news or bad news depending on how it's said, and with Qwen3 TTS you decide which by describing the delivery in a few words. Here the voice
aiden
reads one line three times. The voice and the words don't change between clips, only the instruction.
aiden · excited and upbeat
"Well, that changes everything."
aiden · angry and impatient
"Well, that changes everything."
aiden · sad and disappointed
"Well, that changes everything."
The instruction controls the delivery, and the voice stays the one you chose. You can keep that same voice when you change languages too.
Keep one voice across 10 languages
Every preset voice speaks all 10 supported languages: Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian. That lets a product keep the same voice when it moves into a new market. Here
aiden
, an English voice, reads the same order update in four languages.
"Your order has shipped and should arrive on Thursday."
"Tu pedido ha sido enviado y debería llegar el jueves."
"Ihre Bestellung wurde versandt und sollte am Donnerstag ankommen."
"ご注文の商品は発送済みで、木曜日に到着する予定です。"
Supply the text in the language you select; the four clips above use separately translated text. Each voice also has a native language, and Qwen recommends using a voice in its native language for the best quality, so listen to the languages your application needs before you settle on a preset.
Choose a voice in VoiceFinder
The quickest way to choose a preset is to hear each one say your own lines.
VoiceFinder
lists the Qwen3 TTS voices, plays a sample of each and reads the text you enter in any of them.
Open
voicefinder.together.ai
, select
Qwen/Qwen3-TTS-12Hz-1.7B
in the model menu and select
Find voices
.
Select
Preview
to play a sample of a voice.
Select
Try custom text
, enter up to 500 characters and select
Generate
to hear that voice read your text. Repeat with another voice to compare them on the same text.
Select
Show code
to get the request for that voice in Python, TypeScript or cURL.
The nine preset voices, with each one's native language and Qwen's description:
Voice
Native language
Description
aiden
English
Sunny American male voice with a clear midrange
ryan
English
Dynamic male voice with strong rhythmic drive
vivian
Chinese
Bright, slightly edgy young female voice
serena
Chinese
Warm, gentle young female voice
uncle_fu
Chinese
Seasoned male voice with a low, mellow timbre
dylan
Chinese, Beijing dialect
Youthful Beijing male voice with a clear, natural timbre
eric
Chinese, Sichuan dialect
Lively Chengdu male voice with a slightly husky brightness
ono_anna
Japanese
Playful Japanese female voice with a light, nimble timbre
sohee
Korean
Warm Korean female voice with rich emotion
Generate speech
You need the Together Python SDK (
pip install together
) and a
TOGETHER_API_KEY
. This request sets the voice, the language and the instruction together, and produces the excited reading of the line above.
from together import Together

client = Together()

response = client.audio.speech.create(
    model="Qwen/Qwen3-TTS-12Hz-1.7B",
    input="Well, that changes everything.",
    voice="aiden",  # who speaks
    language="en",  # the language of the text
    extra_body={"instructions": "excited and upbeat"},  # how to say it
    response_format="mp3",
)

response.write_to_file("excited.mp3")
The Python SDK passes
instructions
through
extra_body
. If an instruction doesn't seem to change the delivery, check that the field is spelled
instructions
, since a misspelled field is skipped without an error.
Parameters for this model:
Parameter
What to send
voice
One of the nine voice names, lowercase
instructions
A short description of the delivery, such as
excited and upbeat
. Optional
language
ISO 639-1 code for the input text, such as
en
,
zh
,
ja
or
ko
response_format
wav
,
mp3
,
raw
or
mulaw
.
opus
,
aac
and
flac
aren't supported
sample_rate
24000
(default) or
8000
Word timestamps (
alignment=word
) aren't supported for Qwen3 TTS.
Stream audio for a voice agent
In a voice agent, speech has to start before the whole reply has been synthesized. On Together AI, Qwen3 TTS returns first audio in as little as 97ms, and it streams in two ways. The right one depends on whether you have the full text when you make the request.
When you have the full text: streaming over HTTP
With
stream=True
and
response_format="raw"
, the speech API returns server-sent events as the audio is generated. Each
conversation.item.audio_output.delta
event carries a base64-encoded chunk of audio. This script receives the stream, decodes each chunk and saves the audio to a file.
import base64
import json

from together import Together

client = Together()

with client.audio.speech.with_streaming_response.create(
    model="Qwen/Qwen3-TTS-12Hz-1.7B",
    input="Your order has shipped and should arrive on Thursday.",
    voice="aiden",
    language="en",
    extra_body={"instructions": "excited and upbeat"},
    stream=True,
    response_format="raw",
    response_encoding="pcm_s16le",
) as response, open("order-update.pcm", "wb") as audio:
    for line in response.iter_lines():
        if not line.startswith("data: {"):
            continue
        event = json.loads(line[len("data: "):])
        if event.get("type") == "conversation.item.audio_output.delta":
            # Each event carries a base64 chunk of 16-bit PCM at 24 kHz
            audio.write(base64.b64decode(event["delta"]))
The output is 16-bit mono PCM at 24 kHz, and the instruction applies to a streamed request the same way it does to a complete one. To play speech as it arrives, send each decoded chunk to your audio output instead of a file.
When the text is still being written: WebSocket
If the text comes from a language model token by token, the WebSocket endpoint lets you send it in pieces. You open one connection, append text as it becomes available and commit when the input is complete, and the server synthesizes each sentence once it has the whole sentence. This script sends an order update in two pieces and saves the audio that comes back. It needs the
websockets
package, version 14 or later (
pip install websockets
).
import asyncio
import base64
import json
import os

import websockets

URL = (
    "wss://api.together.ai/v1/audio/speech/websocket"
    "?model=Qwen/Qwen3-TTS-12Hz-1.7B&voice=aiden&language=en"
    "&response_format=pcm&sample_rate=24000"
)


async def main():
    headers = {"Authorization": f"Bearer {os.environ['TOGETHER_API_KEY']}"}
    async with websockets.connect(URL, additional_headers=headers) as ws:
        # Append text as it becomes available, then commit once the input is complete
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": "Your order has shipped. "}))
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": "It should arrive on Thursday."}))
        await ws.send(json.dumps({"type": "input_text_buffer.commit"}))

        with open("order-update.pcm", "wb") as audio:
            async for message in ws:
                event = json.loads(message)
                if event["type"] == "conversation.item.audio_output.delta":
                    # Each event carries a base64 chunk of 16-bit PCM at 24 kHz
                    audio.write(base64.b64decode(event["delta"]))
                elif event["type"] == "conversation.item.audio_output.done":
                    break
                elif event["type"] == "conversation.item.tts.failed":
                    raise RuntimeError(event["error"])


asyncio.run(main())
The connection URL carries the model, voice, language and audio settings (the WebSocket endpoint names raw PCM
pcm
), and the audio arrives in the same base64 events as the HTTP stream. The
WebSocket guide
lists every message type.
Get started
FAQs
How much does Qwen3 TTS cost on Together AI?
Qwen3 TTS costs \$20 per 1M characters on Together Serverless Inference. The model is also available on dedicated endpoints.
How fast is Qwen3 TTS on Together AI?
Qwen3 TTS returns first audio in as little as 97ms on Together AI when you stream the response, on a serving stack our inference team tuned for real-time voice.
How do I control the tone of a Qwen3 TTS voice?
Send a plain-language description of the delivery in the
instructions
field of the speech request, such as
excited and upbeat
. In the Python SDK, pass it through
extra_body
. An instruction changes the emotion and tone of the voice and doesn't change who it sounds like.
Can one Qwen3 TTS voice speak more than one language?
Yes, each of the nine Qwen3 TTS preset voices can speak all 10 supported languages. Set
voice
to the voice name and
language
to the language of the text, and send the text in that language. Qwen recommends using each voice in its native language for the best quality.
Does Qwen3 TTS support streaming on Together AI?
Yes, Qwen3 TTS supports streaming on Together AI in two ways. Over HTTP, set
stream
to
true
and
response_format
to
raw
to receive server-sent events with base64-encoded PCM audio. Over WebSocket, send text in pieces and receive audio as it's generated.
What audio formats does Qwen3 TTS return?
Qwen3 TTS returns
wav
,
mp3
,
raw
(PCM) or
mulaw
audio on Together AI, at a sample rate of 24000 (the default) or 8000. It doesn't return
opus
,
aac
or
flac
.
How do I compare Qwen3 TTS voices before choosing one?
Open
VoiceFinder
and select
Qwen/Qwen3-TTS-12Hz-1.7B
in the model menu. You can preview each voice and generate up to 500 characters of your own text with it.
Is Qwen3 TTS open source?
Yes, Qwen released Qwen3 TTS 12Hz 1.7B under the Apache 2.0 license. The weights are on Hugging Face.
