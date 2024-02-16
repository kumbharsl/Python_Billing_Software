import tkinter as tk 
import os 
from tkinter import ttk, messagebox

class Welcome:
    def __init__(self):
        #Initialize the Tkinter root Window
        self.welcome_root=tk.Tk()
        self.welcome_screen_width=self.welcome_root.winfo_screenwidth()
        self.welcome_screen_height=self.welcome_root.winfo_screenheight()
        self.welcome_root.title("Billing Software")

        #Set up the size of window,
        self.welcome_root.geometry(f"{self.welcome_screen_width}x{self.welcome_screen_height}")
        self.welcome_root.config(bg="#192f43")
        
        #Create a lable Text 
        #self.welcome_lable_text="Welcome..."
        self.welcome_lable=tk.Label(text="Welcome...", background="#192f43", fg="#FFFFFF", font=("Poppins",50,"bold"))
        self.welcome_lable.pack()
        self.welcome_lable.place(x=600,y=300, anchor="nw")
        
       

        self.welcome_root.mainloop()

obj=Welcome()