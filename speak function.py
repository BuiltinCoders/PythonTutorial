from win32com.client import Dispatch
import time

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.speak(str)
    
for i in range(10):
    for i in range(10):
        speak(f"{i+1}")
        # speak("Kartiik")
        time.sleep(2)