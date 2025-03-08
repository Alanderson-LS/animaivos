#arquivo apagável e ignorável, criado para testar a função fala sem ter que ver a cena inteira das animações

from pacote.nucleo import fala
import time

import turtle

screen = turtle.Screen()
turtle.penup()
turtle.goto(100, 100)

t1 = turtle.Turtle()
time.sleep(1)
print (t1)
del t1
time.sleep(1)
print (t1)
turtle.done()