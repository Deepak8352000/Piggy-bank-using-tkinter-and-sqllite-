from tkinter import*
import sqlite3
import datetime
from tkinter import messagebox

date=datetime.datetime.now().date()
date=str(date)

con=sqlite3.connect('database.db')
cur=con.cursor()

class Deposite(Toplevel):
    def __init__(self,accnum1):
        Toplevel.__init__(self)
        
        self.geometry("820x650")
        self.title("Withdraw money")
        self.resizable(False, False)
        
        self.top=Frame(self , height=100,bg="white")
        self.top.pack(fill=X)
        
        self.buttom=Frame(self , height=550,bg='#f59b42')
        self.buttom.pack(fill=X)

        self.bin1=Frame(self.buttom,height=400,width=270,relief=GROOVE,bd=5,bg="#55eb34")
        self.bin1.place(x=535,y=43)
        #####################
        self.top_image=PhotoImage(file='icons/deposite.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=140,y=10)
        self.accnum1=accnum1
        
        self.heading=Label(self.top,text="Deposite money",
                           font='arial 20 bold',fg="#34bdeb",bg='white')
        self.heading.place(x=220,y=30)
        
        
        query="select * from accinfo where acc_no='{}'".format(self.accnum1)
        result=cur.execute(query).fetchone()
        
       
        accnum=result[0]
        accname=result[1]
        accmoney1=result[2]
        accaddress=result[3]
        acc_cont=result[4]
        accdob=result[5]
        accdoj=result[6]
        self.accmoney1=accmoney1
        #current balance
        self.label_currentbal=Label(self.bin1,text="Your current balance is ",font='arial 12 bold',fg='black',bg='light blue')
        self.label_currentbal.place(x=10,y=40)
        
        self.entry_currentbal=Entry(self.bin1,width=30,bd=4)
        
        self.entry_currentbal.insert(0,"Rs."+accmoney1)
        self.entry_currentbal.config(state='disable')
        self.entry_currentbal.place(x=10,y=80)
        
        #dep
        self.label_deposite=Label(self.bin1,text="Enter amount of Deposite",font='arial 12 bold',fg='black',bg='light blue')
        self.label_deposite.place(x=10,y=120)
 
        self.entry_deposite=Entry(self.bin1,width=30,bd=4)
        self.entry_deposite.place(x=10,y=160)

        
        
     #name
        self.label_name=Label(self.buttom,text="Name",font='arial 15 bold ',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_name.place(x=50,y=40)
        
        self.entry_name=Entry(self.buttom,width=30,bd=4,font=("arial, 15"))
        self.entry_name.insert(0,accname)
        self.entry_name.place(x=190,y=40)
        #Acc num
        self.label_accnum=Label(self.buttom,text="Acc_Num",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_accnum.place(x=50,y=80)
        
        self.entry_accnum=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_accnum.insert(0,accnum)
        self.entry_accnum.place(x=190,y=80)
        
        #Acc_money
                
        self.label_acc_money=Label(self.buttom,text="Acc_money",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_money.place(x=50,y=130)
        
        self.entry_acc_money=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_money.insert(0,accmoney1)
        self.entry_acc_money.place(x=190,y=130)
        

        #address
        self.label_address=Label(self.buttom,text="Address",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_address.place(x=50,y=180)
        
        self.entry_address=Text(self.buttom,width=20,height=6,bd=5,font='arial 15 ')
        self.entry_address.place(x=190,y=180)
        self.entry_address.insert(1.0,accaddress)

        #acc contact
        self.label_acc_contact=Label(self.buttom,text="Acc_Contact",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_contact.place(x=50,y=350)
        
        self.entry_acc_contact=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_contact.insert(0,acc_cont)
        self.entry_acc_contact.place(x=190,y=350)
       
        #acc_dob
        self.label_acc_dob=Label(self.buttom,text="Acc_DOB",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_dob.place(x=50,y=400)
        
        self.entry_acc_dob=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_dob.insert(0,accdob)
        self.entry_acc_dob.place(x=190,y=400)

        #acc_doj
        self.label_acc_doj=Label(self.buttom,text="Acc_DOB",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
        self.label_acc_doj.place(x=50,y=450)
        
        self.entry_acc_doj=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
        self.entry_acc_doj.insert(0,accdoj)
        self.entry_acc_doj.place(x=190,y=450)



        
        #button
        
        button=Button(self.bin1,text='  Deposite  ',fg='black',font='arial 10 bold',bg="light blue",command=self.withdraw_money)
        button.place(x=10,y=210)
        
        
    def withdraw_money(self):
        withdrawmoney=self.entry_deposite.get()
        curbal=self.accmoney1
        totalmoney=int(curbal)+int(withdrawmoney)
        query="update accinfo set acc_money='{}' where acc_no={}". format(totalmoney,self.accnum1)
        try:
               cur.execute(query)
               con.commit()
               messagebox.showinfo("updated",'Account Updated ')
               self.destroy()
        except Exception as e:
                 print(e)
        
      
        
        
        
        
        
        

