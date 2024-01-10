#Massiivid - Array
# R.Altmae
# 28.11.23

"""
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
"""
vanused = [13,12,5,4,5,4,45,5,5,54,44,4,4,4]
print(f"Suurim arv on: {max(vanused)} ja väikseim arv on {min(vanused)}")
print(f"Vanuste summa: {sum(vanused)}")
print(f"Vanuste keskmine: {round(sum(vanused)/len(vanused),2)}")

for vanus in vanused:
    print(vanus * "*")

print(vanused[0]*"")

print("")
"""
Duplikaadid

    Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.


"""
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
uus_opilased= []
#käib kõik läbi
for opilane in opilased:
        if opilane not in uus_opilased:
        uus_opilased.append(opilased)
print(uus_opilased)
print("")
input()

"""
"""