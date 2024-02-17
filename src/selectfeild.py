from tkinter import*
import random
import os
from tkinter import messagebox
import tkinter as tk

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
        self.select_root.config(bg="#808080")
        
        
        


    def setup_ui(self):
        bg_color = "#C0C0C0"
        textFeild="#E5E5E5"
        #Create the main background frame
        rgba_color=(222,55,48,255)
        tk_color="#{:02x}{:02x}{:02x}". format(*rgba_color[:3])

        #Create a title bar
        title = Label(text="Billing Software", font=('Arial', 30, 'bold'), pady=2,  bg="#C0C0C0", fg="#000000")
        title.pack(fill=X)

        
        #Entered customer detailes stors in StringVar().
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        #x = random.randint(1000, 9999)
        #elf.bill_no.set(str(x))
        self.search_bill = StringVar()

        #Create a Costomer detail section.
        
        F1 = LabelFrame(self.select_root,text="Customer Details", font=('Rockwell', 15, 'bold'),  fg="#000000", bg="#C0C0C0")
        F1.place(x=0, y=80) 

        #Enter costomer name
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('Rockwell', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, bg=textFeild, font='Rockwell', )
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        #Enter Costomer phone no
        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color, font=('Rockwell', 15, 'bold'))
        cphn_lbl.grid(row=2, column=0, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='Rockwell', bg=textFeild)
        cphn_txt.grid(row=2, column=1, pady=0, padx=5)

        #Bill details
        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('Rockwell', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='Rockwell', bg=textFeild)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        #Search box.
        bil_btn = Button(F1, text="Search",  width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=2, column=5, pady=5, padx=10)

        self.select_root.mainloop()
        '''
        #Set up a lable with welcome text
        self.select_original_label_text="Welcome..."
        self.select_right_label=tk.Label(text=self.select_original_label_text, background="#808080", font=("Poppins", 30,"bold"))
        self.select_right_label.pack()
        self.select_right_label.place(x=10, y=2, anchor='nw')
        #mainloop.loop

        title = Label(text="Billing Software", font=('times new roman', 30, 'bold'), pady=2,  bg="#badc57", fg="#000000")
        title.pack(fill=X)


        F5 = Frame(self.select_root)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.select_root.mainloop()


obj=SelectFeild()
obj.setup_ui()'''