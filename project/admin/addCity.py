from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
import newDatabase
from tkcalendar import Calendar, DateEntry
import manageCity


class addCity:
    def __init__(self):
        self.root=Toplevel()
        self.root.title('area_allocation')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
        
    def area(self):
        self.fr = Frame(self.root,bg='blue')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.fr2 = Frame(self.root,bg='#f5f5f5')
        self.fr2.place(x=200,y=45,width=400,height=400)
        
        self.lab = Label(self.fr2,text='Add City',font=('impact',30),fg='black',bg='#f5f5f5')
        self.lab.place(x=50,y=30)
        
        self.lab1 = Label(self.fr2,text='Name :',font=("Britannic Bold",17),bg='#f5f5f5')
        self.lab1.place(x=35,y=110)
        
        self.name = Entry(self.root,width=30,bg="light grey")
        self.name.place(x=370,y=160,height=22)
        
        self.lab2 = Label(self.fr2,text='State :',font=('Britannic Bold',17),bg='#f5f5f5')
        self.lab2.place(x=35,y=150)
        
        self.state = Entry(self.root,width=30,bg="light grey")
        self.state.place(x=370,y=200,height=22)
        
        # self.lab3 = Label(self.fr2,text='Time :',font=('Britannic Bold',17),bg='#f5f5f5')
        # self.lab3.place(x=35,y=190)
        
        # self.time = DateEntry(self.root,width=25,bg="light grey")
        # self.time.place(x=370,y=240,height=22)
        
        # self.lab3 = Label(self.fr2,text='Dose :',font=('Britannic Bold',17),bg='#f5f5f5')
        # self.lab3.place(x=35,y=190)
        
        # self.dose = Entry(self.root,width=30,bg="light grey")
        # self.dose.place(x=370,y=240,height=22)
        
        
        btn = Button(self.fr2,text='SUBMIT',command=self.create,width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11))
        btn.place(x=50,y=270)
        
        btn2 = Button(self.fr2,text='CANCEL',width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11), command=self.root.destroy)
        btn2.place(x=210,y=270)
                
          
        self.my_pic = Image.open('images/area.jpg')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)
        
        self.root.mainloop()
    
    def create(self):
        data = (
            self.name.get(),
            self.state.get()
        )
        

        if (self.name.get() == ''):
            messagebox.showinfo('Alert', 'Enter helper')
        elif (self.state.get() == ''):
            messagebox.showinfo('Alert', 'Enter area')
                    
        else:
            print(data)
            res  = newDatabase.cityAdd(data)
            if res:
            # #     print(data)
                messagebox.showinfo('Success', 'area allocated successfully.')
                self.root.destroy()
                obj =manageCity.cityview()
                obj.view()
                
            else:
                messagebox.showinfo("Alert","Something went wrong")
        
        
if __name__=='__main__':
    obj = addCity()
    obj.area()        
          