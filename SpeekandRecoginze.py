import pyttsx3
import time
import speech_recognition as sr
import time
import os
import PIL
import serial


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[4].id)

# VOICES
# 4 Zira -- English
# 3 Ravi -- English
# 2 Kalpana -- Hindi
# 1 Hemant -- hindi
# 0 David -- English

voice_default = 0

engine.setProperty('voice', voices[voice_default].id)
r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
# print(rate)


def startUp():
    speak("Hello sir")
    timeNow = time.strftime('%H')
    if (int(timeNow) >= 6 and int(timeNow) < 13):
        speak("Good morning sir, How your day started sir ")
    elif (int(timeNow) >= 13 and int(timeNow) < 20):
        speak("Good afternoon sir, How is your day going sir ")
    else:
        speak("Good night sir just go to sleep, and let me sleep too")

    speak("how can i help you today,Sir")


def startUpShowoff():
    speak("Hello sir")
    timeNow = time.strftime('%H')
    if (int(timeNow) >= 6 and int(timeNow) < 13):
        speak("Good morning sir, How your day started sir ")
    elif (int(timeNow) >= 13 and int(timeNow) < 20):
        speak("Good afternoon sir, How is your day going sir ")
    else:
        speak("Good night sir just go to sleep, and let me sleep too")

    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    time.sleep(0.5)
    speak("आज आप कौनसी आवाज़ सुन्ना चाहेंगे। Ravi। David । Hemant। Kalpana। Ya fir aapki फेवरिट Zira ki ")
    engine.setProperty('voice', voices[0].id)


def takeCommand():
    # Takes input from mic and returns string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recoginzing")
        query = r.recognize_google(audio, language='en-in',show_all=True)
        query = query['alternative'][0]['transcript']
        print('\n\b',"User said : ", query,'\n')

    except Exception as e:
        print(e)
        speak("I ant here that say that again please")
        print("say that again plz ")
        return "none"
    return query


def takeCommandHindi():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        print('Listening ....')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing ...")
            query = r.recognize_google(audio, language='hi-In')
            query = query['alternative'][0]['transcript']
            print('\n\b',"User said : ", query,'\n')
            # for listening the command in indian english

        # handling the exception, so that assistant can
        # ask for telling again the command
        except Exception as e:
            # print(e)
            print("Say that again sir")
            return "None"
        return query

# print('and the name is : ', __name__)


def changeVoices():
    speak("Which voice do you want sir ")
    while True:
        query = takeCommand().lower()
        if ("ravi") in query:
            engine.setProperty('voice', voices[3].id)
            speak("Hello sir i am ravi ")
            break
        elif ("david") in query:
            engine.setProperty('voice', voices[0].id)
            speak("Hello sir i am david")
            break
        elif ("kalpana") in query:
            engine.setProperty("voice", voices[2].id)
            speak("हेलो सर मैं कल्पना")
            break
        elif ("hemant") in query:
            engine.setProperty("voice", voices[1].id)
            speak("हेलो सर मैं हेमंत हू")
            break
        else:
            speak("sir i did not understood which voice you said ")


def screenshot():
    query = None
    while True:
        speak("Ok sir")
        speak("please hold the screen sir ")
        im = PIL.ImageGrab.grab()
        speak(f"screenshot is captured sir, and you can see it now ,do you wanna take another one sir")
        im.show()
        query = takeCommand().lower()
        if not ("yes") in query:
            speak("ok sir now i am redy for another task")
            break


def shutdown():
    query = None
    speak("ok sir shuting down the system")
    speak("say yes to confirm, else say no")
    query = takeCommand().lower()
    if (query == "yes"):
        os.system("shutdown /s /t 1")
    else:
        speak("aborting shutdown sir")


def restart():
    query = None
    speak("ok sir restarting the system")
    speak("say yes to confirm, else say no")
    query = takeCommand().lower()
    if (query == "yes"):
        os.system("shutdown \s \t 1")
    elif not ('yes') in query:
        speak("restart aborted sir")


def loggingut():
    speak("logging out the system sir")
    os.system("shutdown -l")
