import warnings
from pyttsx3 import speak
import speech_recognition as sr
warnings.filterwarnings('ignore')


def speech_recognition_system():
    Recognition = sr.Recognizer()
    Microphone = sr.Microphone()
    return Recognition,Microphone

Recognition, Microphone = speech_recognition_system()


def __init__parser():
    with speech_recognition_system():
        try:
            with Microphone as source:
                Recognition.adjust_for_ambient_noise(source)
                Recognition.dynamic_energy_threshold = 3000
                audio = Recognition.listen(source, phrase_time_limit=6)
                speech = ''
                try:
                    speech = Recognition.recognize_google(audio, language='en-in'), print("Got it! Now to recognize it...")
                    print(f"You said {speech}")
                except sr.WaitTimeoutError:
                    pass
                except sr.RequestError:
                    speak("I am Having Trouble Initiating Your Request")
                except Exception as e:
                    pass
                    print("Oops! Didn't catch that")
                    return "none"
            return speech.lower()
        except sr.WaitTimeoutError:
                pass
        except sr.UnknownValueError:
                    pass
                    speak("I Am Having Trouble Understanding Right Now")