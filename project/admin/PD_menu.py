from tkinter import *
from PIL import Image , ImageTk

import addCity, manageCity
import addArea, manageArea
import area_allocation, viewarea_allocation

# import health_worker
# import viewhealth_worker

import area_allocation
import viewarea_allocation

import helper_details
import viewhelper_details

# import children_details
# import viewchildren_details

class menu:
    def __init__(self):
        self.root=Tk()
        self.root.title("Menu")
        
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
    
    
        self.menubar = Menu(self.root)

        self.city = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='City', menu = self.city)
        self.city.add_command(label ='Add', command = self.addCity)
        self.city.add_command(label ='Manage', command = self.manageCity)

        self.area_allocation = Menu(self.menubar)
        self.menubar.add_cascade(label="Area",menu=self.area_allocation)
        self.area_allocation.add_command(label="Add",command=self.area)
        self.area_allocation.add_command(label="view",command=self.viewarea)

        # self.health_worker = Menu(self.menubar)
        # self.menubar.add_cascade(label="Health worker",menu=self.health_worker)
        # self.health_worker.add_command(label="Add",command=self.health)
        # self.health_worker.add_command(label="view",command=self.viewhealth)
        
        
        
        self.helper_details = Menu(self.menubar)
        self.menubar.add_cascade(label="Helper",menu=self.helper_details)
        self.helper_details.add_command(label="Add",command=self.helper)
        self.helper_details.add_command(label="view",command=self.viewhelper)
        
        self.children_details = Menu(self.menubar)
        self.menubar.add_cascade(label="Assign Area",menu=self.children_details)
        self.children_details.add_command(label="Add",command=self.assignArea)
        self.children_details.add_command(label="view",command=self.manageAssign)
            
        self.logout = Menu(self.menubar)
        self.menubar.add_cascade(label="Logout",command=self.root.destroy)

        self.root.config(menu=self.menubar,height=25)

    def addCity(self):
        obj = addCity.addCity()
        obj.area()
    
    def manageCity(self):
        obj = manageCity.cityview()
        obj.view()
        
    def health(self):
        # self.root.destroy()
        obj = health_worker.health_worker ()
        obj.register() 
        
    def viewhealth(self):
        # self.root.destroy()
        obj = viewhealth_worker.healthview()
        obj.view() 
        
    def area(self):
        # self.root.destroy()    
        obj = addArea.city()
        obj.area()  
        
    def viewarea(self):
        # self.root.destroy()   
        obj = manageArea.areaView()
        obj.view() 
          
    def helper(self):
        # self.root.destroy()
        obj = helper_details.helper_details()
        obj.helper()  
        
    def viewhelper(self):
        # self.root.destroy()
        obj = viewhelper_details.helperview()
        obj.view()  
          
    def assignArea(self):
        # self.root.destroy()
        obj = area_allocation.area_allocation()
        obj.area() 
        
    def manageAssign(self):
        # self.root.destroy()
        obj = viewarea_allocation.area_allocationview()
        obj.view()
    
    
    def features(self):
        self.fr = Frame(self.root)
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.my_pic = Image.open('images/menu.png')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)
        self.root.mainloop()

if __name__=='__main__':
    obj = menu()
    obj.features()