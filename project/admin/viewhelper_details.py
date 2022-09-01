from tkinter import *
from tkinter.ttk import Treeview
import newDatabase
from tkinter import messagebox
import edithelper_details

class helperview():
    # constructor
    def __init__(self):
        self.root = Toplevel()
        self.root.title('viewhelper_details')

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

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I','J'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=35,stretch=NO)

        self.tr.heading('#1',text="Username")
        self.tr.column('#1',minwidth=0,width=100 ,stretch=NO)

        self.tr.heading('#2', text="Name")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Age")
        self.tr.column('#3', minwidth=0, width=35, stretch=NO)

        self.tr.heading('#4', text="Phone_no")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Address")
        self.tr.column('#5', minwidth=0, width=120, stretch=NO)

        # self.tr.heading('#7', text="City")
        # self.tr.column('#7', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#6', text="Edit")
        self.tr.column('#6', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#7', text="Delete")
        self.tr.column('#7', minwidth=0, width=50, stretch=NO)


        self.tr.place(x=0,y=0,width="800",height="500")
        
        for i in newDatabase.allVolunteer():
            self.tr.insert('', 0, text=i[0], values=(i[1], i[3], i[4], i[5], i[6], 'Edit', 'Delete'))
        
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
        if col == '#7':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = newDatabase.deleteVolunteer(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = helperview()
                    obj.view() 
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#6':
            self.root.destroy()
            obj = edithelper_details.edithelper_details()
            obj.helper(gup)                 

if __name__ == '__main__':
    obj = helperview()
    obj.view()