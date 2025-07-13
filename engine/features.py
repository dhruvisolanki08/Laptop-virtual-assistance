import fnmatch
import re
import struct
import webbrowser
from playsound import playsound
import eel
import pyaudio
from engine.command import *
from engine.config import *
import os
import pywhatkit as kit
import sqlite3
import pvporcupine
from engine.helper import *
import time

#Playing Assistent sound function

@eel.expose
def playAssistantSound():
    music_dir = "C:\\Users\\ashar\\OneDrive\\Desktop\\Major_Minor\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


con = sqlite3.connect("sooha.db")
cursor = con.cursor()


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+ query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+ query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+ query)
                    try:
                        os.system('start '+ query)
                    except:
                        speak("not found")
        except:
            speak("something went wrong")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube.")
    kit.playonyt(search_term)


def Search(query):
    query = query.replace("search", "")
    
    if "file" in query:
        search_type = 'file'
        print("file")
    elif "folder" in query:
        search_type = 'folder'
        print("folder")
    else:
        search_type = 'file'
    
    query = query.replace(" ", "")
    query = query.replace("folder", "")
    query = query.replace("file", "")

    speak("Searching " + query)
    item = query

    found_items = find_items_by_name(item, search_type)
    message= ""

# Print the results
    if found_items:
        speak("Found the following items")
        message += "Found the following items:"
        for item in found_items:
            message += item + "\n"

    else:
        message = "No matching items found."
    
    eel.DisplayMessage(message)
    time.sleep(3)
    eel.receiverText(message)
    

def database():
    speak("Showing data in the chatbox.")
    from engine.data import showdata
    showdata()

    


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()







