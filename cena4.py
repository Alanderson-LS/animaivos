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

    turtle.addshape("pacote/personagens/prova_ataque.gif")
    turtle.addshape("pacote/personagens/prova_dano.gif")
    turtle.addshape("pacote/personagens/prova_normal.gif")
    turtle.addshape("pacote/personagens/prova_rindo_1.gif")
    turtle.addshape("pacote/personagens/prova_rindo_2.gif")

    prova_dano = "pacote/personagens/prova_dano.gif"
    prova_ataque = "pacote/personagens/prova_ataque.gif"
    prova_normal = "pacote/personagens/prova_normal.gif"
    prova_rindo_1 = "pacote/personagens/prova_rindo_1.gif"
    prova_rindo_2 = "pacote/personagens/prova_rindo_2.gif"


    alanderson_costa = "pacote/personagens/alanderson_costa.gif"
    douglas_costa = "pacote/personagens/douglas_costa.gif"
    nascimento_costa = "pacote/personagens/nascimento_costa.gif"

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/sala.gif")
    screen.tracer(0)

    alanderson = turtle.Turtle()
    alanderson.shape(alanderson_costa)
    alanderson.penup()

    douglas = turtle.Turtle()
    douglas.shape(douglas_costa)
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

    screen.update()

def cena4():
    habilita_clique()
    sala_personagens()
    turtle.done()

if __name__ == "__main__":
    cena4()