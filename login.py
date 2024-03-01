import ast
from tkinter  import *
from tkinter import messagebox
from google.cloud import firestore
import json
from billing import Bill_App


root =Tk()
root.title('Billing Software')
select_screen_width=root.winfo_screenwidth()
select_screen_height=root.winfo_screenheight()
root.geometry(f"{ select_screen_width}x{select_screen_height}")
#root.geometry( '1000x500+100+50' )
root.configure(bg= 'white')
signin=True
additional_widgets=[]

# user.insert(0,"Username")


def signup():
    screen=Toplevel(root)
    screen.title("App")
    # screen_width=root.winfo_screenwidth()
    # screen_height=root.winfo_screenheight()
    # root.geometry(f"{ screen_width}x{screen_height}")
    screen.geometry('1250x700+100+50' )
    screen.config(bg='white')
    signup()
    
    
    def signup():
        username=user.get()
        password=code.get()
        conform_password=code1.get()
        
        if password == conform_password:
            try:
                file=open('my_projects/Userdata/userInfo.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                
                dict2= {username:password}
                r.update(dict2)
                file.turncate(0)
                file.close()
                
                file=open('my_projects/Userdata/userInfo.txt','w')
                w=file.write(str(r))
                
                messagebox.showinfo('Signup','Sucessfully sign up')
                
            except:
                file = open('my_projects/Userdata/userInfo.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        
    frame1=Frame(root,width=500,height=350,bg="white")

    heading1 = Label(frame1,text= "SIGN UP",font=("Helvetica",20,"bold"),fg="#57a1f8" , bg="white")
    heading1.place(x=100,y=5)
        
    username=user.get()
    password=code.get()
    conform_password=code1.get()
        
    if password == conform_password:
        try:
            file=open('my_projects/Userdata/userInfo.txt','w+')
            d=file.read()
            r=ast.literal_eval(d)
                
            dict2= {username:password}
            r.update(dict2)
            file.turncate(0)
            file.close()
                
            file=open('my_projects/Userdata/userInfo.txt','w')
            w=file.write(str(r))
                
            messagebox.showinfo('Signup','Sucessfully sign up')
                
        except:
            file = open('my_projects/Userdata/userInfo.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()
        
    else:
        messagebox.showerror( "Invalid", "Password does not match"  )  
    
    img  = PhotoImage(file= './assets/image/login.png')
    Label(screen, image=img,bg='white').place(x=50,y=200)
    
    frame=Frame(frame1,width=500,height=450,bg="white")
    frame.place(x=550, y=70)

    heading = Label(frame1,text= "SIGN UP",font=("Helvetica",20,"bold"),fg="#57a1f8" , bg="white")
    heading.place(x=100,y=5)
    
        #-------------------------------------------------------------------------------------------------------------
        #creat user name input
    def on_enter():
        user.delete(0,'end')
        
    def on_leave():
        name=user.get()
        if name=='':
            user.insert(0,'Username')
                
    user = Entry(frame1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',10))
    user.place(x=30,y=300)
    # user.insert(0,"Username")
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=110)
        
    #-------------------------------------------------------------------------------------------------------------
    #create password input
    def on_enter():
        code.delete(0,'end')
        
    def on_leave():
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    # code = Entry(frame1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,"Password")
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    Frame(frame1,width=295,height=2,bg="black").place(x=25,y=180)
    
    #-------------------------------------------------------------------------------------------------------------
    #create confirm password input
    def on_enter():
        code1.delete(0,'end')
        
    def on_leave():
        name=code1.get()
        if name=='':
            code1.insert(0,'Password  Confirm')
        
    code1 = Entry(frame1,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code1.place(x=30,y=220)
    code1.insert(0,"Password Confirm")
    code1.bind('<FocusIn>',on_enter)
    code1.bind('<FocusOut>',on_leave)
    Frame(frame1,width=295,height=2,bg="black").place(x=25,y=250)
        
            #------------------------------------------------------------------------------------------------------------------
    Button(frame1,width=39,pady=7,text='Sign up', bg='#57a1f8',fg='white',border=0).place(x=35,y=274)
    label = Label(frame1,text="I have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=320)
        
    signin = Button(frame1,width=6,text='Sign in', border=0, bg= 'white',cursor='hand2',fg='#57a1f8',command=signin)
    signin.place(x=190,y=320)
    signin=False

    
    

    screen.mainloop()
#-----------------------------------------------------------------------------------------------------------------
def signin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='1234':
        root.destroy()
        app=Bill_App()
        

    
    elif username != 'admin' and password !='1234':
        messagebox.showerror('Invalid','Invalid username and password')
        
    elif password != '1234':
        messagebox.showerror('Invalid','Invalid password')
    
    elif username != 'admin':
        messagebox.showerror('Invalid','Invalid username')

img  = PhotoImage(file='./assets/image/image2.jpg')
Label(root, image=img,bg='#57a1f8').place(x=280,y=200)

frame=Frame(root,width=500,height=350,bg="#57a1f8")
frame.place(x=750, y=200)

heading = Label(frame,text= "SIGN IN",font=("Helvetica",20,"bold"),fg="#57a1f8" , bg="white")
heading.place(x=100,y=5)

#-------------------------------------------------------------------------------------------------------------
def on_enter():
    user.delete(0,'end')
    
def on_leave():
    name=user.get()
    if name=='':
        user.insert(0,'Username')
    
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")   
user.bind('<FocusIn>',on_enter) 
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=110)
#-------------------------------------------------------------------------------------------------------------
def on_enter():
    code.delete(0,'end')
    
def on_leave():
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,"Password")   
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=180)

    #-------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up', border=0, bg= 'white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)


root.mainloop()