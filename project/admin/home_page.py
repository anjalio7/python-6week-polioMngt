from tkinter import *
from PIL import Image,ImageTk 

# import database

class home_page:
    def __init__(self):
        self.root=Tk()
        self.root.title('home_page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
        
    def area(self):
        self.fr = Frame(self.root,bg='sky blue')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.lab = Label(self.root,text='Polio Drops',font=('impact',30),fg='black')
        self.lab.place(x=50,y=30)
        
    
        self.btn = Button(self.root,text='START',width=15,height=2,bg='black',fg='white',font=("Britannic Bold",11))
        self.btn.place(x=50,y=270)
        
        self.img=Image.open('images/welcome_polio.jpg')
        self.img1=ImageTk.PhotoImage(self.img)
        self.lab=Label(self.fr,image=self.img1)
        self.lab.place(x=0,y=0)  
        
        # self.my_pic = Image.open('images/welcome_polio.jpg')
        # self.resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        # self.new_pic = ImageTk.PhotoImage(self.resized)
        # self.my_label = Label(self.fr, image=self.new_pic)
        # self.my_label.place(x=0,y=0)
        
        self.root.mainloop()
        
if __name__=='__main__':
    obj = home_page()
    obj.area()        
             