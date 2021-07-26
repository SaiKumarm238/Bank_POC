from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import tkinter.font as tkFont

from pymysql import cursors
from www_bank_com import login_home
from forgot_password import otp
import pymysql
from tkinter import messagebox
import user_home 

def login_to_admin(root):
    root.destroy()
    from admin_home_page import admin_start
    admin_start()

def user_login(root):
    #root=Tk()
    
    def ok():
           
        uname=ent1.get()
        password=ent2.get()

        if(uname == "" and password == ""):
            messagebox.showinfo("","Blank not allowed")

        else:
            b = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
            mycursor = b.cursor()
            mycursor.execute('select * from bank3 where uid=%s and password=%s', (ent1.get(), ent2.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('error', 'Invalid Username and Password', parent=root)
            else:
                user_home(root)
                mycursor.close()
            # if uname == data_uid and password == data_password:
            #     messagebox.showinfo("","Login sucess")
            #     #login_to_user(root)
            # else:
            #     messagebox.showinfo("","Incorrect username and password")
                
                
    global img
    global ent1
    global ent2
    same=True
    n=0.5

    # Adding a background image
    background_image =Image.open(r"C:\Users\sm21183\Tkinter\bg5.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(500,500,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
   

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="User Login Page", bg='darkred', fg='white', font=('Courier',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    fontStyle = tkFont.Font(family="Lucida Grande", size=18)
    # img=PhotoImage(file='ojas_logo.png')
    # Label(root,image=img).place(x=10,y = 10)
    
    lbl1=Label(root, text='Enter User ID', font=("Lucida Grande", 30),bg='#e68a00')
    lbl1.place(relx=0.4,rely=0.4)

    lbl2=Label(root, text='Password', font=("Lucida Grande", 30), bg='#e68a00')
    lbl2.place(relx=0.4,rely=0.5)
    
    ent1= Entry(root,bg='white',bd = 5)
    ent1.place(relx=0.6,rely=0.4, relwidth=0.2,relheight=0.06)
    
    ent2= Entry(root,bg='white',bd = 5)
    ent2.place(relx=0.6,rely=0.5, relwidth=0.2,relheight=0.06)
    ent2.config(show="*")
    
    btn1 = Button(root,text="Login",bg='white',bd = 5, fg='Green', font=("Lucida Grande", 16),command=ok)
    btn1.place(relx=0.7,rely=0.7, relwidth=0.09,relheight=0.06)
    
    btn2 = Button(root,text="Forgot Password",bg='white',bd = 5, fg='Orange',command= otp, font=("Lucida Grande", 14))
    btn2.place(relx=0.7,rely=0.6, relwidth=0.1,relheight=0.04)
    
    
    btn3 = Button(root,text="Home",bg='white',bd = 5, fg='Orange',command=login_home, font=("Lucida Grande", 14))
    btn3.place(relx=0.89,rely=0.1, relwidth=0.1,relheight=0.04)
    
    root.title('User Login')
    root.state("zoomed")
    root.geometry("800x600+20+20")

    
def user_login_start():
    root = Tk()
    user_login(root)
    root.mainloop()


if '__name__'=='__main__':   
    user_login_start()
    