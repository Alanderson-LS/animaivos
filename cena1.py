from pacote.nucleo import carrega_img_fundo, carrega_personagens, fala, habilita_clique

import turtle
import time

balao = turtle.Turtle()
balao.hideturtle()

turtle.addshape("pacote/personagens/alanderson_redimensionado.gif")
turtle.addshape("pacote/personagens/nascimento_redimensionado.gif")
turtle.addshape("pacote/personagens/douglas_redimensionado.gif")

def rua_personagens():
    global nascimento, alanderson, douglas, screen
    turtle.tracer(0)

    screen = turtle.Screen()

    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/rua_redimensionada.gif")
    

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

def andar(personagem: turtle.Turtle, horizontal: int, vertical: int):
    personagem.goto(personagem.xcor() + horizontal, personagem.ycor() + vertical)

def movimento():
    for i in range(33):
        andar(nascimento, 0, -10)
        screen.update()
        time.sleep(0.1)
        andar(douglas, 0, -10)
        screen.update()
        time.sleep(0.1)

def movimento_2():
    for i in range(20):
        andar(alanderson, 10, 0)
        screen.update()
    


def cena1():
    rua_personagens()
    movimento()
    screen.tracer(1)
    fala(nascimento, "Cadê esse boy?", 225, 150, 5)
    fala(douglas, "Esse amostradinho vai gaziar é?", 225, 150, 5)
    movimento_2()
    fala(alanderson, "Perdi a hora galado, esqueci até da canelite de tanto correr", 45, 150, 5)
cena1()
turtle.done()

