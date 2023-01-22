import multiprocessing
import speech_recognition as sr
import pyttsx3
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
voice_default = 0
engine.setProperty('voice', voices[voice_default].id)

r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recoginzing")
        query = r.recognize_google(audio, language='en-in')
        print("User said :", query)

    except Exception as e:
        print(e)
        speak("I ant here that say that again please")
        print("say that again plz ")
        return "none"
    return query


rr = '''“Most people have done all that they’re ever going to do – they raise a family, they earn a living, and then they die.”
That’s what we’re supposed to do, right? Wrong! Life is made for greater things, and you are meant for greater things.
When Les Brown was a child, he was labeled ‘educable mentally retarded’, and until a chance encounter with another teacher, 
he believed that he would amount to nothing. But this one teacher planted the seeds in Les’ head which would blossom and grow,
and eventually make him one of the best motivational speakers of all time.
This speech will give you permission to rise above other people’s opinions, to break free of their
prejudices, and make a success of whatever you do. Watch ‘It’s Not Over Until You Win! Your Dream is Possible’
and take those first steps towards following your passion and making your dream come true.'''

if __name__=='__main__':
    p1 = multiprocessing.Process(target=speak, args=(rr,))
    p2 = multiprocessing.Process(target=takeCommand(),args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()
