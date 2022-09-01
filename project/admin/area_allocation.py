from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk 
from tkinter import messagebox
import newDatabase
from tkcalendar import Calendar, DateEntry
import viewarea_allocation

class area_allocation:
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
        
        self.lab = Label(self.fr2,text='Area Allocation',font=('impact',30),fg='black',bg='#f5f5f5')
        self.lab.place(x=50,y=30)
        
        self.lab1 = Label(self.fr2,text='City :',font=("Britannic Bold",17),bg='#f5f5f5')
        self.lab1.place(x=35,y=110)
        
        self.cityOptions = newDatabase.assignCity()
        self.cityDrop = Combobox(self.root, values=self.cityOptions)
        self.cityDrop.place(x=370,y=160,height=22)
        
        self.cityDrop.bind("<<ComboboxSelected>>", self.getAreas)

        # self.helper = Entry(self.root,width=30,bg="light grey")
        # self.helper.place(x=370,y=160,height=22)
        
        self.lab2 = Label(self.fr2,text='Area :',font=('Britannic Bold',17),bg='#f5f5f5')
        self.lab2.place(x=35,y=150)

        self.areaOptions = []
        self.areaDrop = Combobox(self.root, values=self.areaOptions, state=DISABLED)
        self.areaDrop.place(x=370,y=200,height=22)
        
        # self.areaentry = Entry(self.root,width=30,bg="light grey")
        # self.areaentry.place(x=370,y=200,height=22)
        
        # self.lab3 = Label(self.fr2,text='Time :',font=('Britannic Bold',17),bg='#f5f5f5')
        # self.lab3.place(x=35,y=190)
        
        # self.time = DateEntry(self.root,width=25,bg="light grey")
        # self.time.place(x=370,y=240,height=22)
        
        self.lab3 = Label(self.fr2,text='Houses :',font=('Britannic Bold',17),bg='#f5f5f5')
        self.lab3.place(x=35,y=190)
        
        self.expHouseEntry = Entry(self.root,width=30,bg="light grey")
        self.expHouseEntry.place(x=370,y=240,height=22)

        self.lab4 = Label(self.fr2,text='Helper :',font=('Britannic Bold',17),bg='#f5f5f5')
        self.lab4.place(x=35,y=230)

        self.voluteerOpt = newDatabase.getVolunteers()
        print(self.voluteerOpt)
        self.volunteerDrop = Listbox(self.root, selectmode= 'multiple')
        self.volunteerDrop.place(x = 370, y = 270, height=80)

        for i in range(len(self.voluteerOpt)):
            self.volunteerDrop.insert(END, self.voluteerOpt[i])
        
        
        btn = Button(self.fr2,text='SUBMIT',command=self.create,width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11))
        btn.place(x=50,y=330)
        
        btn2 = Button(self.fr2,text='CANCEL',width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11) , command=self.root.destroy)
        btn2.place(x=210,y=330)
                
          
        self.my_pic = Image.open('images/area.jpg')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)
        
        self.root.mainloop()
    
    def getAreas(self, e):
        # print(self.cityDrop.get())
        a = list(self.cityDrop.get().split())
        res = newDatabase.getAreass(a[0])
        print(res)
        if res:
            self.areaDrop.delete(0, 'end')
            self.areaDrop.config(state = 'normal')
            # self.areaOptions = [(str(res[0][0]) + ' ' + str(x)) for x in json.loads(res[0][1])]
            self.areaOptions = res
            self.areaDrop.config(values=self.areaOptions)
        else:
            messagebox.showerror('Alert', 'ssssssomething went wrong.')

    def create(self):
        if self.cityDrop.get() == '':
            messagebox.showerror('Alert', 'Please select city')
        elif self.areaDrop.get() == '':
            messagebox.showerror('Alert', 'Please select area')
        # print(self.volunteerDrop.curselection())
        elif len(self.volunteerDrop.curselection()) == 0:
            messagebox.showerror('Alert', 'Please select volunteer')
        elif self.expHouseEntry.get() == '':
            messagebox.showerror('Alert', 'Please enter expected houses')
        else:
            print(self.volunteerDrop.curselection())
            a = [self.voluteerOpt[i][0] for i in self.volunteerDrop.curselection()]
            b = list(self.areaDrop.get().split())
            c = list(self.cityDrop.get().split())
            for i in a:
                self.data = (i, b[0], self.expHouseEntry.get(), c[0])

                res = newDatabase.assignVolunteer(self.data)
                if res:
                    messagebox.showinfo('Success', 'Area assigned successfully.')
                else:
                    messagebox.showerror('Error', 'Something went wrong.')

    
        
if __name__=='__main__':
    obj = area_allocation()
    obj.area()        
          