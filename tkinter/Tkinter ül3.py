# Roomet Altmäe 06.02.23
# Ülesanne 3 Tkinter
"""
Sinu ülesandeks on luua Tkinteri abiga samasugune programmiaken
akna suurus muutub automaatselt vastavalt sisule
akent ei ole võimalik teha suuremaks ega väiksemaks
programmi tiitellribal on nimi ja muudetud on ikoon
akna sisuks on sinu nimi, kursus ja aasta
teksti värv on muudetud, kaldus, paksult ja font Tahoma
tekst hoiab seinast eemale
tausta värv muudetud
"""
from tkinter import *

aken = Tk()
aken.title("Minu Esimene aken")
aken.resizable(False,False)
aken.configure(background='black')
tekst = Label(aken,fg="red",bg="black",font="Tahoma 16 bold italic", text="Nimi: Roomet Altmäe\nRühm: IT-23\n2023", justify=CENTER)
tekst.pack(pady="20",padx="20")
aken.mainloop()
