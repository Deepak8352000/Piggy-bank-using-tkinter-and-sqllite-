from os import error
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import tkinter

con=sqlite3.connect('database.db')
cur=con.cursor()



class CreateAcc(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x650+200+100")
        self.title("Create account")
        self.resizable(False, False)
        self.grab_set()
        
        self.top=Frame(self , height=100,bg="white")
        self.top.pack(fill=X)
        
        self.buttom=Frame(self , height=550,bg='#f59b42')
        self.buttom.pack(fill=X)
        #####################
        self.top_image=PhotoImage(file='icons/add.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=140,y=10)
        
        
        self.heading=Label(self.top,text="Create new account",
                           font='arial 20 bold',fg="#34bdeb",bg='white')
        self.heading.place(x=270,y=30)
        
       
        
        
        #name
        self.label_name=Label(self.buttom,text="Name",font='arial 15 bold ',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_name.place(x=50,y=40)
        
        self.entry_name=Entry(self.buttom,width=30,bd=4,font=("arial, 15"))
        self.entry_name.insert(0,"Enter name")
        self.entry_name.place(x=190,y=40)
        #Acc num
        self.label_accnum=Label(self.buttom,text="Acc_Num",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_accnum.place(x=50,y=80)
        
        self.entry_accnum=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_accnum.insert(0,"Enter Account number")
        self.entry_accnum.place(x=190,y=80)
        
        #Acc_money
                
        self.label_acc_money=Label(self.buttom,text="Acc_money",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_money.place(x=50,y=130)
        
        self.entry_acc_money=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_money.insert(0,"Enter Acc_money")
        self.entry_acc_money.place(x=190,y=130)
        

        #address
        self.label_address=Label(self.buttom,text="Address",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_address.place(x=50,y=180)
        
        self.entry_address=Text(self.buttom,width=20,height=6,bd=5,font='arial 15 ')
        self.entry_address.place(x=190,y=180)

        #acc contact
        self.label_acc_contact=Label(self.buttom,text="Acc_Contact",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_contact.place(x=50,y=350)
        
        self.entry_acc_contact=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_contact.insert(0,"Enter Acc_Contact ")
        self.entry_acc_contact.place(x=190,y=350)
       
        #acc_dob
        self.label_acc_dob=Label(self.buttom,text="Acc_DOB",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_dob.place(x=50,y=400)
        
        self.entry_acc_dob=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_dob.insert(0,"Enter Acc_Date of Birth ")
        self.entry_acc_dob.place(x=190,y=400)

        #acc_doj
        self.label_acc_dob=Label(self.buttom,text="Acc_DOj",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_dob.place(x=50,y=450)
        
        self.entry_acc_doj=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_doj.insert(0,"Enter Acc_Date of Joining ")
        self.entry_acc_doj.place(x=190,y=450)

        #button

        
        button=Button(self.buttom,text='Add Account',fg='yellow',font='arial 12 bold',bg="blue",relief=RAISED,bd=5,command=self.addtodb)
        button.place(x=270,y=500)


    def addtodb(self):
        acc_num=self.entry_accnum.get()
        name=self.entry_name.get()
        acc_money=self.entry_acc_money.get()
        address=self.entry_address.get(1.0,'end-1c')
        acc_contact=self.entry_acc_contact.get()
        acc_doj=self.entry_acc_doj.get()
        acc_dob=self.entry_acc_dob.get()
       
       
    
        if name and acc_num and acc_money and acc_contact and acc_dob and acc_doj and address !="":
            try:
                query="insert into 'accinfo'(acc_no,acc_name,acc_money,acc_address,acc_contact,acc_doj,acc_dob)values(?,?,?,?,?,?,?)"
                cur.execute(query,(acc_num,name,acc_money,address,acc_contact,acc_doj,acc_dob))
                con.commit()
                messagebox.showinfo("Account added",'Dont forget your Account number')
                self.destroy()
                
            except EXCEPTION as t :
                messagebox.showerror("ERROR",str(t))
        else:
            messagebox.showerror("Error","Please fill all the fields",icon='warning')
                
                

