from tkinter import *
#from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
import tkinter.font as tkFont

def admin_to_login(root):
    root.destroy()
    from admin_login_page import admin_login_start
    admin_login_start()
    
def user_to_login(root):
    root.destroy()
    from user_loging_page import user_login_start
    user_login_start()
    
def login_home():
    root = Tk()
    root.state("zoomed")
    root.title("Admin main home page")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # img=PhotoImage(file=r'C:\Users\sm21183\Tkinter\bg.jpg')
    # Label(root,image=img).place(x=10,y = 10) 

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
    headingLabel = Label(headingFrame1, text="   Welcome To \n  Bank Of Honeywell", bg='darkred', fg='white', font=('Courier',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    fontStyle = tkFont.Font(family="Lucida Grande", size=18)

    btn1 = Button(root,text="User Login",bg='white',bd = 5, fg='Green', font=fontStyle, command= lambda: user_to_login(root))
    btn1.place(relx=0.5,rely=0.4, relwidth=0.3,relheight=0.1)
        

    btn3 = Button(root,text="Admin Login",bg='white',bd = 5, fg='Green', font=fontStyle, command= lambda: admin_to_login(root))
    btn3.place(relx=0.5,rely=0.6, relwidth=0.3,relheight=0.1)

    root.mainloop()
    
if __name__=="__main__":   
    login_home()