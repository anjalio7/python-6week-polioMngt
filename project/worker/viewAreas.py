from tkinter import *
from tkinter.ttk import Treeview
import newDataWorker, addHouses, viewDetails
from tkinter import messagebox

class ViewArea():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('viewarea_allocation')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def firstFrame(self, id):

        self.id = id

        self.frame1 = Frame(self.root)
        self.frame1.place(x = 0, y = 0, width=800, height=500)

        self.tr = Treeview(self.frame1, columns=('A', 'B', 'C', 'E', 'F', 'G'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="City Name")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Area")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Expected Houses")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#4', text="View Details")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Add Details")
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)

        # self.tr.heading('#5', text="Delete")
        # self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        j = 0
        print(newDataWorker.viewAssignedArea(self.id))
        for i in newDataWorker.viewAssignedArea(self.id):
            self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], 'View Details', 'Add details'))
            j += 1
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0, width=800, height=500)

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
            obj = addHouses.addHouses()
            obj.firstFrame(volId = self.id, areaId = gup)

        if col == '#4':
            obj = viewDetails.ViewDetails()
            obj.firstFrame(volId = self.id, areaId = gup)


if __name__ == "__main__":
    obj = ViewArea()
    obj.firstFrame()