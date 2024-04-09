import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import smtplib

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am champii. please tell me how may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login()


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Listening..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'chrome'in text:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'wikipedia'in text:
        speak("Seaching wikipedia...")
        text = text.replace("wikipedia","")
        results = wikipedia.summary(text, sentences=2)
        speak("According to wikipedia")
        speak(results)
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'spotify' in text:
        b='opening spotify'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://open.spotify.com/')
    if 'brave' in text:
        c = 'opening Brave'
        engine.say(c)
        engine.runAndWait()
        ProgramName = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        subprocess.Popen([ProgramName])
    if 'vscode' in text:
        c = 'opening vscode'
        engine.say(c)
        engine.runAndWait()
        ProgramName = "C:/Users/ghaywatc/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        subprocess.Popen([ProgramName])
    if 'email to chetan' in text:
        try:
            speak("What should I say")
            content = cmd()
            to = "madhurasd20@gmail.com"
            sendEmail(to, content)
            speak("Email has beens sent!")
        except Exception as ex:
            print(ex)
            speak("sorry my bro . I am not able to send this email")
while True:
      wishMe()
      cmd()



