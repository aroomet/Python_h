# Iseseisevtöö 3 
# R.altmäe
# 10.01.23
import datetime
paev = datetime.datetime.now().day
# tahvli juurde
fail=open("nimekiri.txt", encoding="UTF-8")
nr = 1 
for nimi in fail:
    if nr == paev:
            print(nimi,end="")
    nr+=1

input()
#jukebox
siiamidagi = input("Anna failinimi: ")
fail = open(siiamidagi, encoding="utf-8")
print("Muusikapalade valik: ")
nr = 1
for i in fail:
    print(f"{nr}.{i}",end="")
    nr+=1
valik = int(input("\n Vali laulu nr: "))
fail.seek(0) # keri faili algusesse
nr = 1
for i in fail:
    if nr == valik:
        print(i)
    nr+=1


input()
# Sissetulekud

import random
fail = open("konto.txt")
for i in fail:
    if float(i) > 0:
        print(i,end="")

# Rebased

# fail = open("rebased.txt"encode="UTF-8")