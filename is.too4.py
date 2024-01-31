# Iseseisev töö
#R.Altmäe
#10.01.23

kassa = 0
def pronksikarva_summa(fail):
    fail = open("myndid.txt")
    for mynt in fail:
        if int(mynt)<10:
            print(mynt, end="")
            kassa += int(mynt)
        print("\Kassas: ", kassa)



pronksikarva_summa("myndid.txt")











#---------------------
kylalised = 3

def tervitus(n):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {n}. kord tervitada!")
    print('Külaline: "Tere, suur tänu kutsumast!"')

for i in range(kylalised):
    tervitus(i+1)

#---------------------
def eelarve(kylalised):
    summa = kylalised * 10 + 55
    return summa
palju = int(input("Mitu kutsutud: "))
palju2 = int(input("Mitu tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(palju)}€")
print(f"Minimaalne eelarve: {eelarve(palju2)}€")




#---------------------
def mahlapakkide_arv(kg):
    pakid = round(kg * 0.4 / 3)
    return pakid
kogus = int(input("Õunte kogus: "))
print(mahlapakkide_arv(kogus))


#---------------------
def banner(t):
    print(t.upper())

ask = int(input("Mitu korda: "))
ask2 = input("Reklaamlause: ")

for i in range(ask):
    banner(ask2)
