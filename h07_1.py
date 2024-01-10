#funktsioonid
#5.12.23
#R.Altmäe
"""
RUUMALA ARVUTAMINE
"""

import math

#programm ruumala arvutamiseks
def kuup(a,b,c):
    v = a*b*c
    print(f"Kera ruumala on: {v}")
    print("kuup")

def kera(r):
    v= round(4*math.pi*r**2,2)
    print(f"kera ruumala on: {v}")

def koonus():
    print("koonus")

def silinder():
    print("silinder")

loop = 1
print("n-------------------\Matemaatika funktsioonid\n----------------")
while loop == 1:
    print("Vali kujund:\n1 Kera\n2 Kuup\n3 Koonus\n4 Silinder\n5 EXIT\n--------")
    valik = int(input("Tee valik : "))

    if valik ==1:
        r= int(input("Sisesta kera raadius: "))
        kera(r)
    elif valik == 2:
        a = int(input("Lisa kuubi külg 1: "))
        b = int(input("Lisa kuubi külg 2: "))
        c = int(input("Lisa kuubi külg 3: "))
        kuup(a,b,c)
    elif valik ==5:
        print("Headaega!")
        exit



"""
"""
def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"Hi {nimi}!")
    elif keel == "et":
        print(f"Tere {nimi}!")
    else:
        print(f"Hallo {nimi}!")

tervita ("Jüri","en")
tervita("Jüri")
"""
"""
