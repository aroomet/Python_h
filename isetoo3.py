import random
#Roomet Altmäe
#06.05.24
#Kodutöö








#15. Ülesanne
"""
Temperatuurid - Programm peab tĆ¶Ć¶tlema Ć¼he aasta kĆµigi pĆ¤evade temperatuure. Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupĆ¤eval oli kĆµige soojem. VĆ¤ljasta kuupĆ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pĆ¤eva, vĆ¤ljasta vĆ¤hemalt Ć¼ks)

	jaanuar -16 -12 -15 -20 0 -1 -20 -2 -20 -14 -18 -8 2 -1 -14 -7 -15 -17 -6 -17 -17 -7 0 3 -20 -17 -15 -8 -12 3
	veebruar -9 -2 -7 1 -16 -19 -19 -11 -16 -15 -9 -2 -16 -4 -20 -5 -6 -17 -5 0 -16 2 0 -20 -16 -2 -18
	mĆ¤rts 2 -9 -1 -3 -6 -2 1 -2 -3 -9 -1 -4 0 -6 -7 1 0 2 -5 -10 2 -7 -3 2 -10 2 -9 -8 -5 -2
	aprill -5 0 10 -9 0 -9 -8 6 -5 3 -1 4 9 -1 2 0 10 0 5 0 -10 0 6 3 -6 -2 -10 -8 -2
	mai 12 5 8 -1 -2 4 10 -1 7 15 7 3 6 4 10 9 13 6 14 10 14 2 6 12 15 2 14 11 9 1
	juuni 12 5 17 6 10 14 9 7 15 23 29 11 16 18 9 25 14 8 16 22 19 22 23 18 16 16 26 24 22
	juuli 15 8 21 28 18 13 9 9 8 6 8 12 12 29 28 20 6 9 12 8 14 18 14 13 23 6 24 24 17 20
	august 7 6 5 19 18 18 17 20 15 11 7 10 13 12 20 11 10 14 18 14 24 6 17 16 6 17 5 13 11
	september 21 19 21 9 13 18 6 6 20 7 25 13 8 9 14 16 19 10 7 25 7 17 16 15 17 18 15 9 19
	oktoober 2 2 1 5 -2 5 5 2 2 2 1 -2 1 -2 0 -2 5 4 0 1 -1 2 0 2 2 2 -1 1 4 -1
	november -6 -7 -2 -7 -2 -4 0 -7 -8 -6 0 -9 -2 -3 -2 0 -8 -2 -5 -2 -5 -8 -10 0 -2 -9 -9 -7 -1
	detsember -15 2 -11 -14 -15 -5 -5 -18 -18 -19 0 0 2 -7 -16 -7 -4 -1 -1 -16 -18 -10 -3 -19 -6 -16 -16 -8 -2 -18
"""
def Temperatuurid():
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    temp=[[-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3],
          [-9,-2,-7,1,-16,-19,-19,-11,-16,-15,-9,-2,-16,-4,-20,-5,-6,-17,-5,0,-16,2,0,-20,-16,-2,-18],
          [2,-9,-1,-3,-6,-2,1,-2,-3,-9,-1,-4,0,-6,-7,1,0,2,-5,-10,2,-7,-3,2,-10,2,-9,-8,-5,-2],
          [-5,0,10,-9,0,-9,-8,6,-5,3,-1,4,9,-1,2,0,10,0,5,0,-10,0,6,3,-6,-2,-10,-8,-2],
          [12,5,8,-1,-2,4,10,-1,7,15,7,3,6,4,10,9,13,6,14,10,14,2,6,12,15,2,14,11,9,1],
          [12,5,17,6,10,14,9,7,15,23,29,11,16,18,9,25,14,8,16,22,19,22,23,18,16,16,26,24,22],
          [15,8,21,28,18,13,9,9,8,6,8,12,12,29,28,20,6,9,12,8,14,18,14,13,23,6,24,24,17,20],
          [7,6,5,19,18,18,17,20,15,11,7,10,13,12,20,11,10,14,18,14,24,6,17,16,6,17,5,13,11],
          [21,19,21,9,13,18,6,6,20,7,25,13,8,9,14,16,19,10,7,25,7,17,16,15,17,18,15,9,19],
          [2,2,1,5,-2,5,5,2,2,2,1,-2,1,-2,0,-2,5,4,0,1,-1,2,0,2,2,2,-1,1,4,-1],
          [-6,-7,-2,-7,-2,-4,0,-7,-8,-6,0,-9,-2,-3,-2,0,-8,-2,-5,-2,-5,-8,-10,0,-2,-9,-9,-7,-1],
          [-15,2,-11,-14,-15,-5,-5,-18,-18,-19,0,0,2,-7,-16,-7,-4,-1,-1,-16,-18,-10,-3,-19,-6,-16,-16,-8,-2,-18]]

    max_temp = float('-inf')
    max_temp_kuup = ""
    
    for i in range(len(kuud)):
        for j in range(len(temp[i])):
            if temp[i][j] > max_temp:
                max_temp = temp[i][j]
                max_temp_kuup = f"{j+1} {kuud[i]}"
    
    print(f"kuumim kuupäev on: {max_temp_kuup} ja temperatuur sellel päeval oli {max_temp} kraadi")
