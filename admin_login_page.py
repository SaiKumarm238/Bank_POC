from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image #PIL -> Pillow
import tkinter.font as tkFont
import pymysql

def login_to_admin(root):
    root.destroy()
    from admin_home_page import admin_start
    admin_start()
def closing_admin_page(root):
    root.destroy()
    from www_bank_com import login_home
    login_home()
def admin_login(root):

    def ok():
        uname=ent1.get()
        password=ent2.get()

        if(uname == "" and password == ""):
            messagebox.showinfo("","Blank not allowed")

        else:
            try:
                b = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
                mycursor = b.cursor()
                mycursor.execute("CREATE TABLE if not exists Admin_table(Admin_id varchar(20) primary key,Admin_password varchar(20))")
                mycursor.execute("INSERT INTO Admin_table values('Admin','123')")
                mycursor.execute('select Admin_id,Admin_password from Admin_table where Admin_id=%s and Admin_password=%s', (ent1.get(), ent2.get()))
                row = mycursor.fetchall()
                print(row)
                print("ENter helo")
                admin_id = row[0][0]
                admin_pass = row[0][1]
                if admin_id == ent1.get() and admin_pass == ent2.get():
                    messagebox.showinfo("Success","Login sucess")
                    login_to_admin(root)
                else:
                    messagebox.showinfo("Error","Incorrect username and password")
            except:
                messagebox.showinfo("Error","Incorrect username and password")
    
    global img
    same=True
    n=0.5

    # Adding a background image
    # background_image =Image.open(r"D:\PYTHON CLASS\CODING\POC_2\POC_Banking\poc_update\bg5.jpg")
    # [imageSizeWidth, imageSizeHeight] = background_image.size

    # newImageSizeWidth = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n) 
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n) 
        
    # background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(background_image)
    # Canvas1 = Canvas(root)
    # Canvas1.create_image(500,500,image = img)      
    # Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    # Canvas1.pack(expand=True,fill=BOTH)
    
    
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Admin Login Page", bg='darkred', fg='white', font=('Courier',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    fontStyle = tkFont.Font(family="Lucida Grande", size=18)

    # btn1 = Button(root,text="User Login",bg='white',bd = 5, fg='Green', font=fontStyle, command= lambda: user_to_login(root))
    # btn1.place(relx=0.5,rely=0.4, relwidth=0.3,relheight=0.1)
        

    # btn3 = Button(root,text="Admin Login",bg='white',bd = 5, fg='Green', font=fontStyle, command= lambda: admin_to_login(root))
    # btn3.place(relx=0.5,rely=0.6, relwidth=0.3,relheight=0.1)
    
    global ent1
    global ent2
    
    lbl1=Label(root, text='Enter Admin ID', font=("Lucida Grande", 30))
    lbl1.place(relx=0.4,rely=0.4)

    lbl2=Label(root, text='Password', font=("Lucida Grande", 30))
    lbl2.place(relx=0.4,rely=0.5)
    
    ent1= Entry(root,bg='white',bd = 5)
    ent1.place(relx=0.6,rely=0.4, relwidth=0.2,relheight=0.06)
    
    ent2= Entry(root,bg='white',bd = 5)
    ent2.place(relx=0.6,rely=0.5, relwidth=0.2,relheight=0.06)
    ent2.config(show="*")
    
    btn1 = Button(root,text="Login",bg='white',bd = 5, fg='Green',command=ok, font=("Lucida Grande", 16))
    btn1.place(relx=0.7,rely=0.7, relwidth=0.09,relheight=0.06)
    
    btn2 = Button(root,text="Forgot Password",bg='white',bd = 5, fg='Orange',command=ok, font=("Lucida Grande", 14))
    btn2.place(relx=0.7,rely=0.6, relwidth=0.1,relheight=0.04)
    
    btn3 = Button(root,text="Home",bg='white',bd = 5, fg='Orange',font=("Lucida Grande", 14),command=closing_admin_page)
    btn3.place(relx=0.89,rely=0.1, relwidth=0.1,relheight=0.04)

    root.state("zoomed")
    root.title("Admin Login")
    root.geometry("600x400")
    # img=PhotoImage(file='ojas_logo.png')
    # Label(root,image=img).place(x=10,y = 10)
    #root.bind('<admin_home_page>', admin_home_page)


def admin_login_start():
    root = Tk()
    admin_login(root)
    root.mainloop()


if __name__=="__main__":   
    admin_login_start()
    