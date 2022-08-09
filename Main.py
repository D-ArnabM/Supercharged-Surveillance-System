import tkinter as tk
from tkinter import *
import pandas as pd
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import main_video as mv
from movement import Movement


bgcolor="#d9dadb"
bgcolor1="#41de00"
fgcolor="#349c00"
fgcolor1="#000000"
fgcolor2="#fc0303"


def Home():
        global window
        
        window = tk.Tk()

        window.title("SUPERCHARGED SURVEILLANCE SYSTEM")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="SURVEILLANCE" ,bg=bgcolor  ,fg=fgcolor1  ,width=50  ,height=3,font=('Tekton Pro Ext', 40, 'bold')) 
        message1.place(x=-130, y=20)

        
        def movementprocess():
                mt = Movement()
                mt.movement()
       
        def monitorprocess():
                mv.detect()
        
        

        browse = tk.Button(window, text="Face Recognition With Alert", command=monitorprocess  ,fg=fgcolor1  ,bg=bgcolor1  ,width=30  ,height=2, activebackground = "#fce303" ,font=('Tekton Pro Ext', 15, ' bold '))
        browse.place(x=260, y=300)

        browse = tk.Button(window, text="Movement Detection With Alert", command=movementprocess  ,fg=fgcolor1  ,bg=bgcolor1  ,width=30  ,height=2, activebackground = "#fce303" ,font=('Tekton Pro Ext', 15, ' bold '))
        browse.place(x=700, y=300)

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor1   ,bg="#fce303"  ,width=8  ,height=2, activebackground = "#fce303" ,font=('Tekton Pro Ext', 15, ' bold '))
        quitWindow.place(x=610, y=450)

        window.mainloop()
Home()