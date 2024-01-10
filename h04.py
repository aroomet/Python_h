# Roomet Altmäe
# 14.11.2023
# Ülesanne 04
"""
Tärnid
    Loo tsükkel, mis väljastab 5×5 tärnid
    Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
    Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""
j = 5
for i in range(5):
    print("* "*j)
    j = j - 1
    j -= 1
     
print()
"""
Jalgpalli meeskond
    Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
    Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
    Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""
sugu = "mees"
if sugu == 'mees':
    vanus = 17
    if vanus >= 16 and vanus <=18:
        print("tere tulemast meeskonda!")
    else:
        print("Vanus ei sobi")
else:
    print("Ei pääse meeskonda")

"""
Müük
    Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
    Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""
hind = int(input( "sisesta hind:  "))
al1 = 0.1
al2 = 0.2
if hind <= 10:
    al = hind+hind*al1
else:
    al = hind-hind*al2
print(f"soodus hind on {al}€")
"""
Juubel
    Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
    Plokkskeemi pole vaja!
"""
v = 26
if v % 5 == 0:
    vanus = "on"
else:
    vanus = "ei ole"
print(f"vanus: {v} {vanus} juubel")
"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm
    küsib kasutajalt, mis tehet ta soovib (+-*/)
    ning viib kasutaja valiku ellu.
    Koosta vastab plokkskeem ja salvesta
    see samasse kataloogi programmiga.
"""
nr1 = int(input("arv 1: "))
nr2 = int(input("arv 2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "ära pulli mees!"
    
print(f"{nr1} {tehe} {nr2} = {vastus}")
    
"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm
    tuvastab kas tegemist saab olla ruuduga.
    Koosta vastab plokkskeem ja salvesta
    see samasse kataloogi programmiga.
"""
nr1 = int(input("Ruudu 1. külg: "))
nr2 = int(input("Ruudu 2. külg: "))

if nr1 == nr2:
    print("eepiline ruut")
else:
    print("mitte väga eepiline ruut")