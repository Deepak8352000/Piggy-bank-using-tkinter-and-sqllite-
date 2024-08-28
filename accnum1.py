from tkinter import *
from withdraw import Withdraw



class Acc_Num1(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Information needed")
        self.config(bg="#4B6587")
        
        self.geometry("300x270")

        self.Top_frame=Frame(self,height=70,bg="light blue",relief=SUNKEN,bd=5)
        self.Top_frame.pack(fill=X)
        self.label_title1=Label(self.Top_frame,text="E-piggy bank",font='"Old English Text MT" 30 bold',fg='black',bg="light blue")
        self.label_title1.place(x=30,y=10)
        self.label_title2=Label(self,text="Information Needed",font='"Arial" 7 bold',fg='white',bg="red")
        self.label_title2.place(x=100,y=70)
        
        self.label_accnum=Label(self,text="Acc_Num : ",font='arial 12 bold',fg='black',bg='white',relief=GROOVE)
        self.label_accnum.place(x=0,y=130)
        
        self.entry_accnum=Entry(self,width=30,bd=4,font='arial 12')
        self.entry_accnum.insert(0,"Enter Account number")
        self.entry_accnum.place(x=0,y=160)
        
        button=Button(self,text='   SUBMIT  ',fg='black',font='arial 12',bg="#ffb703",command=self.acc_id,relief=RAISED)
        button.place(x=0,y=195)
    
    
    def acc_id(self):
        accnum=self.entry_accnum.get()
        accnumbe=Withdraw(accnum)
        
      
        self.destroy()
    
    