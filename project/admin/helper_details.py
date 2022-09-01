from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import newDatabase
import viewhelper_details
class helper_details:
    def __init__(self):
        self.root=Toplevel()
        self.root.title('helper_details')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
        
    def helper(self):
        self.fr = Frame(self.root,bg='white')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.fr2 = Frame(self.root,bg='white')
        self.fr2.place(x=400,y=0,width=400,height=500)
        
        self.lab = Label(self.fr2,text='Helper Details',font=('impact',30),fg='black',bg='white')
        self.lab.place(x=50,y=30)
        
        self.lab1 = Label(self.fr2,text='Username :',font=("Britannic Bold",17),bg='white')
        self.lab1.place(x=35,y=110)
        
        self.username = Entry(self.fr2,width=30,bg="grey")
        self.username.place(x=165,y=118,height=22)
        
        self.lab2 = Label(self.fr2,text='Password :',font=('Britannic Bold',17),bg='white')
        self.lab2.place(x=35,y=150)
        
        self.password = Entry(self.fr2,width=30,show="*",bg="grey")
        self.password.place(x=165,y=160,height=22)
        
        self.lab3 = Label(self.fr2,text='Name :',font=('Britannic Bold',17),bg='white')
        self.lab3.place(x=35,y=190)
        
        self.name = Entry(self.fr2,width=30,bg="grey")
        self.name.place(x=165,y=200,height=22)
        
        self.lab4 = Label(self.fr2,text='Age :',font=('Britannic Bold',17),bg='white')
        self.lab4.place(x=35,y=230)
        
        self.age = Entry(self.fr2,width=30,bg="grey")
        self.age.place(x=165,y=240,height=22)
        
        self.lab5 = Label(self.fr2,text='Phone_no :',font=('Britannic Bold',17),bg='white')
        self.lab5.place(x=35,y=270)
        
        self.phone_no = Entry(self.fr2,width=30,bg="grey")
        self.phone_no.place(x=165,y=280,height=22)
        
        self.lab6 = Label(self.fr2,text='Address :',font=('Britannic Bold',17),bg='white')
        self.lab6.place(x=35,y=310)
        
        self.address = Entry(self.fr2,width=30,bg="grey")
        self.address.place(x=165,y=320,height=22)
        
        # self.lab7 = Label(self.fr2,text='City :',font=('Britannic Bold',17),bg='white')
        # self.lab7.place(x=35,y=350)
        
        # self.city = Entry(self.fr2,width=30,bg="grey")
        # self.city.place(x=165,y=360,height=22)
        
        btn = Button(self.fr2,text='SUBMIT',width=15,height=1,command=self.details_helper,bg='black',fg='white',font=("Britannic Bold",11))
        btn.place(x=50,y=400)
        
        btn2 = Button(self.fr2,text='CANCEL',width=15,height=1,bg='black',fg='white',font=("Britannic Bold",11), command=self.root.destroy)
        btn2.place(x=210,y=400)
                
          
        self.my_pic = Image.open('images/helper.jpg')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)
        
        self.root.mainloop()
    
    def details_helper(self):
        data =( 
            self.name.get(),
            self.age.get(),
            self.phone_no.get(),
            self.address.get(),
            self.username.get(),
            self.password.get()
        )
        
        if (self.username.get() == ''):
            messagebox.showinfo('Alert', 'Enter your username')
        elif (self.password.get() == ''):
            messagebox.showinfo('Alert', 'Enter your password')
        elif (self.name.get() == ''):
             messagebox.showinfo('Alert', 'Enter your name')
        elif (self.age.get() == ''):
            messagebox.showinfo('Alert', 'Enter your age')
        elif (self.phone_no.get() == ''):
            messagebox.showinfo('Alert', 'Enter your phone_no')
        elif (self.address.get() == ''):
            messagebox.showinfo('Alert', 'Enter your address')          
        else:
            print(data)
            res  = newDatabase.addVolunteer(data)
            if res:
            # #     print(data)
                messagebox.showinfo('Success', 'data added successfully.')
                self.root.destroy()
                obj =viewhelper_details.helperview()
                obj.view()
                
            else:
                messagebox.showinfo("Alert","Something went wrong")
               
        
if __name__=='__main__':
    obj = helper_details()
    obj.helper()        
          