from tkinter import *
from updating_user_details import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
import tkinter.font as tkFont
import pymysql


def login_to_admin(root):
    root.destroy()
    from admin_home_page import admin_start
    admin_start()

def update_user():
    root=Tk()
    root.configure(bg='#e68a00')
    root.state("zoomed")
    root.title("User Update and Delete")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Customer=StringVar()
    
    # global img
    # same=True
    # n=0.5

    # # Adding a background image
    # background_image =Image.open(r"C:\Users\sm21183\Tkinter\bg5.jpg")
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


    # bg_img=PhotoImage(file=r'C:\Users\sm21183\Tkinter\bg.jpg')
    # Label(root,image=bg_img).place(x=10,y = 10)  
    # global bg_img
    # same=True
    # n=1.75

    # # Adding a background image
    # background_image1 =Image.open(r"C:\Users\sm21183\Tkinter\bank.png")
    # [imageSizeWidth, imageSizeHeight] = background_image1.size

    # newImageSizeWidth1 = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n) 
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n) 
        
    # background_image1 = background_image1.resize((newImageSizeWidth1,newImageSizeHeight),Image.ANTIALIAS)
    # bg_img = ImageTk.PhotoImage(background_image1)
    # Canvas1 = Canvas(root)
    # Canvas1.create_image(600,500,image = bg_img)      
    # Canvas1.config(bg="white",width = newImageSizeWidth1, height = newImageSizeHeight)
    # Canvas1.pack(expand=True,fill=BOTH)

    def update():
        if t1.get()=="":
            messagebox.showinfo("error","Field cannot be empty")
        else:
            try:
                b = pymysql.connect(host='localhost',user='root',password='root')
                mycursor = b.cursor()
                mycursor.execute("USE bank_of_ojas")
                mycursor.execute("SELECT Aadhar FROM bank3 WHERE Aadhar='"+t1.get()+"'")
                check = mycursor.fetchall()
                adhar_check = check[0][0]
                if int(t1.get()) == adhar_check:
                   
                    mycursor.execute("SELECT * FROM bank3 WHERE Aadhar='"+t1.get()+"'")
                                     
                    user_adhar = int(t1.get())
                    fields = mycursor.fetchall()
                    for i in fields:
                        update_entry(user_adhar,i)                          
                    b.commit()

                    #MessageBox.showinfo("succes","updated successfully")
                
            except TypeError:
                messagebox.showinfo("Error","Invalid aadhar number")

    
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="User Update Page", bg='darkred', fg='white', font=('Courier',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    fontStyle = tkFont.Font(family="Lucida Grande", size=18)


    # btn1 = Button(root,text="Create User",bg='white',bd = 5, fg='Green', font=fontStyle, command=reg)
    # btn1.place(relx=0.5,rely=0.4, relwidth=0.3,relheight=0.1)
    lbl1=Label(root, text='Enter User ID', font=("Lucida Grande", 30))
    lbl1.place(relx=0.3,rely=0.4)
    
    global t1
    t1= Entry(root,bg='white',bd = 5,textvar=Customer)
    t1.place(relx=0.5,rely=0.4, relwidth=0.3,relheight=0.08)
    
    btn1 = Button(root,text="Update User",bg='white',bd = 5, fg='Orange', font=("Lucida Grande", 16),command=update)
    btn1.place(relx=0.7,rely=0.6, relwidth=0.09,relheight=0.06)
        

        
    # btn2 = Button(root,text="Delete User",bg='white',bd = 5, fg='red', font=fontStyle)
    # btn2.place(relx=0.5,rely=0.6, relwidth=0.09,relheight=0.06)



    # btn3 = Button(root,text="Back To Home",bg='red',bd = 5, fg='white', font=("Lucida Grande", 15), command=login_to_admin)
    # btn3.place(relx=0.89,rely=0.09, relwidth=0.1,relheight=0.050)
    root.mainloop()


if '__name'=='__main__':
    update_user()


# def update_page():
#     root=Tk()
#     update_user(root)
#     root.mainloop()
    

# if __name__=="__main__":   
#     update_page()
    
    
    
    

