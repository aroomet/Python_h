# Ylesanne 5
# Roomet Altmae 14.11.2023


import turtle
w = turtle.Screen()
w.setup(300,300)

w.title("Roomet Altmae ylesanne 5")
def kolmnurk(edasi,nurk):
    for i in range(6):
        turtle.left(360/6)
        for i in range(3):
            turtle.forward(edasi)
            turtle.left(nurk)
    

kolmnurk(100,120)