from tkinter import *
import tkinter as tk
import os
import pymysql
from tkinter import messagebox as msg



def user_credentials(user_uid,user_pass):
    global holder_name
    global Acc_No
    global Acc_type
    global balance
    global ifsc
    print(user_pass)
    print(user_uid)
    b = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
    mycursor = b.cursor()
    mycursor.execute('select Fname,Account_No,Account_type,Balance,IFSC_code from bank5 where uid=%s and password=%s', (user_uid,user_pass))
    row = mycursor.fetchall()
    print(row)
    
    holder_name = row[0][0]
    Acc_No = row[0][1]
    
    Acc_type = row[0][2]
    
    balance = row[0][3]
    
    ifsc = row[0][4]
    main_account_screen_call()
def account_details(Account):
    Account.state("zoomed")
    Label(Account, text="Holdername").place(x=10, y=10)
    Label(Account, text="Acc No").place(x=10, y=50)
    Label(Account, text="Acc Type").place(x=10, y=90)
    Label(Account, text="Bank Name").place(x=10, y=130)
    Label(Account, text="IFSC code").place(x=10, y=170)
    
    # text = tk.StringVar()
    # text.set(holder_name)
    a1 = Entry(Account)
    a1.insert(END,holder_name)
    a1.place(x=200, y=10)
    

    c1 = Entry(Account)
    c1.insert(END,Acc_No)
    c1.place(x=200, y=50)

    d1 = Entry(Account)
    d1.insert(END,Acc_type)
    d1.place(x=200, y=90)
    
    Label(Account, text="HONEY WELL").place(x=200, y=130)
    Label(Account, text="HW000325").place(x=200, y=170)
    Button(Account, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue', font=("Arial Bold", 10),
           command=lambda :account_details_to_main_account_screen_call(Account)).place(x=430, y=100)

def account_details_to_main_account_screen_call(Account):
    Account.destroy()
    main_account_screen_call()

def main_account_screen_to_account_details(main_screen):
    main_screen.destroy()
    account_details_call()

def account_details_call():
    Account = Tk()
    account_details(Account)
    Account.mainloop()


def mini_statement(mini_statement_screen):
    mini_statement_screen.state("zoomed")
    Label(mini_statement_screen, text="ACCOUNT NO").place(x=10, y=10)
    Label(mini_statement_screen, text="DATE OF TRANSACTION").place(x=10, y=50)
    Label(mini_statement_screen, text="TYPE OF TRANSACTION").place(x=10, y=90)

    a1 = Entry(mini_statement_screen)
    a1.insert(END,Acc_No)
    a1.place(x=200, y=10)

    c1 = Entry(mini_statement_screen)
    c1.place(x=200, y=50)
    
    d1 = Entry(mini_statement_screen)
    d1.insert(END,Acc_type)
    d1.place(x=200, y=90)

    Button(mini_statement_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda :mini_statemen_to_main_account_screen_call(mini_statement_screen)).place(x=430, y=100)


def mini_statement_call():
    mini_statement_screen = Tk()
    mini_statement(mini_statement_screen)
    mini_statement_screen.mainloop()

def mini_statemen_to_main_account_screen_call(mini_statement_screen):
    mini_statement_screen.destroy()
    main_account_screen_call()

def main_account_screen_to_mini_statement(main_screen):
    main_screen.destroy()
    mini_statement_call()



def transactions(transactions_screen):

    transactions_screen.state("zoomed")
    transactions_screen.title('Transactions')
    Label(transactions_screen, text=" FOR DEPOSITE CLICK HERE").place(x=50, y=10)

    Button(transactions_screen, text="DEPOSIT", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda :transactions_to_deposite_screen_call(transactions_screen)).place(x=250, y=10)

    Label(transactions_screen, text="FOR WITHDRAW CLICK HERE").place(x=50, y=70)

    Button(transactions_screen, text="WITHDRAW", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda:with_data()).place(x=250, y=70)

    Button(transactions_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :transactions_to_main_account_screen_call(transactions_screen)).place(x=400, y=70)

    transactions_screen.mainloop()

def main_account_screen_to_transactions(main_screen):
    main_screen.destroy()
    transactions_call()

def transactions_to_main_account_screen_call(trasactions_screen):
    trasactions_screen.destroy()
    main_account_screen_call()

def transactions_call():
    transactions_screen = Tk()
    transactions(transactions_screen)
    transactions_screen.mainloop()

