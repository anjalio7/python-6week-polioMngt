from tkinter import *
from tkinter.ttk import Treeview
import newDataWorker, addHouses, viewDetails
from tkinter import messagebox

class ViewDetails():
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

    def firstFrame(self, volId, areaId):

        self.volId = volId
        self.areadId = areaId

        self.frame1 = Frame(self.root)
        self.frame1.place(x = 0, y = 0, width=800, height=500)

        self.tr = Treeview(self.frame1, columns=('A', 'B', 'C', 'E', 'F', 'G'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="House Address")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Number of Children")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Doses given")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#4', text="Covered By")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        

        j = 0
        print(newDataWorker.viewHouses(self.volId, self.areadId))
        for i in newDataWorker.viewHouses(self.volId, self.areadId):
            self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4]))
            j += 1
        # create double action button
        # self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0, width='800', height='500')

        self.root.mainloop()

if __name__ == "__main__":
    obj = ViewDetails()
    obj.firstFrame()