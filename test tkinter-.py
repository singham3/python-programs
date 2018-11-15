from tkinter import *
import time
counter=0
def counter_label():
    counter=0
    def count():
        global counter
        counter += 1
        label.config(text=time.ctime())
        label.after(1000,count)
    count()

root = Tk()
root.title("counting Seconds")
label=Label(root, fg="dark green")
label.pack()
counter_label(label)
button=Button(root, text="STOP", width=25, command=root.distroy)
button.pack()

    

root.mainloop()
