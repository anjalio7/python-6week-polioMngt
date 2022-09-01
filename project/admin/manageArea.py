from tkinter import *
from tkinter.ttk import Treeview
import newDatabase
from tkinter import messagebox
import editArea

class areaView():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('viewcity')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def view(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E','F' ), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=50,stretch=NO)
        
        self.tr.heading('#1',text="City")
        self.tr.column('#1',minwidth=0,width=150,stretch=NO)

        self.tr.heading('#2',text="Area")
        self.tr.column('#2',minwidth=0,width=100 ,stretch=NO)

        self.tr.heading('#3', text="Edit")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#4', text="Delete")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.place(x=0,y=0,width="800",height="500")
         
        for i in newDatabase.allAreas():
            self.tr.insert('',0,text=i[0],values=(i[1],i[2],'Edit','Delete'))
        
        self.tr.place(x=0,y=0,width="800",height="500")
        self.tr.bind('<Double-Button-1>',self.actions)  

        self.root.mainloop()
    
    def actions(self,e):
        # print("i am e",e)
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        # print("i am gup",gup)
        if col == '#4':
            res = messagebox.askyesno("Delete", "Do You Really Want to delete this item.")
            if res:
                a = newDatabase.deleteAreas(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = areaView()
                    obj.view() 
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#3':
            self.root.destroy()
            obj = editArea.editArea()
            obj.area(gup)        
                 
               

if __name__ == '__main__':
    obj = areaView()
    obj.view()