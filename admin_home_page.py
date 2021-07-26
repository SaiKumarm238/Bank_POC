from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
import tkinter.font as tkFont
from User_Creation import user_create
from admin_login_page import admin_login
from update_user import update_user
from delete_user import delete_user

def admin_to_login(root):
    root.destroy()
    from admin_login_page import admin_login_start
    admin_login_start()
    

def admin_home_page_1(root):
    
    root.state("zoomed")
    root.title("Admin main home page")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # img=PhotoImage(file=r'C:\Users\sm21183\Tkinter\bg.jpg')
    # Label(root,image=img).place(x=10,y = 10) 
    global img
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
    headingLabel = Label(headingFrame1, text="   Welcome To \n  Bank Of Honeywell", bg='darkred', fg='white', font=('Courier',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    fontStyle = tkFont.Font(family="Lucida Grande", size=18)

    btn1 = Button(root,text="Create User",bg='white',bd = 5, fg='Green', font=fontStyle, command=user_create)
    btn1.place(relx=0.5,rely=0.4, relwidth=0.3,relheight=0.1)
    
    btn2 = Button(root,text="Update User",bg='white',bd = 5, fg='Orange', font=fontStyle, command=update_user)
    btn2.place(relx=0.5,rely=0.6, relwidth=0.3,relheight=0.1)

    btn3 = Button(root,text="Delete User",bg='white',bd = 5, fg='red', font=fontStyle, command=delete_user)
    btn3.place(relx=0.5,rely=0.8, relwidth=0.3,relheight=0.1)
  
    btn4 = Button(root,text="Logout",bg='red',bd = 5, fg='white', font=fontStyle, command=lambda: admin_to_login(root))
    btn4.place(relx=0.89,rely=0.09, relwidth=0.1,relheight=0.050)
    #btn4.bind('<Return>',main_menu2)
    # messagebox.showinfo("","logout")
    # root.destroy()    
    
def admin_start():
    
    root = Tk()
    admin_home_page_1(root)
    root.mainloop()
    

if __name__=="__main__":   
    admin_start()

   
        
    
   

