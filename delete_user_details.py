from tkinter import *
import pymysql
import tkinter.messagebox as MessageBox


            

def deleting_user_data(user_adhar):
    b = pymysql.connect(host='localhost',user='root',password='root')
    mycursor = b.cursor()
    mycursor.execute("USE bank_of_ojas")
    mycursor.execute("DELETE FROM bank3 where Aadhar='"+user_adhar+"'")
    b.commit()
    MessageBox.showinfo("succes","Deleted successfully")
    
if '__name__'=='__main__':
    deleting_user_data()
