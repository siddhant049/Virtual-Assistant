import sys
import os
import tkinter
import face_recognition as fr
import numpy as np
import cv2
import playsound
import time
import tkinter as tk
from tkinter import *
from tkmacosx import Button
from tkvideo import tkvideo
from PIL import Image,ImageTk
import imageio
import threading


def commands():
    path = 'images'
    images = []
    myname = []
    mylist = os.listdir(path)
    print(mylist)
    for current_img in mylist:
        current = cv2.imread(f'{path}/{current_img}')
        images.append(current)
        myname.append(os.path.splitext(current_img)[0])
    print(myname)


    def faceencoding(images):
        encodelist = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = fr.face_encodings(img)[0]
            encodelist.append(encode)
        return encodelist


    encodeListUnknown = faceencoding(images)
    recognized = False
    print('All encodings complete')

    cap = cv2.VideoCapture(0)
    os.system('python3 greet.py')

    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = fr.face_locations(faces)
        encodesCurrentFrame = fr.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = fr.compare_faces(encodeListUnknown, encodeFace)
            faceDis = fr.face_distance(encodeListUnknown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                recognized = True
                break
        if recognized:
            # cv2.destroyAllWindows()
            break

        cv2.imshow('recognizing face ', frame)
        if cv2.waitKey(1) == 13:
            break

    cap.release()

    if recognized:
        # window.destroy()
        os.system('python3 greet2.py')
        os.system('python3 Assistant.py')


window = Tk()
file = 'jarvis10.gif'
info=Image.open(file)
frames=info.n_frames
print(frames)

list1=[tk.PhotoImage(file=file,format =f'gif -index {i}') for i in range(frames)]
count=0
# def animation(count):
#     list = list1[count]
#     lbl.configure(image=list)
#     count += 1
#     if count == frames:
#         count=0
#     window.after(60,animation(count))
def update(ind):

    frame = list1[ind]
    ind += 1
    if ind == frames:
        ind = 0
    lbl.configure(image=frame)
    window.after(70, update, ind)


window.title('Identification')
window.geometry("1200x800")
# add widgets here
window.configure(bg='black')

btn = Button(window, text="Identify", bg='#4da6ff' , fg='#171616' , command=commands,borderless=1,height=50,width=200)
btn.place(x=490, y=650)
lbl = tkinter.Label(window,bg='black')
# lbl.config(height=10, width=70)
lbl.place(x=470, y=260)
lbl.pack()
window.after(0, update, 0)
# player = tkvideo("jarvis1.mp4", lbl, loop=1,size=(300,300),)
# player.play()
window.mainloop()

