import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',180)
engine.setProperty('voice',voices[1].id)

def lis():
    '''
        listens through mic and ret
        urns string
        '''
    r = sr.Recognizer() #function for speech recognition
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1000
        r.pause_threshold=1 #adjusting hearing phase to 1 second
        audio=r.listen(source) #listen fn passed to audio
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print("User:",query)
    except Exception as e:
        #print(e)
        print("Voice not clear,Try speaking again...")
        return "None"
    return query
def speak(audio):
    '''
    speaks string
         '''
    engine.say(audio)
    engine.runAndWait()
def Wishme():
    '''
        greets based on 24 hour time
        '''
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning...")

    elif hour>=12 and hour <=15:
        speak("Good afternoon...")
    else:
        speak("Good evening...")
    speak("I am your voice assistant, how may i help you")
if __name__=="__main__":
    Wishme()
    while True:
        query=lis().lower()
        if "wikipedia" in query or "wiki" in query:
            query=query.replace(wikipedia,"")
            result= wikipedia.summary(query,sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "youtube" in query:
            print("opening youtube")
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif "leetcode" in query:
            print("opening leetcode...")
            speak("opening leetcode")
            webbrowser.open("https://leetcode.com/")
        elif "naruto" in query:
            print("opening naruto...")
            speak("opening naruto")
            webbrowser.open("https://animixplay.to/v1/naruto-shippuden")
        elif "gmail" in query:
            print("Opening gmail...")
            speak("Opening gmail")
            webbrowser.open("gmail.com")
        elif "google" in query:
            print("Opening google...")
            speak("Opening google")
            g="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(g)
        elif "music" in query:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            print("Playing music...")
            speak("Playing music")
        elif "exit" in query or "stop" in query:
            speak("Bye,See you next time")
            break