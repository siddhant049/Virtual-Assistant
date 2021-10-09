
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('Recognized! Hello Siddhant sir  ')
