import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("mera naam hemant hai")

def wishMe():
    time = int(datetime.datetime.now().hour)

    if time >= 0 and time < 12:
        speak("Good morning sir")

    elif time >= 12 and time < 16:
        speak("Good afternoon sir")

    elif time >= 16 and time < 21:
        speak("Good evening sir")

    elif time >= 21 and time < 24:
        speak("Good night sir")

    speak("I am zera, how may i help you sir")


def takeCommand():
    '''it takes input form the user and converts audio input to string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("say that again please...")
        speak("say that again please")

    return query


wishMe()

# while True:
query = takeCommand().lower()

if 'wikipedia' in query:
    speak('searching your query in wikipedia.Please wait')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=1)
    speak("According to wikipedia")
    print(results)
    speak(results)

elif 'open youtube' in query:
    webbrowser.open("youtube.com")

elif 'open google' in query:
    speak("sir google opened. what do you want to browse sir")
    browse = takeCommand().lower()
    address = browse.replace("browse", "")
    webbrowser.open(f"https:\\{address}")

elif 'play music' in query:
    musicDirectory = r"E:\NITESH\Songs"
    songs = os.listdir(musicDirectory)
    ranValue = random.randint(0, len(songs))
    print(songs)
    os.startfile(os.path.join(musicDirectory, songs[ranValue]))

elif "the time" in query:
    currentTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"sir the time is {currentTime}")

elif "open vs code" in query:
    os.startfile(
        r"C:\Users\abc\AppData\Local\Programs\Microsoft VS Code\Code.exe")
