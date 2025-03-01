from pacote.nucleo import carrega_img_fundo, carrega_personagens, fala, habilita_clique

import turtle
import time

turtle.addshape("pacote/personagens/alanderson_redimensionado.gif")
turtle.addshape("pacote/personagens/nascimento_redimensionado.gif")
turtle.addshape("pacote/personagens/douglas_redimensionado.gif")

def rua_personagens():
    global nascimento, alanderson, douglas, screen
    turtle.tracer(0)

    screen = turtle.Screen()
    screen.bgpic("pacote/fundos/rua_redimensionada.gif")
    screen.setup(800, 800)

    alanderson = turtle.Turtle()
    alanderson.shape("pacote/personagens/alanderson_redimensionado.gif")
    alanderson.penup()

    douglas = turtle.Turtle()
    douglas.shape("pacote/personagens/douglas_redimensionado.gif")
    douglas.penup()

    nascimento = turtle.Turtle()
    nascimento.shape("pacote/personagens/nascimento_redimensionado.gif")
    nascimento.speed(0)
    nascimento.penup()

    alanderson.goto(-450, -130)
    nascimento.goto(275, 450)
    douglas.goto(275, 570)
    screen.update()

def andar(personagem: turtle.Turtle(), horizontal: int, vertical: int):
    personagem.goto(personagem.xcor() + horizontal, personagem.ycor() + vertical)

def movimento():
    for i in range(33):
        andar(nascimento, 0, -10)
        screen.update()
        time.sleep(0.1)
        andar(douglas, 0, -10)
        screen.update()
        time.sleep(0.25)
    


def cena1():
    rua_personagens()
    movimento()
    fala(nascimento, "Cadê esse boy?", 225, 50, 5)

cena1()
turtle.done()

