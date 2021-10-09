import sys
import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import pywhatkit as kt
import osascript
import face_recognition as fr
import numpy as np
import cv2
import playsound

engine = pyttsx3.init()
engine.setProperty("rate", 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('Recognizing Face! Please wait a Second ')
