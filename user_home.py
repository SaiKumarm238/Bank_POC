from tkinter import *
import os
# from pymysql import*
from tkinter import messagebox as msg


def account_details(Account):
    Account.state("zoomed")
    Label(Account, text="Holdername").place(x=10, y=10)
    Label(Account, text="Acc No").place(x=10, y=50)
    Label(Account, text="Acc Type").place(x=10, y=90)
    Label(Account, text="Bank Name").place(x=10, y=130)
    Label(Account, text="IFSC code").place(x=10, y=170)
    a1 = Entry(Account).place(x=200, y=10)
    c1 = Entry(Account).place(x=200, y=50)
    d1 = Entry(Account).place(x=200, y=90)
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
    a1 = Entry(mini_statement_screen).place(x=200, y=10)
    c1 = Entry(mini_statement_screen).place(x=200, y=50)
    d1 = Entry(mini_statement_screen).place(x=200, y=90)
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
           font=("Arial Bold", 10), command=withdraw).place(x=250, y=70)
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

def deposit(deposit_screen):

    deposit_screen.state('zoomed')
    deposit_screen.title('deposit')
    Label(deposit_screen, text=" FOR SELF DEPOSITE  ENTER AMOUNT").place(x=50, y=10)
    Button(deposit_screen, text="SUBMIT", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10)).place(x=470, y=10)
    self_deposit = Entry(deposit_screen).place(x=270, y=10)
    Label(deposit_screen, text=" TO DEPOSITE IN ANOTHER ACCOUNT ").place(x=50, y=50)
    Button(deposit_screen, text="CLICK HERE", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10), command=lambda :deposit_screen_to_another_acc(deposit_screen)).place(x=270, y=50)
    Button(deposit_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :deposite_screen_to_transactions_call(deposit_screen)).place(x=370, y=50)
    Button(deposit_screen, text="HOME", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :deposit_screen_to_main_account_screen_call(deposit_screen)).place(x=470, y=50)


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


def another_acc(acc_screen):

    acc_screen.state('zoomed')
    acc_screen.title('deposit in another acc')
    Button(acc_screen, text="SUBMIT", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10)).place(x=285, y=130)
    Label(acc_screen, text="ENTER ACCOUNT NUMBER").place(x=50, y=10)
    deposit_acc_no = Entry(acc_screen).place(x=270, y=10)
    Label(acc_screen, text="ENTER IFCI CODE").place(x=50, y=50)
    deposit_acc_ifci = Entry(acc_screen).place(x=270, y=50)
    Label(acc_screen, text="ENTER AMOUNT").place(x=50, y=90)
    deposit_acc_amount = Entry(acc_screen).place(x=270, y=90)
    Button(acc_screen, text="BACK", height="1", width="10", fg='WHITE', bg='SteelBlue',
          font=("Arial Bold", 10),command=lambda :another_acc_to_deposite_screen_call(acc_screen)).place(x=385,y=130)
    Button(acc_screen, text="HOME", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10),command=lambda :another_acc_to_main_screen_call(acc_screen)).place(x=485,y=130)

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

def withdraw():
    withdraw_screen = Tk()
    withdraw_screen.state('zoomed')
    withdraw_screen.title('withdraw')
    Label(withdraw_screen, text=" ENTER AMOUNT ").place(x=50, y=10)
    withdraw_amount = Entry(withdraw_screen).place(x=150, y=10)
    Button(withdraw_screen, text="SUBMIT", height="1", width="10", fg='WHITE', bg='SteelBlue',
           font=("Arial Bold", 10)).place(x=370, y=10)
    withdraw_screen.mainloop()


def view_balance(viewBalance_screen):

    viewBalance_screen.state("zoomed")
    viewBalance_screen.title("ViewBalance")
    Label(viewBalance_screen, text="BALANCE").place(x=10, y=10)
    a1 = Entry(viewBalance_screen).place(x=200, y=10)
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
    Label(text="HOME PAGE", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="ACCOUNT DETAILS", height="3", width="20", fg='black', bg='Turquoise', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_account_details(main_screen)).pack()
    Label(text="").pack()
    Button(text="MINI STATEMENT", height="3", width="20", fg='black', bg='LightCyan', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_mini_statement(main_screen)).pack()
    Label(text="").pack()
    Button(text="TRANSACTIONS", height="3", width="20", fg='black', bg='Sienna', font=("Arial Bold", 10),
           command=lambda: main_account_screen_to_transactions(main_screen)).pack()
    Label(text="").pack()
    Button(text="VIEW BALANCE", height="3", width="20", fg='black', bg='orange', font=("Arial Bold", 10),
           command=lambda :main_account_screen_to_viewbalance_screen(main_screen)).pack()
    Label(text="").pack()




def main_account_screen_call():
    global main_screen
    main_screen = Tk()
    main_account_screen(main_screen)
    main_screen.mainloop()



main_account_screen_call()

