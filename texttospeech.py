import tkinter as tk 
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from gtts import gTTS
from playsound import playsound

root = tk.Tk()
frame = tk.Frame(root) 
frame.pack()

filename = 0

def browse():
	global filename
	filename = askopenfilename()



def play():
	global filename
	data = open(filename,"r")
	text = data.read()
	lang='en'
	sound = gTTS(text,lang,slow=False)
	sound.save('lol.mp3')
	playsound('lol.mp3')

button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
button1 = tk.Button(frame,text="BROWSE",command=browse)
button1.pack(side=tk.LEFT)
button2 = tk.Button(frame,text="play",command=play)
button2.pack(side=tk.LEFT)

root.mainloop()