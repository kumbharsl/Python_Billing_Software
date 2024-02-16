import os
import tkinter as tk
from tkinter import ttk, messagebox

class SelectFeild:
    def __init__(self):

        #Initalize the Tkinter root window.
        self.select_root=tk.Tk()
        self.select_screen_width=self.select_root.winfo_screenwidth()
        self.select_screen_height=self.select_root.winfo_screenheight()

        #Creater a main Window.
        self.select_root.geometry(f"{ self.select_screen_width}x{self.select_screen_height}")
        self.select_root.config(bg="#00FFFF")
        self.select_root.mainloop()

obj=SelectFeild()