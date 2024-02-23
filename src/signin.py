import tkinter as tk    
import os
from tkinter import messagebox, ttk
from tkinter import*
from billing import Bill_App
from PIL import ImageTk, Image


class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
        self.root.geometry(f"{ self.screen_width}x{self.screen_height}")
        self.root.title("Welcome in Sign up")
        self.setup_ui()
        

    def setup_ui(self):
        self.signPageColor="#6082B6"
        #set up background frame.
        self.background_frame=tk.Frame(self.root, bg="White", width=self.screen_width, height=self.screen_height)
        self.background_frame.pack()
        self.signinUi()

    def signinUi(self):
        #set up login frame.
        self.signFrame=tk.Frame(self.background_frame, bg=self.signPageColor, width=self.screen_width //2.3, height= self.screen_height )
        self.signFrame.pack(side=tk.LEFT)
        self.signFrame.place(x=0,y=0)

        #login lable
        self.welcome_text=tk.Label(self.signFrame, text="Lets's sign in ...", fg="white" , bg=self.signPageColor, font=('Sofia Pro', 30, 'bold'))
        self.welcome_text.pack()
        self.welcome_text.place(x=160, y=150)

        #username lable
        self.userName=tk.Label(self.signFrame, text="Username", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.userName.pack()
        self.userName.place(x=200, y=230)

        #username TextFeild
        self.username=tk.Entry(self.signFrame,width=35)
        self.username.pack()
        self.username.place(x=200, y=260, anchor='nw')


        #password lable
        self.pas=tk.Label(self.signFrame, text="Password", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.pas.pack()
        self.pas.place(x=200, y=300)

        #password TextFeild
        self.password=tk.Entry(self.signFrame,width=35)
        self.password.pack()
        self.password.place(x=200, y=330, anchor='nw')

        style=ttk.Style()
        style.configure("Rounded.TButton",borderwidth=0, relief='flat',background="#BCD2E8", padding=10, font=("Poppins", 12))
        style.map("Rounded.Tbutton", foreground=[('pressed', 'black'),('active', 'white')])
        #Login button
        self.loginButton=tk.Button(self.signFrame, command=self.signIn,text="Sign In", font=("Sofia Pro", 15, ), width=19, bg='#364275' ,fg='White')
        self.loginButton.pack()
        self.loginButton.place(x=200, y=380)

        #signup lable
        self.signup_lable=Label(self.signFrame, text="Don't have an account?", font=('Poppins', 10,'bold'), fg="white", bg=self.signPageColor)
        self.signup_lable.pack()
        self.signup_lable.place(x=200, y=440)

        #signup button
        self.loginButton=tk.Button(self.signFrame, command=self.signup_UI,text="Sign up", font=("Poppins", 10,'bold' ), border=0, bd=0 ,bg=self.signPageColor ,fg='White')
        self.loginButton.pack()
        self.loginButton.place(x=355, y=439)

        
        
        image = PhotoImage(file="./assets/image/login image.png")
        self.image_lable=tk.Label(self.background_frame, image=image, bg="White")
        self.image_lable.pack()
        self.image_lable.place(x=700, y=-100)
        self.root.mainloop()
    
    def signIn(self):
        
        user=self.username.get()
        passw=self.password.get()

        if user=='':
            messagebox.showerror("404 Error", "Please Enter username")

        elif passw=='':
            messagebox.showerror("404 Error","Enter password")
        elif user=='' and passw=='':
            messagebox.showerror("404 Error", "Please Enter username & password")
            
        else:  
            self.root.destroy()
            app=Bill_App()

    
    def signupValidation(self):
        new_user=self.Enter_name.get()
        new_user_cont=self.Enter_phone.get()
        new_username=self.Enter_username.get()
        new_user_passw=self.Enter_password.get()

        if new_user =="":
            messagebox.showerror("Error", "please enter name ")
        elif  new_user_cont=="" :
            messagebox.showerror("Error", "please enter phone number")
        elif new_username=="":
            messagebox.showerror("Error", "please enter username")
        elif new_user_passw=="":
            messagebox.showerror("Error", "please enter password")
       
        else:
            self.signinUi()
    def signup_UI(self):
         #login lable
        
        self.signFrame.destroy()
        #set up login frame.
        self.signFrame=tk.Frame(self.background_frame, bg=self.signPageColor, width=self.screen_width //2.3, height= self.screen_height )
        self.signFrame.pack(side=tk.LEFT)
        self.signFrame.place(x=0,y=0)

        self.welcome_signup=tk.Label(self.signFrame, text="Create account...", fg="White" , bg=self.signPageColor, font=('Sofia Pro', 30, 'bold'))
        self.welcome_signup.pack()
        self.welcome_signup.place(x=160, y=150)

        #username lable
        self.name=tk.Label(self.signFrame, text="Name", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.name.pack()
        self.name.place(x=200, y=230)

        #username TextFeild
        self.Enter_name=tk.Entry(self.signFrame,width=35, )
        self.Enter_name.pack(padx=40, pady=(20, 50))
        self.Enter_name.place(x=200, y=260, anchor='nw')

        #username lable
        self.phone=tk.Label(self.signFrame, text="Phone number", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.phone.pack()
        self.phone.place(x=200, y=300)

        #username TextFeild
        self.Enter_phone=tk.Entry(self.signFrame,width=35)
        self.Enter_phone.pack()
        self.Enter_phone.place(x=200, y=330, anchor='nw')
        

        #username lable
        self.username=tk.Label(self.signFrame, text="Username", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.username.pack()
        self.username.place(x=200, y=370)

        # userName TextFeild
        self.Enter_username=tk.Entry(self.signFrame,width=35)
        self.Enter_username.pack()
        self.Enter_username.place(x=200, y=400, anchor='nw')

        #password lable
        self.pas=tk.Label(self.signFrame, text="Password", font=('PT Sans', 13), bg=self.signPageColor, fg="white")
        self.pas.pack()
        self.pas.place(x=200, y=440)

        # #password TextFeild
        self.Enter_password=tk.Entry(self.signFrame,width=35)
        self.Enter_password.pack()
        self.Enter_password.place(x=200, y=470, anchor='nw')

       
         #Login button
        self.signupButton=tk.Button(self.signFrame, command=self.signupValidation,text="Sign Up", font=("Sofia Pro", 15, ), width=19, bg='#364275' ,fg='White')
        self.signupButton.pack()
        self.signupButton.place(x=200, y=520)

          #signup lable
        self.signup_lable=Label(self.signFrame, text="Already have an account?", font=('Poppins', 10,'bold'), fg="white", bg=self.signPageColor)
        self.signup_lable.pack()
        self.signup_lable.place(x=200, y=570)

        #  #signup button
        self.loginButton=tk.Button(self.signFrame, command=self.signinUi,text="Sign in", font=("Poppins", 10,'bold' ), border=0, bd=0 ,bg=self.signPageColor ,fg='White')
        self.loginButton.pack()
        self.loginButton.place(x=370, y=570)



obj=Login()