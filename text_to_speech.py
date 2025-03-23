from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text, lang="hi")
    tts.save(filename)
    return filename
