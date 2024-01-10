# Roomet Altmae 14.11.2023
# Ülesanne 4 turtle

import turtle
w = turtle.Screen()
w.setup(300,300)

w.title("R.Altmae Ülesanne 04")
def ruut (edasi, nurk):
    for i in range (5):
        turtle.forward(edasi/2)
        turtle.left(nurk)
        for i in range (3):
            turtle.forward(edasi)
            turtle.left(nurk)
        turtle.forward(edasi/2)
        turtle.left(360/5)

        
ruut(100,90)
#akna loomine