def deposite_amount_database():
    b = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
    mycursor = b.cursor()
    global amount
    amount = customer.get()
    print(type(amount))
    print("Hello")
    print(amount)
    print(Acc_No)
    print("Comming")
    mycursor.execute("UPDATE bank5 SET Balance = Balance + '"+amount+"' WHERE Account_No='"+str(Acc_No)+"'")
    b.commit()
    print("Enter")
    res = mycursor.fetchall()
    print(res)
    #msg.showinfo("Success","Amount send Successfully")

    #deposit_screen.destroy()

def deposit(deposit_screen):

    deposit_screen.state('zoomed')
    deposit_screen.title('deposit')
        
    global customer
    
    customer = StringVar()

    lb1 = Label(deposit_screen, text=" FOR SELF DEPOSITE  ENTER AMOUNT")
    lb1.place(x=50, y=10)
    
    global self_deposit
    self_deposit = Entry(deposit_screen,bg='white',bd = 5,textvar=customer)
    self_deposit.place(x=270, y=10)
    #amount = self_deposit.get()
    Button(deposit_screen, text="SEND", height="1", width="10", fg='white', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda:deposite_amount_database()).place(x=470, y=10)
    
    tk.Label(deposit_screen, text=" TO DEPOSITE IN ANOTHER ACCOUNT ").place(x=50, y=50)
    tk.Button(deposit_screen, text="CLICK HERE", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda :deposit_screen_to_another_acc(deposit_screen)).place(x=270, y=50)
    tk.Button(deposit_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :deposite_screen_to_transactions_call(deposit_screen)).place(x=370, y=50)
    tk.Button(deposit_screen, text="HOME", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :deposit_screen_to_main_account_screen_call(deposit_screen)).place(x=470, y=50)

    deposit_screen.mainloop()

def deposit_call():
    deposit_screen = Tk()
    deposit(deposit_screen)
    deposit_screen.mainloop()

def transactions_to_deposite_screen_call(trasactions_screen):
    trasactions_screen.destroy()
    deposit_call()
    
def deposite_screen_to_transactions_call(deposit_screen):
    deposit_screen.destroy()
    transactions_call()

def deposit_screen_to_main_account_screen_call(deposite_screen):
    deposite_screen.destroy()
    main_account_screen_call()

def sending_amount_to_database(acc_screen):
    try:
        #deposit_acc_no,deposit_acc_ifci,deposit_acc_amount
        
        global ifsc_code
        global amt
        global Ac
        Ac = deposit_acc_no.get() 
        ifsc_code = deposit_acc_ifci.get()
        amt = deposit_acc_amount.get()
        print(Ac)
        print(ifsc_code)
        print(amt)
        print("Enter")
        b = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
        mycursor = b.cursor()
        mycursor.execute("select balance from bank5 where Account_No = '"+str(Acc_No)+"'")
        result_1 = mycursor.fetchone()
        database_amount = str(result_1[0])
        mycursor.execute("select Account_No,IFSC_code from bank5 where Account_No='"+Ac+"' and IFSC_code='"+ifsc_code+"'")
        if (amt != 0 and amt != '') and (database_amount != '' and eval(database_amount) > 0.0) and amt < database_amount:
            
            mycursor.execute("UPDATE bank5 SET Balance = Balance + '"+amt+"' where Account_No= '"+Ac+"'")
            mycursor.execute("UPDATE bank5 SET Balance = Balance - '"+amt+"' where Account_No='"+str(Acc_No)+"'")
            b.commit()
            msg.showinfo("Success","Successfully Transfered")


        else:
            msg.showinfo("Error","Not Enough Amount !")
            sending_amount_to_database(acc_screen)
        
    except :
        msg.showinfo("Error","Enter Valid Account Number and IFSC Code")
        another_acc(acc_screen)

def another_acc(acc_screen):

    acc_screen.state('zoomed')
    acc_screen.title('deposit in another acc')
    global acc
    global accifsc
    global accamt

    acc = StringVar()
    accifsc = StringVar()
    accamt = StringVar()

    Label(acc_screen, text="ENTER ACCOUNT NUMBER").place(x=50, y=10)

    global deposit_acc_no
    deposit_acc_no = Entry(acc_screen,textvar = acc)
    deposit_acc_no.place(x=270, y=10)

    
    Label(acc_screen, text="ENTER IFCI CODE").place(x=50, y=50)

    global deposit_acc_ifci
    deposit_acc_ifci = Entry(acc_screen,textvar = accifsc)
    deposit_acc_ifci.place(x=270, y=50)

    Label(acc_screen, text="ENTER AMOUNT").place(x=50, y=90)
    global deposit_acc_amount
    deposit_acc_amount = Entry(acc_screen,textvar = accamt)
    deposit_acc_amount.place(x=270, y=90)

    Button(acc_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
          font=("Arial Bold", 10),command=lambda :another_acc_to_deposite_screen_call(acc_screen)).place(x=385,y=130)
    Button(acc_screen, text="HOME", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :another_acc_to_main_screen_call(acc_screen)).place(x=485,y=130)
    Button(acc_screen, text="SEND", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda:sending_amount_to_database(acc_screen)).place(x=285, y=130)


