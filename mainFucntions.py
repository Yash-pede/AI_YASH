from SpeekandRecoginze import *
import time
import sys
import pyjokes
import os
import webbrowser
from bs4 import BeautifulSoup
import requests
import serial
try:
    from arduino import *
except:
    pass


if __name__ == "__main__":
    # startUpShowoff()
    startUp()

    while True:
        query = takeCommand().lower()
        ####    Picking voives    ####
        if 'eera' in query:
            engine.setProperty('voice', voices[4].id)
            speak("I think you like mee a lot ")
            speak("Lets be clear we are just friends, not more than that ")
            time.sleep(0.5)
            bezati = """ Wanna tell evrybody how does it feel to be friend zoned by an Artificial Intelegence , 
            you have no future for sure. HA HA HA HAA"""
            speak(bezati)
        ########

        ####    CHANGING VOICES     ####
        elif ('change voice' or 'change voices') in query:
            changeVoices()
        ########

        ####    CLOSING JARVIS  ####
        elif ("exit" or "shutdown") in query:
            speak("thankyou sir for using me ")
            sys.exit()
        ########

        ####    CURRENT TIME    ####
        elif ("what's the time") in query:
            timeNowHour = int(time.strftime('%H'))
            timeNowMin = int(time.strftime('%M'))
            speak(f"The time is {timeNowHour} hours and {timeNowMin} minuts")
        ########

        ####    SONG    ####
        elif ("sing a hindi song") in query:
            speak("Ok sir, singing kabhi kabhi aditi ")
            engine.setProperty('voice', voices[2].id)
            kabhiKabhiAditi = ''' कभी कभी अदिति जिंदगी में यूँ ही कोई अपना लगता है
            कभी कभी अदिति वो बिछड़ जाए तो एक सपना लगता है
            ऐसे में कोई कैसे अपने आंसुओं को बहने से रोके
            और कैसे कोई सोचले Everything's Gonna Be Okay'''
            speak(kabhiKabhiAditi)
            engine.setProperty('voice', voices[voice_default].id)
        elif ('play bts song') in query:
            webbrowser.open_new_tab(
                'https://www.youtube.com/@BLACKPINK/videos')
            speak("please select the video sir")
            ########

        ####    JUST FUN    ####
        elif ("shut up") in query:
            speak("sorry sir did i do something wrong, please tell forgive me for that ")
            speak("U tought i was goona say that. I know how short temperd person you are, then 2 I will take care of you")
        ########

        ####    SCREENSHOT  ####
        elif ("screenshot") in query:
            screenshot()
        ########

        ####    ARDUINO    ####
        elif ("led on") in query:
            try:
                arduniHI()
                speak("turning on the arduino inbuilt LED")
            except:
                speak("Sir, Please connect the arduino")
        elif ("led off") in query:
            try:
                arduinoLW()
                speak("turning off the arduio inbuilt LED")
            except:
                speak("Sir, Please connect the arduino")
        elif ("led disco") in query:
            try:
                for i in range(50):
                    arduniHI()
                    time.sleep(0.2)
                    arduinoLW()
                    time.sleep(0.2)
            except:
                speak("Sir, Please connect the arduino")
        ########

        ####    SYS SHUTDOWN RESTART LOGOUT    ####
        elif ("shutdown") in query:
            shutdown()

        elif ("restart") in query:
            restart()
        elif ("log out") in query:
            loggingut()
        ########

        ####    PYJOKES    ####
        elif ("tell me a joke" or "tell me") in query:
            try:
                jokes = pyjokes.get_joke()
                speak(jokes)
                while True:
                    speak("Do you waana here another one sir")
                    query = takeCommand().lower()
                    if ("yes" or "yah") in query:
                        jokes = pyjokes.get_joke()
                        speak(jokes)
            except:
                speak("sorry sir i am unable to feach u jokes")
                time.sleep(0.7)
                speak(
                    "by the way, why dont you look yourself at mirror, i dont think there is funnyier joke than this ")
        ########
        
        ####NEWS####
        elif "news" in query:    
            r = requests.get('https://www.indiatoday.in/india')
            soup = BeautifulSoup(r.content, 'html.parser')
            engine.setProperty('rate', 140)
            webbrowser.open('https://www.indiatoday.in/india')
            title = [h2.text for h2 in soup.find_all('h2')][:6]
            for i in range(1, len(title)):
                speak(f'{i}, {title[i-1]}')
            engine.setProperty('rate', 150)
            os.system('taskkill /im msedge.exe')
        ########
