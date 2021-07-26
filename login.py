from tkinter import messagebox
import pymysql

def login(self):
        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='root',
                                      database='e_commerce')
                cur = con.cursor()
                cur.execute('select * from registration_copy where email=%s and password=%s', (self.email_txt.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('error', 'Invalid Username and Password', parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    login_to_home(self.root)
                    con.close()
            except Exception as es:
                messagebox.showerror('error', f'Error Due to : {str(es)}', parent=self.root)