'''
A basic GUI app.
'''

from tkinter import *

root = Tk()
theLabel = Label(root, text = 'This is my first GUI app')
theLabel.pack() # This actually puts the text in the GUI window.
root.mainloop() # This will keep the program running until we close the window manually.