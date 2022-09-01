from tkinter import *
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import newDataWorker, viewAreas


class addHouses:
    def __init__(self):
        self.root=Toplevel()
        self.root.title('House Details')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
        
    def firstFrame(self, volId, areaId):

        self.volId = volId
        self.areadId = areaId

        self.fr = Frame(self.root,bg='white')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.fr2 = Frame(self.root,bg='white')
        self.fr2.place(x=250,y=0,width=550,height=500)
        
        self.lab = Label(self.fr2,text='Add House Details',font=('impact',30),fg='black',bg='white')
        self.lab.place(x=50,y=30)


        self.lab1 = Label(self.fr2,text='Area :',font=("Britannic Bold",17),bg='white')
        self.lab1.place(x=35,y=110)

        self.areaEntry = Entry(self.fr2)
        self.areaEntry.place(x=165,y=118,height=22)
        res = newDataWorker.getArea(self.areadId)
        if res:
            self.areaEntry.insert(0, res[0])
            self.areaEntry.config(state='readonly')
        else:
            messagebox.showerror('Alert', 'Something went wrong.')
        
        

        self.addressLabel = Label(self.fr2, text='Address', font=("Britannic",15),bg='white')
        self.addressLabel.place(x = 35, y = 170)

        self.childLabel = Label(self.fr2, text='No. of children', font=("Britannic",15),bg='white')
        self.childLabel.place(x = 150, y = 170)

        self.numDoses = Label(self.fr2, text='Doses given', font=("Britannic",15),bg='white')
        self.numDoses.place(x = 300, y = 170)

        self.addBtn = Button(self.fr2, text='Add', command=self.addAreas, bg='black', fg = 'white')
        self.addBtn.place(x = 450, y = 170)


        self.btn = Button(self.fr2, text="Add Houses", command = self.area)
        self.btn.place(x = 200, y = 350)

        self.xPos = 35
        self.yPos = 210
        self.i = 0


        self.my_pic = Image.open('images/children1.webp')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)

        self.root.mainloop()

    
    def addAreas(self):

        

        # globals()[f"self.areaLabel{self.i}"] = Label(self.frame1, text='Area Name')
        # globals()[f"self.areaLabel{self.i}"].place(x = self.xPos, y = self.yPos)

        globals()[f"self.addressEntry{self.i}"] = Entry(self.fr2)
        globals()[f"self.addressEntry{self.i}"].place(x = self.xPos, y = self.yPos, width = '90')

        globals()[f"self.childEntry{self.i}"] = Entry(self.fr2)
        globals()[f"self.childEntry{self.i}"].place(x = self.xPos + 115, y = self.yPos, width = '90')

        globals()[f"self.dosesEntry{self.i}"] = Entry(self.fr2)
        globals()[f"self.dosesEntry{self.i}"].place(x = self.xPos + 265, y = self.yPos, width = '90')

        globals()[f"self.removeBtn{self.i}"] = Button(self.fr2, text= 'x', bg='black', fg = 'white', command = lambda j = self.i : self.getIndex(j))
        globals()[f"self.removeBtn{self.i}"].place(x = self.xPos + 415, y = self.yPos)

        self.yPos += 50
        
        self.i += 1 


    def getIndex(self, j):
        self.i -= 1
        print(j)
        globals()[f"self.addressEntry{j}"].destroy()
        globals()[f"self.childEntry{j}"].destroy() 
        globals()[f"self.dosesEntry{j}"].destroy() 
        globals()[f"self.removeBtn{j}"].destroy()

        # self.yPos -= 20

    def area(self):
        print(self.i)
        dataList = []
        for i in range(self.i):
            if globals()[f'self.addressEntry{i}'].get() == '':
                messagebox.showerror('Alert', 'Please enter address')
            elif globals()[f'self.childEntry{i}'].get() == '':
                messagebox.showerror('Alert', 'Please enter number of children')
            elif globals()[f'self.dosesEntry{i}'].get() == '':
                messagebox.showerror('Alert', 'Please enter number of doses given')
            else:
                dataList.append((globals()[f'self.addressEntry{i}'].get(), globals()[f'self.childEntry{i}'].get(), globals()[f'self.dosesEntry{i}'].get()))
        # print(self.cityEntry.get())

        if self.i == 0:
            messagebox.showerror('Alert', 'Please add areas names')
        else:
            a = False
            # a = list(self.cityEntry.get().split())
            for i in dataList:
                self.data = (self.areadId[0], i[0], i[1], i[2], self.volId[0])
                print(self.data)

                res = newDataWorker.addHouses(self.data)
                if res:
                    messagebox.showinfo('Success', 'Houses added successfully.')
                    a  = True
                else:
                    a = False
            
            if a:
                self.root.destroy()
                obj = viewAreas.ViewArea()
                obj.firstFrame(self.volId)
            else:
                messagebox.showerror('Alert', 'something went wrong')

        

if __name__ == "__main__":
    obj = addHouses()
    obj.firstFrame()