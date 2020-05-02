#!/usr/bin/python3
import speech_recognition as sr
from gtts import gTTS
import os


mytext = 'Hi, Giovanni'
language = 'en'


r = sr.Recognizer()
with sr.Microphone() as source:

    try:
        print("Speak Anything :" )
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        if format(text) == "hello":
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("welcome.mp3")
            os.system("play welcome.mp3")
    except:
        print("Sorry could not recognize what you said")