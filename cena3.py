from pacote.nucleo import fala

import turtle
import time

def corredor_personagens():
    global alanderson, nascimento, douglas, screen, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape
    balao = turtle.Turtle()
    balao.hideturtle()
    turtle.addshape("pacote/personagens/nascimento_falando.gif")
    turtle.addshape("pacote/personagens/alanderson_redimensionado.gif")
    turtle.addshape("pacote/personagens/nascimento_redimensionado.gif")
    turtle.addshape("pacote/personagens/douglas_redimensionado.gif")
    turtle.addshape("pacote/personagens/alanderson_falando.gif")
    turtle.addshape("pacote/personagens/douglas_falando.gif")
    alanderson_shape = ("pacote/personagens/alanderson_redimensionado.gif")
    nascimento_shape = ("pacote/personagens/nascimento_redimensionado.gif")
    douglas_shape = ("pacote/personagens/douglas_redimensionado.gif")
    alanderson_falando = ("pacote/personagens/alanderson_falando.gif")
    nascimento_falando = ("pacote/personagens/nascimento_falando.gif")
    douglas_falando = ("pacote/personagens/douglas_falando.gif")
    turtle.tracer(0)

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/corredor_redimensionado.gif")

    alanderson = turtle.Turtle()
    alanderson.shape(alanderson_shape)
    alanderson.penup()

    nascimento = turtle.Turtle()
    nascimento.shape(nascimento_shape)
    nascimento.penup()

    douglas = turtle.Turtle()
    douglas.shape(douglas_shape)
    douglas.penup()

    irapuan = turtle.Turtle()
    irapuan.penup()

    jurandy = turtle.Turtle()
    jurandy.penup()

    alanderson.goto(-450, 0)
    douglas.goto(-450, 0)
    nascimento.goto(-450, 0)

    irapuan.goto(-60, -250)
    jurandy.goto(60, -250)
    jurandy.right(180)

    screen.update()
    turtle.done()


def movimento1():
    pass

def cena3():
    corredor_personagens()
    fala()


cena3()