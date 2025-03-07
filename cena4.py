from pacote.nucleo import fala, fala_2, andar, habilita_clique

import turtle
import time

def sala_personagens():
    global alanderson
    global nascimento
    global douglas
    global prova
    global screen, balao
    
    turtle.addshape("pacote/personagens/alanderson_costa.gif")
    turtle.addshape("pacote/personagens/douglas_costa.gif")
    turtle.addshape("pacote/personagens/nascimento_costa.gif")

    alanderson_costa = "pacote/personagens/alanderson_costa.gif"
    douglas_costa = "pacote/personagens/douglas_costa.gif"
    nascimento_costa = "pacote/personagens/nascimento_costa.gif"

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/sala.gif")

    alanderson = turtle.Turtle()
    alanderson.shape(alanderson_costa)
    alanderson.penup()

    douglas = turtle.Turtle()
    
    douglas.penup()

    nascimento = turtle.Turtle()
    nascimento.shape(nascimento_costa)
    nascimento.penup()

    prova = turtle.Turtle()
    prova.penup()

    balao = turtle.Turtle()
    balao.hideturtle()

    nascimento.goto(-250, -300)
    douglas.goto(-20, -300)
    alanderson.goto(220, -300)



def cena4():
    habilita_clique()
    sala_personagens()
    turtle.done()

if __name__ == "__main__":
    cena4()