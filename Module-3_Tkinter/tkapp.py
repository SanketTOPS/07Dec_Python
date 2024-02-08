import tkinter
from tkinter import ttk



window=tkinter.Tk()
window.title("FirstApp")
window.geometry("400x500")
window.config(bg='orange')

#tkinter.Label(text='Firstname:').pack()

lblfnm=tkinter.Label(text='Firstname:',bg='orange',fg='blue',font='Aptos 12 bold')
#lblfnm.pack()
#lblfnm.place(x=0,y=0)
lblfnm.grid(row=0,column=0,sticky='W')

lbllnm=tkinter.Label(text='Lastname:',bg='orange',fg='blue',font='Aptos 12 bold')
#lbllnm.pack()
#lbllnm.place(x=0,y=30)
lbllnm.grid(row=1,column=0,sticky='W')

txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')

txtlnm=tkinter.Entry()
txtlnm.grid(row=1,column=1,sticky='W')

male=tkinter.Radiobutton(value=0, text="Male",bg='orange',fg='blue',font='Aptos 12 bold')
male.grid(row=2,column=0,sticky='W')

female=tkinter.Radiobutton(value=1,text="Female",bg='orange',fg='blue',font='Aptos 12 bold')
female.grid(row=2,column=1,sticky='W')

ch1=tkinter.Checkbutton(text='Python',bg='orange',fg='blue',font='Aptos 12 bold')
ch1.grid(row=3,column=0,sticky='W')

ch2=tkinter.Checkbutton(text='Java',bg='orange',fg='blue',font='Aptos 12 bold')
ch2.grid(row=4,column=0,sticky='W')

ch3=tkinter.Checkbutton(text='PHP',bg='orange',fg='blue',font='Aptos 12 bold')
ch3.grid(row=5,column=0,sticky='W')

ch4=tkinter.Checkbutton(text='React',bg='orange',fg='blue',font='Aptos 12 bold')
ch4.grid(row=6,column=0,sticky='W')

city=['Ahemedabad','Rajkot','Baroda','Surat','Jamnagar']
ct=ttk.Combobox(values=city)

ct.grid(row=7,column=0,sticky='W')

def btnclick():
    #print("Button clicked..")
    print("Firstname:",txtfnm.get())
    print("Lastname:",txtlnm.get())


btn=tkinter.Button(text='Submit',font='Aptos 12 bold',command=btnclick)
#btn.grid(row=10,column=0)
btn.place(x=180,y=270)

window.mainloop()