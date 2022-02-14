import os
import pyttsx3
import speech_recognition as sr
from gtts import gTTS


mytext='hello world'*2
language='en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")