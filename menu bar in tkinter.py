from tkinter import *
from tkinter import scrolledtext

root=Tk()
root.geometry('800x600')


m=Menu(root,bg='#F0F0F0')
root.config(menu=m)
subn1=Menu(m)
m.add_cascade(label='File', menu=subn1)
subn1.add_command(label='New',compound=RIGHT)
subn1.add_command(label='Open...',compound=RIGHT)
subn1.add_command(label='Save',compound=RIGHT)
subn1.add_command(label='Save As...',compound=RIGHT)
subn1.add_command(label='Page Setup...',compound=RIGHT)
subn1.add_command(label='Print',compound=RIGHT)
subn1.add_command(label='Exit',compound=RIGHT)

subn2=Menu(m)
m.add_cascade(label='Edit', menu=subn2,compound=RIGHT)
subn2.add_command(label='Undo')
subn2.add_command(label='Cut')
subn2.add_command(label='copy')
subn2.add_command(label='Psste')
subn2.add_command(label='Delete')
subn2.add_command(label='Find..')
subn2.add_command(label='Find Next')
subn2.add_command(label='Replace...')
subn2.add_command(label='Go To...')
subn2.add_command(label='Select All')
subn2.add_command(label='Time/Date')

subn3=Menu(m)
m.add_cascade(label='Format', menu=subn3,compound=RIGHT)
subn3.add_command(label='Word Wrap')
subn3.add_command(label='Font...')

subn4=Menu(m)
m.add_cascade(label='View', menu=subn4,compound=RIGHT)
subn4.add_command(label='Status Bar')

subn5=Menu(m)
m.add_cascade(label='Help', menu=subn5,compound=RIGHT)
subn5.add_command(label='View Help')
subn5.add_command(label='About Notepad')

txt=scrolledtext.ScrolledText(root,width=40,height=10,bd=0,bg='#F0F0F0')
txt.pack(expand=YES,fill=BOTH)

root.mainloop()
