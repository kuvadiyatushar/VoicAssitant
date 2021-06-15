import datetime
import wikipedia
import smtplib
import pyttsx3
import  webbrowser as wb
import speech_recognition as sr
import os
import pyautogui
import psutil
import pyjokes


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)
newVoiceRate=150
engine.setProperty("rate",newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime('%I:%M:%S')
    speak(time)

def date():
    year=int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternood")
    elif hour>=18 and hour<=24:
        speak("good Evening")
    else:
        speak("good night")

    speak("Siri at your service, how can i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogitioizing...")
        query=r.recognize_google(audio,language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("sorry i can't understand your voice, try again...")
        return "None"
    return query
takeCommand()