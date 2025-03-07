from pacote.nucleo import fala, fala_2, andar, habilita_clique

import turtle
import time

def sala_personagens():
    global alanderson
    global nascimento
    global douglas
    global prova
    global screen, balao

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/sala.gif")

    alanderson = turtle.Turtle()
    alanderson.penup()

    douglas = turtle.Turtle()
    douglas.penup()

    nascimento = turtle.Turtle()
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

cena4()