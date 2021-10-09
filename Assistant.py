import tkinter

import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import pywhatkit as kt
import osascript
import tkinter as tk
from tkinter import *
from PIL import Image
from tkmacosx import Button


window = Tk()
# Main code starts
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices)
# engine.setProperty('voice',voices[16].id)
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    h = int(datetime.datetime.now().hour)
    print(h)
    if h >= 4 and h < 12:
        speak("Good Morning ! ")
    elif h>=0 and h<=4:
        speak('Good Night sir ! You should by this sleeping this time! Anyways ')
    elif h >= 12 and h < 17:
        speak("Good Afternoon ! ")
    else:
        speak("Good Evening ")

    speak("I am jarvis your assistant!")


def takecommand():
    # takes microphone input and return string as output
    r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source)
    #     r.adjust_for_ambient_noise(source, duration=0.2)
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"

    return query


def startcommand():
    wishme()
    x = 2
    while x > 1:
        query = takecommand().lower()

        if 'jarvis' in query or 'Jarvis' in query:
            # speak('Hello and Ready sir')

            while 1:
                if 1:
                    # query = takecommand().lower()
                    if 'how are you' in query:
                        speak(
                            'I am good sir! Thanks for asking. Hope you are well too. Please tell me how may i help you')
                        query = takecommand().lower()
                        continue
                    elif 'thank you' in query or 'thankyou' in query:
                        speak('No problem sir! I am here for you sir! Please  call me again for any help')
                        break

                    elif 'open whatsapp' in query:
                        speak('Opening whatsapp sir')
                        os.system("open /Applications/WhatsApp.app")
                        break

                    elif 'open vs code' in query:
                        speak('Opening visual studio code sir ')
                        os.system("open /Applications/Visual\ Studio\ Code.app")
                        break

                    elif 'open Pycharm' in query:
                        speak('Opening Pycharm  sir ')
                        os.system("open /Applications/PyCharm\ CE.app")
                        break

                    elif 'open chrome' in query:
                        speak('Opening chorme sir')
                        os.system("open /Applications/Google\ Chrome.app")
                        break

                    elif 'open youtube' in query:
                        speak('Sure sir! Opening sir')
                        webbrowser.open('https://www.youtube.com/')
                        break

                    elif 'open new tab' in query:
                        webbrowser.open_new_tab('https://www.google.co.in/')
                        break

                    elif 'open discord' in query:
                        speak('opening Discord sir')
                        os.system("open /Applications/Discord.app")
                        break

                    elif 'give me something to write my notes on' in query:
                        speak('Opening word sir')
                        os.system("open /Applications/Microsoft\ Word.app")
                        break

                    elif 'it is my class time' in query:
                        speak('Opening M S Teams sir')
                        os.system("open /Applications/Microsoft\ Teams.app")
                        break

                    elif 'open my facebook account' in query:
                        speak('Sure sir')
                        webbrowser.open("https://www.facebook.com/")
                        break

                    elif 'want to see my professional account' in query:
                        speak('opening sir')
                        webbrowser.open_new_tab("https://www.linkedin.com/feed/")
                        break

                    # elif 'open settings' in query:
                    #     speak('opening sir')
                    #     # os.system("open /Applications/System\ Preferences.app")
                    #     os.system("open /Applications/System\ Preferences.app")

                    # elif 'spotlight search' in query:
                    #     speak('sure sir')
                    #     keyboard=Controller()
                    #     key="command"+" "
                    #     keyboard.press(key)
                    #     keyboard.release(key)

                    elif 'volume mute' in query:
                        speak('Muting the volume sir ')
                        target_volume = 0
                        vol = "set volume output volume " + str(0)
                        osascript.osascript(vol)
                        break

                    elif 'volume 10' in query:
                        target_volume = 10
                        vol = "set volume output volume " + str(10)
                        osascript.osascript(vol)
                        speak('volume 10 ')
                        break

                    elif 'volume 25' in query:
                        target_volume = 25
                        vol = "set volume output volume " + str(25)
                        osascript.osascript(vol)
                        speak('volume 25')
                        break

                    elif 'volume 50' in query:
                        target_volume = 50
                        vol = "set volume output volume " + str(50)
                        osascript.osascript(vol)
                        speak('volume 50')
                        break

                    elif 'volume 75' in query:
                        target_volume = 75
                        vol = "set volume output volume " + str(75)
                        speak('volume now is 75 sir!')
                        osascript.osascript(vol)
                        speak('volume 75')
                        break

                    elif 'volume 90' in query:
                        target_volume = 90
                        vol = "set volume output volume " + str(90)
                        osascript.osascript(vol)
                        speak('volume now is 90 sir!')
                        break

                    elif 'volume full' in query:
                        speak('not gonna do that sir')
                        target_volume = 100
                        vol = "set volume output volume " + str(100)
                        speak('volume now is 100 sir!')
                        osascript.osascript(vol)
                        break

                    elif 'want to search something on google' in query:
                        speak('what do you want to search sir?')
                        ques = takecommand().lower()
                        kt.search(ques)
                        break

                    elif 'play song a from youtube' in query:
                        speak('which song you want me to play sir?')
                        ques = takecommand().lower()
                        kt.playonyt(f"{ques}")
                        if 'then sleep' in query:
                            speak('Going to sleep mode sir')
                            break

                    elif 'send message on whatsapp' in query:
                        speak('whom do you want to message sir ?')
                        recipent = takecommand().lower()
                        speak('what is the message sir?')
                        message = takecommand().lower()
                        # with Whatsapp() as bot:
                        #     bot.send(f"{recipent}", f"{message}")

                    elif 'sleep jarvis' in query or 'jarvis sleep' in query:
                        speak('Good bye sir')
                        break

                    elif 'shut down' in query or 'shutdown' in query:
                        speak('Good bye sir! Meet you soon ')
                        x = 0
                        sys.exit()
                    elif 'jarvis' in query:
                        speak('Yes sir? Please tell me what to do? ')
                        query = takecommand().lower()
                        continue


file = 'jarvis6.gif'
info=Image.open(file)
frames=info.n_frames
print(frames)

list1=[tk.PhotoImage(file=file,format =f'gif -index {i}') for i in range(frames)]
count=0
def update(ind):

    frame = list1[ind]
    ind += 1
    if ind == frames:
        ind = 0
    lbl.configure(image=frame)
    window.after(50, update, ind)

# add widgets here
window.configure(bg='black')
btn=Button(window, text="TERMINATE", bg='#ff8080',fg='#171616',command=window.destroy,borderless=1,height=50,width=200)
btn.place(x=650, y=650)
btn=Button(window, text="START", bg='#4da6ff',fg='#171616',command=startcommand,borderless=1,height=50,width=200)
btn.place(x=350, y=650)
lbl=tkinter.Label(window,bg='black')
# lbl.config(height=100, width=200)
lbl.place(x=350, y=50)
window.title('J.A.R.V.I.S')
window.geometry("1200x800")
window.after(0, update, 0)
window.mainloop()
