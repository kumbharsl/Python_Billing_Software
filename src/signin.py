
import tkinter as tk
from tkinter import*
import os
from tkinter import messagebox, ttk
from billsoft import Bill_App




class SignIn:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
        self.root.geometry(f"{ self.screen_width}x{self.screen_height}")
        self.root.title("Billing Software")
        self.signInUI()        

        

    def signupUi(self):
        self.background_frame.destroy()

        self.background_frame=tk.Frame(self.root, bg="White", width=self.screen_width, height=self.screen_height)
        self.background_frame.pack()

        # insert image
        self.img  = PhotoImage(file='./assets/image/images2.jpg')
        self.img_label=Label(self.background_frame, image=self.img, bg="white")
        self.img_label.place(x=700, y=-100)

        #Create the left frame for navigation and buttons
        self.signin_left_frame=tk.Frame(self.background_frame, bg=self.left_frame_color, width=self.screen_width //2.5, height= self.screen_height)
        self.signin_left_frame.pack(side=tk.LEFT)
        self.signin_left_frame.place(x=0)

        #Create a sign in lable 
        self.sign_in_title = Label(self.signin_left_frame, text="Create account", font=('times new roman', 35, 'bold'), pady=2, bg=self.left_frame_color, fg="White")
        self.sign_in_title.pack()
        self.sign_in_title.place(y=150,relwidth=1)
        


        #Create a signin info  lable
        self.info_label = Label(self.signin_left_frame,bg=self.left_frame_color, height=35, width=50)
        self.info_label.pack()
        self.info_label.place(y=250, x=120)

        #Create a username lable
        self.username_lable=Label(self.info_label, text="Name", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.username_lable.pack()
        self.username_lable.place(x=100)
        
        #Create a username text feild 
        self.enter_username=Entry(self.info_label, width=25)
        self.enter_username.pack()
        self.enter_username.place(x=100,y=30)
        
        #Create a password lable
        self.password_lable=Label(self.info_label, text="Phone number", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.password_lable.pack()
        self.password_lable.place(x=100, y=70)
        
        #Create a password text feild 
        self.enter_password=Entry(self.info_label, width=26)
        self.enter_password.pack()
        self.enter_password.place( x=100,y=100)

        #Create a username lable
        self.username_lable=Label(self.info_label, text="Username", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.username_lable.pack()
        self.username_lable.place(x=100,y=140 )
        
        #Create a username text feild 
        self.enter_username=Entry(self.info_label, width=25)
        self.enter_username.pack()
        self.enter_username.place(x=100,y=170)
        
        #Create a password lable
        self.password_lable=Label(self.info_label, text="Password", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.password_lable.pack()
        self.password_lable.place(x=100, y=210)
        
        #Create a password text feild 
        self.enter_password=Entry(self.info_label, width=26)
        self.enter_password.pack()
        self.enter_password.place( x=100,y=240)
        
        #Create a signInButton
        self.signIn_button = Button(self.info_label,text="Sign Up", bg=self.left_frame_color,fg="White", width=15, font='quiksand 13 bold')
        self.signIn_button.pack()
        self.signIn_button.place(x=100,y=300 )

        #SignUP Lable.
        self.label = Label(self.info_label,text="Already have an account?",fg="white",bg=self.left_frame_color,font=('quiksand',11))
        self.label.place(x=100,y=340)
        
        
        self.signup_button = Button(self.info_label, command=self.signupUi,  text="Sign In", bg=self.left_frame_color,fg="white",border=0, font='quiksand 11 bold')
        self.signup_button.pack()
        self.signup_button.place(x=138,y=364 )



    def mainsignin(self):
        user=self.enter_username.get()
        passe=self.enter_password.get()
        print("In sign")

        if user == "admin" and passe=="1234":
            self.root.destroy()
            app=Bill_App()
            self.root.destroy()

    def signInUI(self):
        self.left_frame_color="#35364b"
         #Create the main background frame
        self.background_frame=tk.Frame(self.root, bg="White", width=self.screen_width, height=self.screen_height)
        self.background_frame.pack()


        # insert image
        self.img  = PhotoImage(file='./assets/image/login image.png')
        self.img_label=Label(self.background_frame, image=self.img, bg="white")
        self.img_label.place(x=700, y=-100)

        #Create the left frame for navigation and buttons
        self.signin_left_frame=tk.Frame(self.background_frame, bg=self.left_frame_color, width=self.screen_width //2.5, height= self.screen_height)
        self.signin_left_frame.pack(side=tk.LEFT)
        self.signin_left_frame.place(x=0)

        #Create a sign in lable 
        self.sign_in_title = Label(self.signin_left_frame, text="Let's sign in ...", font=('times new roman', 35, 'bold'), pady=2, bg=self.left_frame_color, fg="White")
        self.sign_in_title.pack()
        self.sign_in_title.place(y=150,relwidth=1)
        


        #Create a signin info  lable
        self.info_label = Label(self.signin_left_frame,bg=self.left_frame_color, height=35, width=50)
        self.info_label.pack()
        self.info_label.place(y=250, x=120)

        #Create a username lable
        self.username_lable=Label(self.info_label, text="Username", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.username_lable.pack()
        self.username_lable.place(x=100)
        
        #Create a username text feild 
        self.enter_username=Entry(self.info_label, width=25)
        self.enter_username.pack()
        self.enter_username.place(x=100,y=30)
        
        #Create a password lable
        self.password_lable=Label(self.info_label, text="Password", bg=self.left_frame_color, fg="White",font=("quiksand", 13, 'bold'))
        self.password_lable.pack()
        self.password_lable.place(x=100, y=70)
        
        #Create a password text feild 
        self.enter_password=Entry(self.info_label, width=26)
        self.enter_password.pack()
        self.enter_password.place( x=100,y=100)
        
        #Create a signInButton
        self.signIn_button = Button(self.info_label, command=self.mainsignin, text="Sign In", bg=self.left_frame_color,fg="White", width=15, font='quiksand 13 bold')
        self.signIn_button.pack()
        self.signIn_button.place(x=100,y=150 )

        #SignUP Lable.
        self.label = Label(self.info_label,text="Don't have an account?",fg="white",bg=self.left_frame_color,font=('quiksand',11))
        self.label.place(x=100,y=190)
        
        
        self.signup_button = Button(self.info_label, command=self.signupUi,  text="Sign Up", bg=self.left_frame_color,fg="white",border=0, font='quiksand 11 bold')
        self.signup_button.pack()
        self.signup_button.place(x=138,y=210 )
        self.root.mainloop()
        

