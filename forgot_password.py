from tkinter import *
import tkinter.messagebox as tsmg
from tkinter import messagebox
import pymysql
import requests
import random
def otp():
    root = Tk()
    root.state("zoomed")
    rand = random.randint(1, 999999)
    msg = f"Your One Time Password(OTP) is {rand}"
    def sms_send(a, msg):
        url = "https://www.fast2sms.com/dev/bulk"
        params = {
            # Paste Your Unique API Here in-place of ************
            "authorization": "ZzYxEM0mb5gQndTsl9WJqH71P4Aet8uv3DraBK6GFoVOc2XyNiUl3rR5OvWMS0gEoFYPiQpNtBTzuK2f",
            "sender_id": "SMSINI",
            "message": msg,
            "language": "english",
            "route": "p",
            "numbers": a
        }
        rs = requests.get(url, params=params)
    def send():
        a = num.get()
        print(num)
        print(a)
        if (a == ""):
            tsmg.showerror("Error", "Enter Your Mobile Number")
        elif (len(a) < 10):
            tsmg.showerror("Error", "Invalid Mobile Number")
            num.set("")
        else:
            b = tsmg.askyesno("Info", f"Your Number is {a}")
            if (b == True):
                mydb = pymysql.connect(host='localhost', user='root', password='root', db='bank_of_ojas')
                mycursor = mydb.cursor()
                mycursor.execute("select Phno from bank5 where uid='"+uid.get()+"'")
                result = mycursor.fetchone()
                print(result[0])
                if str(result[0])==num.get():
                    sms_send(a, msg)
                    mydb.commit()
                else:
                    messagebox.showinfo("Error","enter valid username and valid mobilenumber")
            else:
                num.set("")
    def check():
        c = otp2.get()
        if (c == ""):
            tsmg.showerror("Error", "Enter OTP")
        else:
            if (str(rand) == c):
                # tsmg.showinfo("info","success")
                f4 = Frame(root)
                Label(f4, text="New Password", font="SegoeUI 20 bold", fg="teal").pack(padx=5, pady=8)
                t2 = Entry(f4, font="SegoeUI 14 bold", fg="black", bg="white", relief=SUNKEN, borderwidth=5,
                           justify="center")
                t2.config(show="*")
                t2.pack(ipady=5)
                f4.pack(fill=BOTH, padx=10, pady=10)
                f5 = Frame(root)
                Label(f5, text="Confirm Password", font="SegoeUI 20 bold", fg="teal").pack(padx=5, pady=8)
                t3 = Entry(f5, font="SegoeUI 14 bold", fg="black", bg="white", relief=SUNKEN, borderwidth=5,
                           justify="center")
                t3.config(show="*")
                t3.pack(ipady=5)
                f5.pack(fill=BOTH, padx=10, pady=10)
                def check1():
                    if t2.get() != "" or t3.get() != "":
                        if t2.get() == t3.get():
                            b=pymysql.connect(host='localhost',user='root',password='root',db='bank_of_ojas')
                            mycursor=b.cursor()
                            mycursor.execute("update bank5 set Password='"+t3.get()+"' where Phno='"+num.get()+"'")
                            b.commit()
                            messagebox.showinfo("success", "password updated successfully!!")
                            root.destroy()
                        else:
                            messagebox.showinfo("Error", "Your password didn't get match!!")
                    else:
                        messagebox.showinfo("Error", "Please fill the complete field!!")
                f6 = Frame(root)
                Button(f6, text="Submit", command=check1, font="SegoeUI 10 bold", fg="purple").pack(padx=5, pady=10,
                                                                                                   side=LEFT)
                f6.pack()
            else:
                tsmg.showerror("Error", "Invalid OTP")
                num.set("")
                otp.set("")
    root.geometry("500x500")
    root.title("OTP-Checker")
    global num,otp2,uid
    num = StringVar()
    otp2 = StringVar()
    uid = StringVar()
    f1 = Frame(root)
    Label(f1, text="Reset Password", font="SegoeUI 30 bold", fg="purple").pack(padx=5, pady=10)
    f1.pack(fill=BOTH)
    f12 = Frame(root)
    Label(f12, text="Enter Uid", font="SegoeUI 20 bold", fg="teal").pack(padx=5, pady=5)
    e12 = Entry(f12, textvar=uid, font="SegoeUI 14 bold", fg="black", bg="white", relief=SUNKEN, borderwidth=4,
               justify="center").pack(ipady=5)
    f12.pack(fill=BOTH, padx=5, pady=10)
    f2 = Frame(root)
    Label(f2, text="Enter Your Mobile Number", font="SegoeUI 20 bold", fg="teal").pack(padx=5, pady=5)
    e1 = Entry(f2, textvar=num, font="SegoeUI 14 bold", fg="black", bg="white", relief=SUNKEN, borderwidth=4,
               justify="center").pack(ipady=5)
    f2.pack(fill=BOTH, padx=5, pady=10)
    f4 = Frame(root)
    Button(f4, text="Send OTP", command=send, font="SegoeUI 10 bold", fg="purple").pack(padx=20, pady=10, side=LEFT)
    f4.pack()
    f3 = Frame(root)
    Label(f3, text="Enter OTP", font="SegoeUI 20 bold", fg="teal").pack(padx=5, pady=5)
    e2 = Entry(f3, textvariable=otp2, font="SegoeUI 14 bold", fg="black", bg="white", relief=SUNKEN, borderwidth=5,
               justify="center").pack(ipady=5)
    f3.pack(fill=BOTH, padx=5, pady=10)
    f4 = Frame(root)
    # Button(f4,text="Send OTP",command=send,font="SegoeUI 10 bold",fg="purple").pack(padx=20,pady=10,side=LEFT)
    Button(f4, text="Check OTP", command=check, font="SegoeUI 10 bold", fg="purple").pack(padx=40, pady=10, side=LEFT)
    f4.pack()
    root.mainloop()

