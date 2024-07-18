'''
For Python Application with GUIs
Dockerization - Containerization, Compatibility
Docker image - Build a container using this
It will include interdependent classes, modules, libraries
Packages, Environment variables etc
Container - Environment, Application
For GUI apps, connect docker container to a display
'''

import tkinter as tk 
from tkinter.messagebox import showinfo

root = tk.Tk()

def show_message():
    showinfo('Message', 'Hello, World!') # (Title, Message)

btn = tk.Button(root, text = 'Click me!', command=show_message)
btn.pack()

root.mainloop()