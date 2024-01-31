#	Python iseseisvad tööd (PAARITUD)
# Roomet Altmäe 31.01.24

# Korrutamise kontrollimine
#	programm esitab korrutustehte 1p
#	ootab kasutajalt vastuse sisestamist 1p
#	kontrollib vastuse Ćµigsust 1p
#	väljastab, kas vastus oli õige või väär. 1p
#	kokku antakse lahendamiseks 10 ülesannet. 1p

#import random
#õiged_vastused= 0

#for i in range(10):
#    number = random.randint(1, 10)
#    number2 = random.randint(1, 10) 
#   vastus = int(input(f"{number} * {number2} = "))
#    if vastus == number * number2:
#        print("Õige!")
#        õiged_vastused += 1
#    else:
#        print(f"Vale! Õige vastus oli: {number * number2}")

#    print(f"\nKokku sai õigeid vastuseid {õiged_vastused}/10.")


#---------------------
    #3. Positiivsed ja negatiivsed
	#tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
	#kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
	#nulli lisamisel ei tehta midagi 1p
	#vĆ¤ljasta mĆµlemad loendit 1p
# 

#positiivsed = []
#negatiivsed = []
#for i in range(5):
#    arv = int(input("Sisesta arv:"))
#
#    if arv > 0:
#        positiivsed.append(arv)
#    elif arv < 0:
#        negatiivsed.append(arv)
#
#    print(f"\nPositiivsed:",positiivsed)
#
#    print(f"Negatiivsed: ",negatiivsed)

#Shopping List
#	Create a program that will keep track of items for a shopping list. 
# The program should keep asking for new items until nothing is entered (no input followed by enter/return key).
#     The program should then display the full shopping list.
# 



#poe_nimekiri = []

#while True:
#    valik = input("Sisesta toode: ")
#    if valik  == "":
#        break
#    poe_nimekiri.append(valik)
#print("------------Ostukorv------------")
#for i in poe_nimekiri:
#    print(i)

#7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
#	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
#	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
#	kĆ¼sitakse valuuta kogust ja tehakse arvutused - 2p
#	kood kommenteeritud - 1p

#def eurokalkulaator():
#    print("Eurokalkulaator")
#    print("Kas soovite teisendada EUR->EEK või EEK->EUR siis EEK?") # Küsib kasutajalt, kas ta soovib eurodes või kroonides
#    valik = input("Sisesta oma valik: ") # Kasutaja sisestab oma valiku
#    if valik == "EUR": # summa eur
#        summa = int(input("Sisesta summa eurodes: "))
#        print(summa*15.6466) # Summa kroonidesse teisendatud
#    elif valik == "EEK": # Summa kroonides
#        summa = int(input("Sisesta summa kroonides: "))
#        print(summa/15.6466, "€") # Summa Eurodesse teisendatud
#    else:
#        print("Õpi lugema!")
#eurokalkulaator()


	
#9. Emaili kontroll
#	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
#programm tükeldab selle ja väljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com - 1p
#	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
#	kood kommenteeritud - 1p

#def email():
#    email = input("Sisesta email: ")
#    if "@" in email:
#        print("Tere " + email.split("@")[0].split(".")[0] + ", sinu email on serveris " + email.split("@")[1].split(".")[0] + " ja domeeniks on sul " + email.split("@")[1].split(".")[1])
#    else:
#        print("Vale email!")
#email()


# 11. Salakeel
#	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
#	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
#	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
#	kood kommenteeritud - 1p


