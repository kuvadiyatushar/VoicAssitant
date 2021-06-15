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

def screenshot():
    img=pyautogui.screenshot()
    img.save("ss.jpg")

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)
newVoiceRate=150
engine.setProperty("rate",newVoiceRate)

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery=psutil.sensors_battery
    speak("battery is at "+battery.percent)

def jokes():
    speak(pyjokes.get_jokes())

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

def sendMail(to,contet):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("kuvadiyatushar2001@gmail.com",'9259252001')
    server.sendmail("kuvadiyatushar2001@gmail.com",to,contet)
    server.close()

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)
        if "time"  in query:
            time()
        elif "date"  in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipidia"  in query:
            speak("searching...")
            query=query.replace('wikipida',"")
            resut=wikipedia.summery(query,sentance=2)
            speak(resut)
        elif "send mail" in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="19itubd001@ddu.ac.in"
                sendMail(to,content)
                speak("Email sent successfull")
            except Exception as e:
                print(e)
                speak("unable to send mail...")
        elif "search in chrome"  in query:
            speak("what should i serach?")
            crompath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            search=takeCommand().lower()
            wb.get(crompath).open_new_tab(search+".com")
        elif "log out" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart"  in query:
            os.system("shutdown /r /t 1")
        elif "play song" in query:
            song_dir="D:\photos"
            sogs=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,sogs[0]))
        elif "remember that" in query:
            speak("what should i remember?")
            data=takeCommand()
            speak("you said me to remember "+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that "+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("screenshot has been taken...")
        elif "CPU"in query:
            cpu()
        elif "jokes" in query:
            jokes()