def another_acc_call():
    acc_screen = Tk()
    another_acc(acc_screen)
    acc_screen.mainloop()

def another_acc_to_deposite_screen_call(acc_screen):
    acc_screen.destroy()
    deposit_call()

def deposit_screen_to_another_acc(deposit_screen):
    deposit_screen.destroy()
    another_acc_call()
def another_acc_to_main_screen_call(acc_screen):
    acc_screen.destroy()
    main_account_screen_call()

def withdraw_database():
    global amount
    amount = withdraw_amount.get()

    print(amount)
    
    data = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
    mycursor = data.cursor()
    mycursor.execute("select balance from bank5 where Account_No = '"+str(Acc_No)+"'")
    result = mycursor.fetchone()
    database_amount = result[0]
    if database_amount != '' and database_amount > 0:
        
        print("withdraw")
        
        print(amount)
       # print(arg)
        mycursor.execute("UPDATE bank5 SET Balance = Balance - '"+amount+"' where Account_No = '"+str(Acc_No)+"'")
        data.commit()
    else:
        msg.INFO("Error","Not Enough money")


def with_data():
    withdraw_screen =Tk()
    withdraw(withdraw_screen)
    withdraw_screen.mainloop()

def withdraw(withdraw_screen):
    
    withdraw_screen.state('zoomed')
    withdraw_screen.title('withdraw')

    global withdrawing
    global withdraw_amount
    withdrawing = StringVar()

    lb5 = Label(withdraw_screen, text=" ENTER AMOUNT ")
    lb5.place(x=50, y=10)

    global withdraw_amount
    withdraw_amount = Entry(withdraw_screen,bg='white',bd = 5,textvar = withdrawing)
    withdraw_amount.place(x=150, y=10)

    Button(withdraw_screen, text="Withdraw", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command =lambda:withdraw_database()).place(x=370, y=10)
    


def view_balance(viewBalance_screen):

    data = pymysql.connect(host='localhost',user='root',password='root',database='bank_of_ojas')
    mycursor = data.cursor()
    mycursor.execute("select balance from bank5 where Account_No = '"+str(Acc_No)+"'")
    res = mycursor.fetchone()
    print(res)
    main_balance = res[0]

    viewBalance_screen.state("zoomed")
    viewBalance_screen.title("ViewBalance")
    Label(viewBalance_screen, text="BALANCE").place(x=10, y=10)
    a1 = Entry(viewBalance_screen)
    a1.insert(END,main_balance)
    a1.place(x=200, y=10)

    Button(viewBalance_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda: viewbalance_screen_to_main_account_screen_call(viewBalance_screen)).place(
        x=200, y=50)


def main_account_screen_to_viewbalance_screen(main_screen):
    main_screen.destroy()
    view_balance_call()

def viewbalance_screen_to_main_account_screen_call(viewBalance_screen):
    viewBalance_screen.destroy()
    main_account_screen_call()

def view_balance_call():
    viewBalance_screen = Tk()
    view_balance(viewBalance_screen)
    viewBalance_screen.mainloop()

def main_account_screen(main_screen):
    main_screen.state("zoomed")
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(main_screen,text="HOME PAGE", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(main_screen,text="ACCOUNT DETAILS", height="3", width="20", fg='black', bg='Turquoise', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_account_details(main_screen)).pack()
    Label(text="").pack()

    Button(main_screen,text="MINI STATEMENT", height="3", width="20", fg='black', bg='LightCyan', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_mini_statement(main_screen)).pack()
    Label(text="").pack()

    Button(main_screen,text="TRANSACTIONS", height="3", width="20", fg='black', bg='Sienna', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_transactions(main_screen)).pack()
    Label(text="").pack()

    Button(main_screen,text="VIEW BALANCE", height="3", width="20", fg='black', bg='orange', font=("Arial Bold", 10),
           command=lambda :main_account_screen_to_viewbalance_screen(main_screen)).pack()
    Label(text="").pack()

def main_account_screen_call():
   #,holder_name,Acc_No,Acc_type,balance,ifsc
    global main_screen
    main_screen = Tk()
    main_account_screen(main_screen)
    main_screen.mainloop()


if __name__=='__main__':
    main_account_screen_call()