from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk 
from tkinter import messagebox
import newDatabase, manageArea

class editArea:
    def __init__(self):
        self.root=Toplevel()
        self.root.title('city')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
        
    def area(self, id):
        self.id = id
        self.fr = Frame(self.root,bg='blue')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.fr2 = Frame(self.root,bg='#f5f5f5')
        self.fr2.place(x=210,y=55,width=350,height=350)
        
        self.lab = Label(self.fr2,text='Area Details',font=('impact',35),fg='black',bg='#f5f5f5')
        self.lab.place(x=80,y=30)
        
        self.lab1 = Label(self.fr2,text='City :',font=("Britannic Bold",25),bg='#f5f5f5')
        self.lab1.place(x=35,y=110)
        
        # self.areaentry = Entry(self.fr2,width=30,bg="light grey")
        # self.areaentry.place(x=130,y=125,height=24)

        self.options = newDatabase.allCityForArea()
        self.cityDrop = Combobox(self.fr2, values=self.options, width=30)
        self.cityDrop.place(x=130,y=125,height=24)
        
        self.lab2 = Label(self.fr2,text='Area :',font=('Britannic Bold',25),bg='#f5f5f5')
        self.lab2.place(x=35,y=170)
        
        self.city = Entry(self.fr2,width=30,bg="light grey")
        self.city.place(x=130,y=185,height=24)
        
        self.btn = Button(self.fr2,text='SUBMIT',width=15,height=2,command=self.create,bg='black',fg='white',font=("Britannic Bold",11))
        self.btn.place(x=35,y=270)
        
        self.btn2 = Button(self.fr2,text='CANCEL',width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11), command=self.root.destroy)
        self.btn2.place(x=190,y=270)
                
          
        self.my_pic = Image.open('images/city2.webp')
        resized = self.my_pic.resize((800,600), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)

        res = newDatabase.singleArea(self.id)
        if res:
            self.cityDrop.insert(0, (res[0], res[1]))
            self.city.insert(0, res[2])
        else:
            messagebox.showerror('Alert', 'Something went wrong.')
        
        self.root.mainloop()
    
    def create(self):
        data = (
            self.cityDrop.get(),
            self.city.get(),
            self.id[0]
        )
        

        if (self.cityDrop.get() == ''):
            messagebox.showinfo('Alert', 'select city ')
        elif (self.city.get() == ''):
            messagebox.showinfo('Alert', 'Enter area')
                    
        else:
            print(data)
            res  = newDatabase.editArea(data)
            if res:
            # #     print(data)
                messagebox.showinfo('Success', 'area updated successfully.')
                self.root.destroy()
                obj =manageArea.areaView()
                obj.view()
                
            else:
                messagebox.showinfo("Alert","Something went wrong")
        
        
if __name__=='__main__':
    obj = editArea()
    obj.area()        
          