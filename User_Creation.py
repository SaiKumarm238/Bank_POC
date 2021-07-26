from os import umask
from tkinter import*
from tkinter import messagebox
import tkinter as tk
import re
import pymysql
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def user_create():
    def check():
        
        if (Fname.get() == "" or Lname.get() == "" or gender.get() == "" or DOB.get() == "" or Phno.get() == "" 
        or Email.get() == "" or Adhar.get() == "" or Address.get() == "" or Pan_number.get() == "" 
        or Father_name.get() == "" or Mother_name.get() == "" or User_id.get() == "" or User_Password.get() == ""):
            messagebox.showinfo("Blank Spaces not allowed","Blank Spaces not Allowed")
        elif len(Fname.get()) <= 3:
            messagebox.showinfo("Please Enter Min Char in First Name","Please Enter Min Char in First Name")
        elif len(Lname.get()) <= 3:
            messagebox.showinfo("Please Enter Min Char in Last Name","Please Enter Min Char in Last Name")
        # elif gender.get() != 'male' or gender.get() != 'female' :
        #     messagebox.showinfo("Please Enter Male or Female Only !", "Please Enter Male or Female Only !") 
        # elif len(DOB.get()) != 8:
            messagebox.showinfo("Please Enter Correct DOB format","Please Enter Correct DOB format")
        elif len(Phno.get()) != 10:
            messagebox.showinfo("Please Enter Correct Phone Number","Please Enter Correct Phone Number")
        elif not re.search(regex,Email.get()):  
            messagebox.showinfo("Please Enter Correct Email","Please Enter Correct Email")
        elif len(Adhar.get()) != 12:
            messagebox.showinfo("Please Enter Correct Aadhar Number","Please Enter Correct Aadhar Number")
        elif len(Pan_number.get()) != 10:
            messagebox.showinfo("Please Enter Correct Pan Number","Please Enter Correct Pan Number")
        elif len(Father_name.get()) <= 6:
            messagebox.showinfo("Please Enter Full Father Name","Please Enter Full Father Name")
        elif len(Mother_name.get()) <= 6:
            messagebox.showinfo("Please Enter Full Mother Name","Please Enter Full Mother Name")
        elif len(User_id.get()) <= 8:
            messagebox.showinfo("Please Enter correct User ID/Customer ID","Please correct Enter User ID/Customer ID")
        else:
            insert()
            messagebox.showinfo("User Created Successfully","User Created Successfully")  
            #root.destroy() 
        
    def insert():
        
        if (Fname.get()=="" or Lname.get()==""):
                messagebox.showinfo("Error","Enter all fields")
        else:
            
            #quit_loop()
            b = pymysql.connect(host='localhost',user='root',password='root')
            mycursor = b.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS bank_of_ojas")
            mycursor.execute("USE bank_of_ojas")
            mycursor.execute("CREATE TABLE if not exists bank3(Fname varchar(20),Lname varchar(20),Gender varchar(10),DOB date,Phno bigint(50),Email varchar(30),Aadhar bigint(15),Address varchar(30),"
                            "Pan varchar(20),Father varchar(20),Mother varchar(20),Uid varchar(20),Password varchar(20))")
            mycursor.execute("INSERT INTO bank3 (Fname,Lname,Gender,DOB,Phno,Email,Aadhar,Address,Pan,Father,Mother,Uid,Password) VALUES('"+Fname.get()+"','"+Lname.get()+"','"+gender.get()+"','"+DOB.get()+"','"+Phno.get()+"','"+Email.get()+"','"+Adhar.get()+"','"+Address.get()+"','"+Pan_number.get()+"','"+Father_name.get()+"','"+Mother_name.get()+"','"+User_id.get()+"','"+User_Password.get()+"')")
            b.commit()
            messagebox.showinfo("Success","Inserted successfully.")

    # Radio_Value0 = tk.IntVar ()
    # def quit_loop():
    #     global gender
    #     print ("result", Radio_Value0.get ())
    #     if Radio_Value0.get () == 0:
    #         gender = 'Male'    
    #     else:
    #         gender = 'Female'
         
    def user_entry():
        global Fname
        global gender
        global Lname
        global DOB
        global Phno
        global Email
        global Adhar
        global Address
        global Pan_number
        global Father_name
        global Mother_name
        global User_id
        global User_Password

        
        root = Tk()
        root.state("zoomed")
        root.configure(bg='#e68a00')
        root.geometry('500x1000')
        root.title("Registration Form")
        temporary=StringVar()

        label_0 = Label(root, text="User Creation",width=20,font=("bold", 20))
        label_0.place(x=700,y=53)


        label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
        label_1.place(x=700,y=130)

        Fname = Entry(root)
        Fname.place(x=900,y=130)

        label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
        label_2.place(x=700,y=180)

        Lname = Entry(root)
        Lname.place(x=900,y=180)
        
        label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
        label_3.place(x=700,y=230)

        
        # Radio_Value0.set(0)
        # Shutdown_Option = {0: 'Male', 1: 'Female'}
        gender = Entry(root)
        gender.place(x=900,y=230)

        # R_button0 = (tk.Radiobutton(root, text=Shutdown_Option[0],padx = 5, variable=Radio_Value0, value=0).place(x=235,y=230))
        # R_button1 = (tk.Radiobutton(root, text=Shutdown_Option[1],padx = 20, variable=Radio_Value0, value=1).place(x=290,y=230))
        # button4=tk.Button(root, text='Submit',width=20,bg='brown',fg='white',command=quit_loop).place(x=180,y=780)



        label_4 = Label(root, text="Date of Birth",width=20,font=("bold", 10))
        label_4.place(x=700,y=280)


        DOB = Entry(root)
        DOB.place(x=900,y=280)


        label_5 = Label(root, text="Phone Number",width=20,font=("bold", 10))
        label_5.place(x=700,y=330)


        Phno = Entry(root)
        Phno.place(x=900,y=330)


        label_6 = Label(root, text="Email",width=20,font=("bold", 10))
        label_6.place(x=700,y=380)


        Email = Entry(root)
        Email.place(x=900,y=380)

        label_7 = Label(root, text="Aadhar Number",width=20,font=("bold", 10))
        label_7.place(x=700,y=430)


        Adhar = Entry(root)
        Adhar.place(x=900,y=430)

        label_8 = Label(root, text="Address",width=20,font=("bold", 10))
        label_8.place(x=700,y=480)


        Address = Entry(root)
        Address.place(x=900,y=480)

        label_9 = Label(root, text="Pan Number",width=20,font=("bold", 10) )
        label_9.place(x=700,y=520)


        Pan_number = Entry(root)
        Pan_number.place(x=900,y=520)

        label_10 = Label(root, text="Father Name",width=20,font=("bold", 10) )
        label_10.place(x=700,y=570)


        Father_name= Entry(root)
        Father_name.place(x=900,y=570)

        label_11 = Label(root, text="Mother Name",width=20,font=("bold", 10) )
        label_11.place(x=700,y=620)


        Mother_name = Entry(root)
        Mother_name.place(x=900,y=620)

        label_12 = Label(root, text="User ID/Customer ID",width=20,font=("bold", 10) )
        label_12.place(x=700,y=670)


        User_id = Entry(root)
        User_id.place(x=900,y=670)

        label_13 = Label(root, text="User Password",width=20,font=("bold", 10) )
        label_13.place(x=700,y=720)


        User_Password = Entry(root)
        User_Password.place(x=900,y=720)

        Button(root, text='Submit',width=20,bg='brown',fg='white',command=check).place(x=800,y=800)
        
        #messagebox.showinfo("","User Created sucessfully")

        # it is use for display the registration form on the window

        root.mainloop()
        #print("registration form  successfully created...")
    
    user_entry()
if '__name__'=='__main__':
    user_create()
