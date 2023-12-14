#!pip install TIME-python
#!pip install DateTime
#!pip install playsound
#!pip install SpeechRecognition
#!pip install wolframalpha
#!pip install PyObjC
#!pip install gTTs
import os
import datetime as dt
from gtts import *
from IPython.display import Audio

def speak(text):
  x=dt.datetime.now()
  tts=gTTS(text=text,lang='en')
  fname = str(x.hour)+"_"+str(x.minute)+"_"+str(x.second)+".mp3"
  file=fname
  tts.save(file)
  wn = Audio(file, autoplay=True)
  display(wn)
  os.remove(fname)
speak("what is mining!")
os.remove("/content/ReelAudio-1.mp3")
import os
import speech_recognition as sr
def speak(text):
    print(text)
    tts = gTTS(text=text,lang='en')
    file="/content/ReelAudio-1.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove("/content/ReelAudio-1.mp3")

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = " "
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: '+str(e))
    return said


