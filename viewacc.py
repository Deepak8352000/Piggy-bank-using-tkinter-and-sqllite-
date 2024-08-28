from tkinter import *
import sqlite3
import datetime
from tkinter import messagebox

date=datetime.datetime.now().date()
date=str(date)

con=sqlite3.connect('database.db')
cur=con.cursor()

class SeeAcc(Toplevel):
    def __init__(self,accnum):
         Toplevel.__init__(self)
    
         self.geometry("650x650")
         self.title("Account infromation")
         self.resizable(False, False)
         self.top=Frame(self , height=100,bg="white")
         self.top.pack(fill=X)
         self.buttom=Frame(self , height=550,bg='#42ecf5')
         self.buttom.pack(fill=X)
        #####################
         self.top_image=PhotoImage(file='icons/search.png')
         self.top_image_label=Label(self.top,image=self.top_image,bg='white')
         self.top_image_label.place(x=140,y=10)
        
        
         self.heading=Label(self.top,text="Account Information",
                           font='arial 20 bold',fg="#34bdeb",bg='white')
         self.heading.place(x=270,y=30)

         query="select * from accinfo where acc_no='{}'".format(accnum)
         result=cur.execute(query).fetchone()
         print(result)
         
         acc_num=result[0]
         acc_name=result[1]
         acc_money=result[2]
         acc_address=result[3]
         acc_contact=result[4]
         acc_doj=result[5]
         acc_dob=result[6]
      
        
        
        
        #name
         self.label_name=Label(self.buttom,text="Name",font='arial 15 bold ',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_name.place(x=50,y=40)
        
         self.entry_name=Entry(self.buttom,width=30,bd=4,font=("arial, 15"))
         self.entry_name.insert(0,acc_name)
         
         self.entry_name.place(x=190,y=40)
        #Acc num
         self.label_accnum=Label(self.buttom,text="Acc_Num",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_accnum.place(x=50,y=80)
        
         self.entry_accnum=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
         
         self.entry_accnum.insert(0,acc_num)
         self.entry_accnum.config(state='disable')
         self.entry_accnum.place(x=190,y=80)
        
        #Acc_money
                
         self.label_acc_money=Label(self.buttom,text="Acc_money",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_acc_money.place(x=50,y=130)
        
         self.entry_acc_money=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
         self.entry_acc_money.insert(0,acc_money)
         self.entry_acc_money.place(x=190,y=130)
        

        #address
         self.label_address=Label(self.buttom,text="Address",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_address.place(x=50,y=180)
        
         self.entry_address=Text(self.buttom,width=20,height=6,bd=5,font='arial 15 ')
         self.entry_address.place(x=190,y=180)
         self.entry_address.insert(1.0,acc_address)

        #acc contact
         self.label_acc_contact=Label(self.buttom,text="Acc_Contact",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_acc_contact.place(x=50,y=350)
        
         self.entry_acc_contact=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
         self.entry_acc_contact.insert(0,acc_contact)
         self.entry_acc_contact.place(x=190,y=350)
       
        #acc_dob
         self.label_acc_dob=Label(self.buttom,text="Acc_DOB",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_acc_dob.place(x=50,y=400)
        
         self.entry_acc_dob=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
         self.entry_acc_dob.insert(0,acc_dob)
         self.entry_acc_dob.place(x=190,y=400)

        #acc_doj
         self.label_acc_doj=Label(self.buttom,text="Acc_DOB",font='arial 15 bold',fg='black',bg='light blue',width=10,anchor=W,relief=SUNKEN)
         self.label_acc_doj.place(x=50,y=450)
        
         self.entry_acc_doj=Entry(self.buttom,width=30,bd=4,font='arial 15 ')
         self.entry_acc_doj.insert(0,acc_doj)
         self.entry_acc_doj.place(x=190,y=450)