#def salakeel():
#    keel = {"a":"e", "b":"t", "c":"m", "d":"v", "e":"a", "f":"p", "g":"r", "h":"y", "i":"õ", "j":"ä", "k":"o", "l":"ü", "m":"c", "n":"d", "o":"k", "p":"f", "q":"w", "r":"g", "s":"z", "t":"b", "u":"õ", "v":"h", "w":"q", "x":"j", "y":"h", "z":"s", "õ":"i", "ä":"u", "ö":"x", "ü":"l"}
#    print("Kas soovid salakeelt luua või tõlkida?")
#    valik = input("Sisesta oma valik: ")
#    if valik == "luua":
#        sona = input("Sisesta sõna, mis soovid salakeelde muuta: ")
#        salasona = ""
#        for i in sona:
#            salasona += keel[i]
#        print(salasona)
#    elif valik == "tõlkida":
#        salasona = input("Sisesta sõna, mis soovid salakeelest tõlkida: ")
#        sona = ""
#        for i in salasona:
#            for key,value in keel.items():
#                if value == i:
#                    sona += key
#        print(sona)
#    else:
#        print("Õpi lugema!")
#salakeel()

# 13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
#	kuvatakse korrektne arusaadav küsimus ja  vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 2p
#	kood mis teavitab paaris või paaritust arvust - 2p
#	kuvatakse programmi pealkiri - 1p

#def paaris_paaritu_kontroll():
#    print("Paaris või paaritu arvu kontrollija")
#
#    try:
#        arv = int(input("Sisesta arv: "))
#    except ValueError:
#        print("Valesti sisestatud.")
#        return
#
#    if arv == 0:
#        print("Arv on 0.")
#    elif arv % 2 == 0:
#        print(f"{arv} on paaris arv.")
#    else:
#        print(f"{arv} on paaritu arv.")

#paaris_paaritu_kontroll()

# ---------------------


#15. Temperatuurid - Programm peab töötlema ühe aasta kõigi päevade temperatuure. Kirjutada programm
#, mis leiab kuude kaupa, mitmendal kuupĆ¤eval oli kĆµige soojem. Väljasta kuupäev ja vastav temperatuur. 
#(Kui sama temperatuuriga oli mitu päeva, väljasta vĆ¤hemalt üks)


kuud=[["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3],
	["veebruar",-9,-2,-7,1,-16,-19,-19,-11,-16,-15,-9,-2,-16,-4,-20,-5,-6,-17,-5,0,-16,2,0,-20,-16,-2,-18],
	["marts",2,-9,-1,-3,-6,-2,1,-2,-3,-9,-1,-4,0,-6,-7,1,0,2,-5,-10,2,-7,-3,2,-10,2,-9,-8,-5,-2],
	["aprill",-5,0,10,-9,0,-9,-8,6,-5,3,-1,4,9,-1,2,0,10,0,5,0,-10,0,6,3,-6,-2,-10,-8,-2],
	["mai",12,5,8,-1,-2,4,10,-1,7,15,7,3,6,4,10,9,13,6,14,10,14,2,6,12,15,2,14,11,9,1],
	["juuni",12,5,17,6,10,14,9,7,15,23,29,11,16,18,9,25,14,8,16,22,19,22,23,18,16,16,26,24,22],
	["juuli",15,8,21,28,18,13,9,9,8,6,8,12,12,29,28,20,6,9,12,8,14,18,14,13,23,6,24,24,17,20],
	["august",7,6,5,19,18,18,17,20,15,11,7,10,13,12,20,11,10,14,18,14,24,6,17,16,6,17,5,13,11],
	["september",21,19,21,9,13,18,6,6,20,7,25,13,8,9,14,16,19,10,7,25,7,17,16,15,17,18,15,9,19],
	["oktoober",2,2,1,5,-2,5,5,2,2,2,1,-2,1,-2,0,-2,5,4,0,1,-1,2,0,2,2,2,-1,1,4,-1],
	["november",-6,-7,-2,-7,-2,-4,0,-7,-8,-6,0,-9,-2,-3,-2,0,-8,-2,-5,-2,-5,-8,-10,0,-2,-9,-9,-7,-1],
	["detsember",-15,2,-11,-14,-15,-5,-5,-18,-18,-19,0,0,2,-7,-16,-7,-4,-1,-1,-16,-18,-10,-3,-19,-6,-16,-16,-8,-2,-18]]

for i in kuud:
    kuu = i.pop(0)
    print(f"{i.index(max(i))+1}. {kuu} sooja oli {max(i)} kraadi.")






