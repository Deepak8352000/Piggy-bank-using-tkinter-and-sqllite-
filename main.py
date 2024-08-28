from tkinter import*
import time
from createacc import CreateAcc
from viewacc import SeeAcc
from accnum import Acc_Num
from withdraw import Withdraw
from accnum1 import Acc_Num1
from deposite import Deposite
from accnum2 import Acc_Num2





class Application(object):
    def __init__(self,master): 
        self.master=master

        #===========================Frames
        self.top=Frame(master,height=150,bg="#F7F6F2",relief=SUNKEN,border=5)
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=740,bg='#4B6587',relief=SUNKEN,bd=5)
        self.bottom.pack(fill=X)


        #============================TITLE
        self.top_image=PhotoImage(file="icons/bank.png")
        self.top_label=Label(self.top,image=self.top_image,bg="#F7F6F2",height=100)
        self.top_label.place(x=160,y=30)

        self.top_image1=PhotoImage(file="icons/bank.png")
        self.top_label1=Label(self.top,image=self.top_image1,bg="#F7F6F2",height=100)
        self.top_label1.place(x=1300,y=30)

        self.heading=Label(self.top,text=" Welcome to E-piggy bank",font=("Old English Text MT", 70,"bold"),bg='#F7F6F2')
        self.heading.place(x=250,y=20)

        #==================================buttons
        def time1():
            time_string=time.strftime("%H:%M:%S")
            date_string=time.strftime("%d:%m:%y")
            clock.config(text="Time :"+time_string+"  "+"Date :"+date_string)
            clock.after(200,time1)
        

        self.create_btn=Button(self.bottom,text="Create Account",font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8,command=self.create_acc)
        self.create_btn.place(x=350,y=200)

        self.see_acc = Button(self.bottom,text="View Account",font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8,command=self.view_acc)
        self.see_acc.place(x=350,y=300)

     
        self.withdraw_btn=Button(self.bottom,text="Withdraw money", font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8,command=self.withdraw_acc)
        self.withdraw_btn.place(x=350,y=400)
        

        self.deposite_btn=Button(self.bottom,text="Deposite money", font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8,command=self.deposite_acc)
        self.deposite_btn.place(x=850,y=200)

        self.aboutus=Button(self.bottom,text="About us",font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8)
        self.aboutus.place(x=850,y=300)

        self.exit_btn=Button(self.bottom,text="EXIT",font='arial 20 bold',fg='#FF3F00',bg='#C8C6C6',width=15,anchor=W,relief=RAISED,bd=8,command=self.exit)
        self.exit_btn.place(x=850,y=400)

        clock=Label(self.bottom,font=('time', 25,'bold'),background='#F0E5CF',foreground='black',relief=FLAT,bd=8)
        clock.place(x=500,y=5)
        time1()
    
    def create_acc(self):
        createacc=CreateAcc()
    def view_acc(self):
        accountnumber=Acc_Num()
    def withdraw_acc(self):
        accountnumber=Acc_Num1()

    def deposite_acc(self):
        accountnumber=Acc_Num2()
 
    def exit(self):
        self.master.destroy()
        
    
       

def main():
    root=Tk()
    app=Application(root)
    root.title("E-piggy bank")
    
    root.geometry("1500x800+10+5")
    root.mainloop()

if __name__=="__main__":
    main()