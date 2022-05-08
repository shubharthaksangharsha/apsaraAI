from gtts import gTTS
import speech_recognition as sr
import os
def speak(text):
    speech = gTTS(text=text, lang="en", slow=False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")

