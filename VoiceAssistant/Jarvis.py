import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecognition
import os
import webbrowser # pip install webbrowser
from datetime import datetime
import wikipedia # pip install wikipedia

def assistant_recognizer():
    Microphone = sr.Microphone
    Recognition = sr.Recognizer
    try:
        with Microphone as source:
            try:
                Recognition.adjust_for_ambient_noise(source)
                Recognition.dynamic_energy_threshold = 3000
                speech = Recognition.listen(source, phrase_time_limit=6) 
                speech = ''
                text = Recognition.recognize_google(speech, language='en-us'), print("Got it! Now to recognize it")
                print(f"You Said {text}")
            except sr.WaitTimeoutError:
                pass
            except sr.RequestError:
                response("I am Having Trouble Initiating Your Request")
            except Exception as e:
                print("Oops! Didn't catch that")
    
            return speech.lower()
    except Exception as e:
        print(e), response("I Am Having Trouble Understanding Right Now")

processor()