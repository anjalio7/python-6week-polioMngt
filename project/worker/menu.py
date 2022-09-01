from tkinter import *
from PIL import Image , ImageTk
import viewAreas

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

        # self.home = Menu(self.menubar)
        # self.menubar.add_cascade(label="Home",menu=self.home)

        self.health_worker = Menu(self.menubar)
        self.menubar.add_cascade(label="Assigned Area", menu=self.health_worker)
        # self.health_worker.add_command(label="Add")
        self.health_worker.add_command(label="view", command=self.viewAreas)
        
        # self.area_allocation = Menu(self.menubar)
        # self.menubar.add_cascade(label="Area")
        # self.area_allocation.add_command(label="Add")
        # self.area_allocation.add_command(label="view")
        
        # self.helper_details = Menu(self.menubar)
        # self.menubar.add_cascade(label="Helper")
        # self.helper_details.add_command(label="Add")
        # self.helper_details.add_command(label="view")
        
        # self.children_details = Menu(self.menubar)
        # self.menubar.add_cascade(label="Children")
        # self.children_details.add_command(label="Add")
        # self.children_details.add_command(label="view")
            
        self.logout = Menu(self.menubar)
        self.menubar.add_cascade(label="Logout",command=self.root.destroy)

        self.root.config(menu=self.menubar,height=25)
        

    def viewAreas(self):
        obj = viewAreas.ViewArea()
        obj.firstFrame(self.id)

    
    def features(self, id):
        self.id = id 
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