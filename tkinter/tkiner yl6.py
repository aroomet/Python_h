# Roomet Altmäe
# 16.02.24
# IT-23


from tkinter import *

# akna seaded
aken = Tk()
aken.title('Joonistamine')

#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(10,20,500,200, fill="white")
louend.create_rectangle(10,200,500,400, fill="red")

louend.create_arc(100,100,300,300, extent=180, fill="red")
louend.create_arc(100,100,300,300, extent=-180, fill="white")

# teksti loomine

louend.create_text(250,420, text="Gröönimaa", fill="black", font=("Arial", 20, "bold"))


# pildi lisamine
minu_pilt = PhotoImage(file='groonimaa.jpg')
louend.create_image(0, 0, anchor=NW, image=minu_pilt)

aken.mainloop()