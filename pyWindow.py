#!/usr/bin/env python
from Tkinter import *

def changeText(event):
	data = entryData.get()
	textBox.configure(text=data )

#root window
root = Tk()
root.minsize(300,300)
root.geometry("500x300")
#Frames
topFrame = Frame(root)
topFrame.pack()

#Input field
entryData = Entry(topFrame)
entryData.pack(side=LEFT)
#Button
entryBtn = Button(topFrame, text="Add")
entryBtn.bind("<Button-1>", changeText)
entryBtn.pack(side=LEFT)
#textbox
textBox = Label(root)
textBox.pack()


root.mainloop()



