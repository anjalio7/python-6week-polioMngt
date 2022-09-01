from tkinter import *
from tkinter.ttk import Treeview
import newDatabase
from tkinter import messagebox
import area_allocation
# import editarea_allocation
class area_allocationview():
    # constructor
    def __init__(self):
        self.root = Toplevel()
        self.root.title('viewarea_allocation')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def view(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(x = 0, y = 0, width=800, height=400)

        self.tr = Treeview(self.frame1, columns=('A', 'G', 'B', 'C', 'D', 'E'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Volunteer")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="City")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Area")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#4', text="Expected Houses")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        # self.tr.heading('#5', text="Edit")
        # self.tr.column('#5', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Delete")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        j = 0
        print(newDatabase.allAssignArea())
        for i in newDatabase.allAssignArea():
            self.tr.insert('', 0, text=i[0], values=(i[1], i[4], i[2], i[3], 'Delete'))
            j += 1
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0)

        self.root.mainloop()

    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#5':
            res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
            if res:
                rs = newDatabase.deleteAssignArea(gup)
                if rs:
                    messagebox.showinfo("ALERT", "Suuccessfully Deleted")
                    self.root.destroy()
                    obj = area_allocationview()
                    obj.view()
               

if __name__ == '__main__':
    obj = area_allocationview()
    obj.view()