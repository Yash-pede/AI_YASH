import speech_recognition as sr
import pyttsx3
import vosk


engine = pyttsx3.init('sapi5')

r = sr.Recognizer()
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def takecommand():
#     r = sr.Recognizer()
#     vosk.SetLogLevel(-1)
#     with sr.Microphone() as source:
#         print('listning')
#         audio = r.listen(source)
#     try:
#         print('recognizing')
#         query = r.recognize_vosk(audio)
#         star = query.find(":")
#         en = query.find("\'", 7+3)
#         print(query[(star+3):en-2])
#     except:
#         return 'none'
#     return query


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recoginzing")
        query = r.recognize_google(audio, language='en-in', show_all=True)
        query = query['alternative'][0]['transcript']
        print('\n\b', "User said : ", query, '\n')

    except Exception as e:
        if "getaddrinfo failed" in str(e):
            erGoogle_internet = """
            Sir, I am currently unable to connect to the internet.
            Thus switching to offline speech Recognation model.
            This could be a little slow and a bit inaccurate, 
            Plz make sure to connect to the internet ASAP"""
            speak(erGoogle_internet)
            return None
        speak("I ant here that say that again please")
        print("say that again plz ")
    return query


while True:
    speak(takeCommand())
