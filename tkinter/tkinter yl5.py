# Roomet Altmäe 16.02.24
# IT-23

from tkinter import *
from tkinter import ttk
#akna seaded

aken = Tk()
aken.title('KM kalkulaator')
aken.geometry("350x250")

#funktsioonid
def arvuta():
    hind = float(sisestus.get())
    km = var.get()/100
    arvutus = hind + hind * km
    print(arvutus)
    valjund1.config(text=str(km*hind)+"€")
#rida1
silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=0,column=0)

sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
#rida2-3
silt2 = Label(aken, text="Käibemaksumäär:")
silt2.grid(row=1,column=0)

var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=2, column=1)

#rida 4
joon = ttk.Separator(aken, orient='horizontal')
joon.grid(row=3, column=0, ipadx = 100)

#rida5
silt3 = Label(aken, text="Käibemaks")
silt3.grid(row=4,column=0)

valjund1 = Label(aken, text="0.00€")
valjund1.grid(row=4,column=1)

#rida6
silt4= Label(aken, text="Hind käibemaksuga")
silt4.grid(row=5,column=0)

valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=5,column=1)

#nupud
nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=6, column=1)

aken.mainloop()