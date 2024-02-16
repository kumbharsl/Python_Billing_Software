import os
import tkinter as tk
from tkinter import ttk, messagebox
#from medical import Medical

class SelectFeild:
    def __init__(self):

        #Initalize the Tkinter root window.
        self.select_root=tk.Tk()
        self.select_screen_width=self.select_root.winfo_screenwidth()
        self.select_screen_height=self.select_root.winfo_screenheight()
        self.select_root.title("Billing Software")

        #Creater a main Window.
        self.select_root.geometry(f"{ self.select_screen_width}x{self.select_screen_height}")
        self.select_root.config(bg="#00FFFF")

        


    def setup_ui(self):
        #Create the main background frame
        rgba_color=(222,55,48,255)
        tk_color="#{:02x}{:02x}{:02x}". format(*rgba_color[:3])
        '''self.select_background_frame=tk.Frame(self.select_root, bg="#0A2472", width=self.select_screen_width, height=self.select_screen_height)
        self.select_background_frame.pack()

        #Create the left frame for navigation and buttons
        self.select_left_frame=tk.Frame(self.select_background_frame, bg='#00072D', width=self.select_screen_width //6, height= self.select_screen_height)
        self.select_left_frame.pack(side=tk.LEFT)

        #set up button styling
        style=ttk.Style()
        style.configure("Rounded.TButton",borderwidth=0, relief='flat',background="#BCD2E8", padding=10, font=("Poppins", 12))
        style.map("Rounded.Tbutton", foreground=[('pressed', 'black'),('active', 'white')])

        #Create the font Library button
        self.select_button_label=ttk.Button(self.select_left_frame, text="Medical", style="Rounded.TButton")
        self.select_button_label.pack()
        self.select_button_label.place(x=60, y=350, anchor='nw')
        
        

        #Set up the right frame for Dyanamic content
        rgba_color=(222,55,48,255)
        tk_color="#{:02x}{:02x}{:02x}". format(*rgba_color[:3])
        self.select_right_frame=tk.Frame(self.select_background_frame,bg="#BCD2E8", width=(self.select_screen_width-self.select_screen_width//6),height=self.select_screen_height)
        self.select_right_frame.pack(side=tk.RIGHT)

        

        #Create the font Library button
        self.select_button_label=ttk.Button(self.select_left_frame, text="Grocery", style="Rounded.TButton")
        self.select_button_label.pack()
        self.select_button_label.place(x=60, y=410, anchor='nw')
        
        
        
        #create a "back button"
        self.select_back_button=ttk.Button(self.select_left_frame, text="Back", style="Rounded.TButton", )
        self.select_back_button.pack()
        self.select_back_button.place(x=60, y=470, anchor="nw")
        self.select_root.mainloop()
        '''
        #Set up a lable with welcome text
        self.select_original_label_text="Welcome "
        self.select_right_label=tk.Label(text=self.select_original_label_text, background="#BCD2E8", font=("Poppins", 50,"bold"))
        self.select_right_label.pack()
        self.select_right_label.place(x=500, y=300, anchor='nw')
        self.select_root.mainloop()


obj=SelectFeild()

obj.setup_ui()