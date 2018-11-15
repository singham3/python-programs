from tkinter import *

from tkinter.ttk import *

root=Tk()
root.title('Redio Button')
root.geometry('350x200')
combo=Combobox(root)
combo['value']=(1,2,3,4,5,'Text')
combo.current(1)
combo.grid(column=0,row=0)

root.mainloop()


