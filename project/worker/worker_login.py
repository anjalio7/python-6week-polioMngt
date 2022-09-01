from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import newDataWorker
import menu

class workerlogin_page:
    def __init__(self):
        self.root=Tk()
        self.root.title('worker login page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        
        self.width =int((self.fullwidth-800)/2)
        self.height =int((self.fullheight-500)/2)
        
        s="800x500+"+str(self.width)+"+"+str(self.height)
        
        self.root.geometry(s)
        
        self.root.resizable(False,False)
    def login(self):
        self.fr = Frame(self.root,bg='blue')
        self.fr.place(x=0,y=0,width=800,height=500)
        
        self.fr2 = Frame(self.root,bg="#f5f5f5")
        self.fr2.place(x=50,y=80,width=370,height=350)
        
        self.lab = Label(self.fr2,text='Login Here',font=('impact',35,'bold'),fg='black',bg='#f5f5f5')
        self.lab.place(x=80,y=20)
        
        self.lab1 = Label(self.fr2,text='Username :',font=("Britannic Bold",20),fg='black',bg='#f5f5f5')
        self.lab1.place(x=60,y=100)
        
        self.username = Entry(self.fr2,width=40,bg="light grey")
        self.username.place(x=60,y=155,height=30)
        
        self.lab2 = Label(self.fr2,text='Password :',font=('Britannic Bold',20),fg='black',bg='#f5f5f5')
        self.lab2.place(x=60,y=190)
        
        self.password = Entry(self.fr2,show="*",width=40,bg ="light grey")
        self.password.place(x=60,y=235,height=30)
        
        btn = Button(self.fr2,text='SUBMIT',width=15,height=1,command=self.log,bg='black',fg='#f5f5f5',font=("Britannic Bold",12))
        btn.place(x=110,y=290)
        
        self.my_pic = Image.open('images/log.webp')
        resized = self.my_pic.resize((800,500), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.my_label = Label(self.fr, image=self.new_pic)
        self.my_label.place(x=0,y=0)
        
        self.root.mainloop()
        
    def log(self): 
        data = (
            self.username.get(),
            self.password.get()
        )
        if self.username.get()=="":
            messagebox.showerror("Alert",'enter your username')
        elif self.password.get()=="":
            messagebox.showerror("Alert",'enter your password')
        else:
            # print(data)
            res = newDataWorker.login(data)
            if res:
                messagebox.showinfo('success','LOGIN successfully')
                
                self.root.destroy()
                obj= menu.menu()
                obj.features(res[0])
            else:
                messagebox.showerror('Alert',"Invalid username and/or password")
                
   
if __name__=='__main__':
    obj = workerlogin_page()
    obj.login()        
          