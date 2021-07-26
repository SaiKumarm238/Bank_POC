from tkinter import *
import pymysql
#import os
#from PIL import ImageTk,Image
import tkinter.messagebox as MessageBox

def update_entry(user_adhar,*n):
    #global user_adhar
    global Fname
    global Lname
    global gender
    global DOB
    global Phno
    global Email
    global Aadhar
    global Address
    global Pan_number
    global Father_name
    global Mother_name
    global User_id
    global User_Password

    def updating_user_data():
        b = pymysql.connect(host='localhost',user='root',password='root')
        mycursor = b.cursor()
        mycursor.execute("USE bank_of_ojas")
        mycursor.execute("UPDATE bank3 SET Fname='"+Fname.get()+"',Lname='"+Lname.get()+"',Gender='"+gender.get()+"',DOB='"+DOB.get()+"',Phno='"+Phno.get()+"',Email='"+Email.get()+"',Aadhar='"+Aadhar.get()+"',Address='"+Address.get()+"',Pan='"+Pan_number.get()+"',Father='"+Father_name.get()+"',Mother='"+Mother_name.get()+"',Uid='"+User_id.get()+"',Password='"+User_Password.get()+"' WHERE Aadhar='"+str(user_adhar)+"'")
        b.commit()

        MessageBox.showinfo("success","updated successfully")

    
    root = Tk()
    root.state("zoomed")
    root.configure(bg='#e68a00')
    root.geometry('500x1000')
    root.title("Registration Form")
    #temporary=StringVar()

    label_0 = Label(root, text="Update user details",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)


    label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    Fname = Entry(root)
    Fname.insert(0,n[0][0])
    Fname.place(x=240,y=130)

    label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)

    Lname = Entry(root)
    Lname.insert(0,n[0][1])
    Lname.place(x=240,y=180)
        

    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)

        
    gender = Entry(root)
    gender.insert(0,n[0][2])
    gender.place(x=900,y=230)

    label_4 = Label(root, text="Date of Birth",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)


    DOB = Entry(root)
    DOB.insert(0,n[0][3])
    DOB.place(x=240,y=280)


    label_5 = Label(root, text="Phone Number",width=20,font=("bold", 10))
    label_5.place(x=72,y=330)


    Phno = Entry(root)
    Phno.insert(0,n[0][4])
    Phno.place(x=240,y=330)


    label_6 = Label(root, text="Email",width=20,font=("bold", 10))
    label_6.place(x=74,y=380)


    Email = Entry(root)
    Email.insert(0,n[0][5])
    Email.place(x=240,y=380)
    
    label_7 = Label(root, text="Aadhar Number",width=20,font=("bold", 10))
    label_7.place(x=74,y=430)


    Aadhar = Entry(root)
    Aadhar.insert(0,n[0][6])
    Aadhar.place(x=240,y=430)

    label_8 = Label(root, text="Address",width=20,font=("bold", 10))
    label_8.place(x=74,y=480)


    Address = Entry(root)

    Address.insert(0,n[0][7])
    Address.place(x=240,y=480)

    label_9 = Label(root, text="Pan Number",width=20,font=("bold", 10) )
    label_9.place(x=74,y=520)


    Pan_number = Entry(root)
    Pan_number.insert(0,n[0][8])
    Pan_number.place(x=240,y=520)

    label_10 = Label(root, text="Father Name",width=20,font=("bold", 10) )
    label_10.place(x=74,y=570)


    Father_name= Entry(root)
    Father_name.insert(0,n[0][9])
    Father_name.place(x=240,y=570)

    label_11 = Label(root, text="Mother Name",width=20,font=("bold", 10) )
    label_11.place(x=74,y=620)


    Mother_name = Entry(root)

    Mother_name.insert(0,n[0][10])
    Mother_name.place(x=240,y=620)

    label_12 = Label(root, text="User ID/Customer ID",width=20,font=("bold", 10) )
    label_12.place(x=74,y=670)


    User_id = Entry(root)
    User_id.insert(0,n[0][11])
    User_id.place(x=240,y=670)

    label_13 = Label(root, text="User Password",width=20,font=("bold", 10) )
    label_13.place(x=74,y=720)


    User_Password = Entry(root)
    User_Password.insert(0,n[0][12])
    User_Password.place(x=240,y=720)

    Button(root, text='Update',width=20,bg='brown',fg='white',command=updating_user_data).place(x=180,y=780)
        
    #messagebox.showinfo("","User Created sucessfully")

    # it is use for display the registration form on the window

    root.mainloop()
    print("registration form  successfully created...")


      

if '__name__'=='__main__':
    update_entry()
