
# Roomet Altmäe
# 18.12.2023
import winsound
import random
"""
Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. Koosta programm, mis

    küsib kasutajalt, mitu korda äratus heliseb ning
    väljastab sama arv kordi ekraanile Tõuse ja sära!
"""

def aratus (nr):
    for i in range(nr):
        winsound.Beep(2500,200)
        print("Tõuse ja sära!")

"""
Jänestevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja 
süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 
progandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel
porgandeid juurde ei saa.

Koostada programm, mis
    küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
    arvutab while-tsükli abil saadavate porgandite koguarvu;
    väljastab saadavate porgandite koguarvu ekraanile.
"""

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid += joostud_ringid
    print(f"Jänkukene saab: {porgandid} porgandit!")

"""
Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks
on vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koosta programm, mis
    küsib kasutajalt vajalike täringute arvu;
    viskab vastava arvu täringuid
    väljastab iga arvu eraldi reale
"""

def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))

"""
Male
"""
def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut +=1
    print(nisuterad)

    """
Õunad
"""

def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad -=pounad
        print(pounad)
    print(F"Lumivalgekesekesekele jäi {ounad} õuna")

# kordused = int(input("Äratuste arv : "))
# aratus(kordused)

# ringid = int(input("Ringide arv : "))
# porgandid(ringid)

# taringud(6)

# male(5)

lumivalgeke(6)