Temperatuurid()


input()

  



"""
Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
	kuvatakse korrektne arusaadav kĆ¼simus ja  vastus - 1p
	eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 2p
	kood mis teavitab paaris vĆµi paaritust arvust - 2p
	kuvatakse programmi pealkiri - 1p
"""
input()
#13. Ülesanne
print("------PAARIS VÕI PAARITU ARV------")
try:
    arv = input("Sisesta arv: ")
    if int(arv)== 0:
        print("Arv on null")

    elif int(arv) % 2  == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
except ValueError:
    print("Vigane sisend") 
"""
Salakeel
	sinu programm kĆ¼sib kasutajalt, kas ta soovib salakeelt luua vĆµi tĆµlkida - 1p
	kasutaja sisestab tavalise sĆµna, mis muudetakse salakeeleks - 1p
	kasutaja sisestab salakeeles sĆµna, mis teisendatakse jĆ¤lle normaalseks - 1p
	kood kommenteeritud - 1p
"""
input()

#11. Ülesanne

def loo_salakeel():
    valik = input("Kas soovid luua salakeelt (sisesta 1) või tõlkida salakeelt (sisesta 2): ")
    if valik == "1":
        salakeel = input("Sisesta sõna, mida soovid salakeelde tõlkida: ")
        salakeel = salakeel.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
        print(salakeel)
        
    elif valik == "2":
        salakeel = input("Sisesta salakeelde tõlgitud sõna: ")
        salakeel = salakeel.replace("1", "a").replace("2", "e").replace("3", "i").replace("4", "o").replace("5", "u")
        print(salakeel)
       
    else:
         print("Vigane valik. Palun sisesta 1 või 2.")


loo_salakeel()

# see on ainult põhimõtte ma ei hakka pikka replace rida kirjutama kuid tehniliselt saab kõik tähed ära muuta
"""

9. Emaili kontroll
	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
	programm kontrollib kas email on sisestatud Ćµigesti - vĆ¤hemalt @-mĆ¤rgi kontroll - 1p
	programm tĆ¼keldab selle ja vĆ¤ljastab lause: ā€Tere enimi, sinu email on server serveris ja domeeniks on sul comā€™ - 1p
	kasutajalt kĆ¼situd kĆ¼simused on selgelt Ć¼heselt mĆµistetavad - 1p
	kood kommenteeritud - 1p
	

"""
input()
#9. Ülesanne

def emaili_kontroll(email):
    email = input("Sisesta email: ")
    if "@" in email:
        nimi = email.split('.')[0]
        domeen = email.split('@')[1]
        print(f"Tere {nimi}, sinu email on {email} ja domeeniks on {domeen}.")
    else:
        print("Sisestatud email on vale")

print(emaili_kontroll("email"))

"""
Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
	kĆ¼sitakse valuuta kogust ja tehakse arvutused - 2p
	kood kommenteeritud - 1p
"""

input()
#7. Ülesanne
def eurokalkulaator():
    while True:  
        print("1. EUR->EEK")
        print("2. EEK->EUR")
        print("3. EXIT")
        valik=int(input("vali: "))
        if valik==1:
            summa=int(input("summa: "))
            print(f"{summa} eurot on {summa*15.6466} krooni")
        elif valik==2:
            summa=int(input("summa: "))
            print(f"{summa} krooni on {summa/15.6466} eurot")
        elif valik==3:
            break
        else:
            print("vale valik loll lammas")
eurokalkulaator()


input()
#5. Ülesanne

ostunimekiri = []

def ostunimekirja(ostunimekiri):
    while True:
        toode = input("Sisesta toode: ")
        if toode == "":
            print(ostunimekiri)
            break
        else:
            ostunimekiri.append(toode)
        

ostunimekirja(ostunimekiri)

"""
3. Positiivsed ja negatiivsed
	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
	nulli lisamisel ei tehta midagi 1p
	vĆ¤ljasta mĆµlemad loendit 1p
"""
input()

#3. Ülesanne

loend1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loend2 =  [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


def hoidmine(loend1, loend2):
    for i in range (5) :
        number = int(input("Sisesta number: "))
        if number > 0:
            loend1.append(f"{number},")
        elif number < 0:
            loend2.append(f"{number},")
    for i in loend1:
        print(i)
    for i in loend2:
        print(i)

hoidmine(loend1, loend2)

"""
1. Korrutamise kontrollimine
	programm esitab korrutustehte 1p
	ootab kasutajalt vastuse sisestamist 1p
	kontrollib vastuse Ćµigsust 1p
	vĆ¤ljastab, kas vastus oli Ćµige vĆµi vĆ¤Ć¤r. 1p
	kokku antakse lahendamiseks 10 Ć¼lesannet. 1p

"""
input()

#1. Ülesanne

arv1 = random.randint(1, 10)
arv2 = random.randint(1, 10)


def korrutamine(arv1, arv2):
    print(f"{arv1} * {arv2} = ")
    for i in range(10):
        vastus = int(input("Sisesta vastus: "))
        if vastus == arv1 * arv2:
            print("Õige vastus!")
        else:
            print("Vale vastus!")

korrutamine(arv1, arv2)
