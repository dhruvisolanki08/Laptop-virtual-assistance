import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
    eel.DisplayMessage("")
    


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(3)
       
        
    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takeCommand()
        print(query)
        eel.senderText(query)
    else:
        query = str.lower(message)
        eel.senderText(query)
        
    
    try:    
        
        if "search" in query:
            from engine.features import Search
            Search(query)

        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "show database" in query:
            from engine.features import database
            database()
            eel.ShowHood()
        
        elif "add path" or "add url" or "delete path" or "delete url" in query:
            spl = query.split()
            method = spl[0]
            if method == "add":
                from engine.db import insert_command
                insert_command(query)
            elif method == "delete":
                from engine.db import delete_command
                delete_command(query)
            else:
                from engine.chatbot import Chat
                Chat(query)
        
        eel.ShowHood()
    
    except:
        print("Error")
        eel.ShowHood()
