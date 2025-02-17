from tkinter import *
from db import DataBase
from emotions import emo
from tkinter import  messagebox

class ben:
    def __init__(self):
        self.root = Tk()
        self.root.title("Benetton App")
        self.root.iconbitmap('ben.ico')
        self.root.geometry('300x600')
        self.root.configure(bg='#21c388')
        self.data = DataBase()

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        l_head = Label(self.root, text='Benetton App', bg='#21c388', fg='Black', font=('Showcard Gothic', 25))
        l_head.pack(pady=(50, 50))

        l_email = Label(self.root, text='Email', bg='#21c388', fg='Black', font=('Calibri', 16), justify="center")
        l_email.pack(pady=(3, 3))
        self.l_email_in = Entry(self.root, width=30, font=('Arial', 12), justify='center', bd=2, relief="solid")
        self.l_email_in.pack(pady=(3, 3), ipady=4)

        l_pass = Label(self.root, text='Password', bg='#21c388', fg='Black', font=('Calibri', 16), justify="center")
        l_pass.pack(pady=(3, 3))
        self.l_pass_in = Entry(self.root, width=30, font=('Arial', 12), justify='center', bd=2, relief="solid", show='*')
        self.l_pass_in.pack(pady=(3, 3), ipady=4)

        l_pass_in = Button(self.root, text='Login', width=10, font=('Calibri', 12), justify='center',command=self.checkdata)
        l_pass_in.pack(pady=(15, 15), ipady=2)

        l_member = Label(self.root, text='Not a Member', bg='#21c388', fg='Black', font=('Calibri', 15), justify="center")
        l_member.pack(pady=(2, 2))

        l_log_in = Button(self.root, text='Register Now', width=20, font=('Calibri', 12), bg='#1a976a', command=self.register_gui)
        l_log_in.pack(pady=(15, 15), ipady=2)

    def register_gui(self):
        self.clear()
        l_head = Label(self.root, text='Benetton App', bg='#21c388', fg='Black', font=('Showcard Gothic', 25))
        l_head.pack(pady=(50, 50))

        l_name = Label(self.root, text='Enter Your Name', bg='#21c388', fg='Black', font=('Calibri', 16), justify="center")
        l_name.pack(pady=(3, 3))
        self.l_name_in = Entry(self.root, width=30, font=('Arial', 12), justify='center', bd=2, relief="solid")  # FIXED
        self.l_name_in.pack(pady=(3, 3), ipady=4)

        l_email = Label(self.root, text='Enter Your Email', bg='#21c388', fg='Black', font=('Calibri', 16), justify="center")
        l_email.pack(pady=(3, 3))
        self.l_email_inn = Entry(self.root, width=30, font=('Arial', 12), justify='center', bd=2, relief="solid")
        self.l_email_inn.pack(pady=(3, 3), ipady=4)

        l_pass = Label(self.root, text='Enter Your Password', bg='#21c388', fg='Black', font=('Calibri', 16), justify="center")
        l_pass.pack(pady=(3, 3))
        self.l_pass_inn = Entry(self.root, width=30, font=('Arial', 12), justify='center', bd=2, relief="solid", show='*')
        self.l_pass_inn.pack(pady=(3, 3), ipady=4)

        l_pass_in = Button(self.root, text='Register Now', width=20, font=('Calibri', 12), justify='center', command=self.dbdata)
        l_pass_in.pack(pady=(15, 15), ipady=2)

        l_member = Label(self.root, text='Already a Member', bg='#21c388', fg='Black', font=('Calibri', 15), justify="center")
        l_member.pack(pady=(2, 2))

        l_log_in = Button(self.root, text='Login Now', width=10, font=('Calibri', 12), bg='#1a976a', command=self.login_gui)
        l_log_in.pack(pady=(15, 15), ipady=2)

    def dbdata(self):

        name = self.l_name_in.get()  # FIXED
        email=self.l_email_inn.get()
        pws=self.l_pass_inn.get()
        res=self.data.add_data(email,name,pws)

        if res:
            messagebox.showinfo('Success', 'Registration Done Successfully')
        else:
            messagebox.showinfo('Error', 'Email Already Exists')

    def checkdata(self):
        email=self.l_email_in.get()
        pss=self.l_pass_in.get()
        result=self.data.check_data(email,pss)
        if result:
            return self.sen()
        else:
            messagebox.showinfo('Error','Failed to Log in As Wrong Email Or Password')


    def sen(self):
        self.clear()

        l_head = Label(self.root, text='Benetton App', bg='#21c388', fg='Black', font=('Showcard Gothic', 25))
        l_head.pack(pady=(50, 50))

        l_log_in = Button(self.root, text='Sentimental Analysis', width=20, font=('Calibri', 15), bg='#949e82',command=self.login_gui)
        l_log_in.pack(pady=(20, 20), ipady=4)

        l_log_in = Button(self.root, text='Sentimental Analysis', width=20, font=('Calibri', 15), bg='#949e82',command=self.login_gui)
        l_log_in.pack(pady=(20, 20), ipady=4)

        l_log_in = Button(self.root, text='Sentimental Analysis', width=20, font=('Calibri', 15), bg='#949e82',command=self.login_gui)
        l_log_in.pack(pady=(20, 20), ipady=4)

        l_log_in = Button(self.root, text='Back', width=5, font=('Calibri', 12),command=self.login_gui)
        l_log_in.pack(pady=(15, 15), ipady=3)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

ben1 = ben()
