#arquivo apagável e ignorável, criado para testar a função fala sem ter que ver a cena inteira das animações

from pacote.nucleo import fala

import turtle

screen = turtle.Screen()
turtle.penup()
turtle.goto(100, 100)
fala(turtle, "sei lá", 100, 100, 5, "white")

turtle.done()