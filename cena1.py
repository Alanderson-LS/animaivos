from pacote.nucleo import fala, andar

import turtle
import time


def rua_personagens(screen = turtle.Screen()):
    global nascimento, alanderson, douglas, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape
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
    


def movimento(screen = turtle.Screen()):
    for i in range(33):
        andar(nascimento, 0, -10)
        screen.update()
        time.sleep(0.1)
        andar(douglas, 0, -10)
        screen.update()
        time.sleep(0.1)
        """
        novas posições: 
        Nascimento(275, 120)
        Douglas(275, 240)
        """

def movimento_2(screen = turtle.Screen()):
    for i in range(20):
        andar(alanderson, 10, 0)
        screen.update()
        """
        nova posição
        Alanderson: (-250, -130)
        """

def movimento_3(screen = turtle.Screen()):
    for i in range(25):
        andar(alanderson, 10, 10)
        time.sleep(0.05)
        screen.update()
        """
        nova posição
        Alanderson: (0, 120)
        """

    for i in range(6):
        andar(nascimento, 0, -10)
        screen.update()
        andar(douglas, 0, -10)
        screen.update()
        andar(alanderson, 10, 0)
        screen.update()
        time.sleep(0.05)
        """
        novas posições:
        Alanderson: (60, 120)
        Nascimento: (275, 60)
        Douglas: (275, 180)
        """

    for i in range(12):
        andar(nascimento, 10, 0)
        screen.update()
        andar(douglas, 0, - 10)
        screen.update()
        andar(alanderson, 5, -5)
        time.sleep(0.05)
        screen.update()
        """
        novas posições:
        Alanderson: (120, 60)
        Nascimento: (395, 60)
        Douglas: (275, 60)
        """
    
    for i in range(33):
        andar(nascimento, 10, 0)
        andar(douglas, 10, 0)
        andar(alanderson, 10, 0)
        time.sleep(0.05)
        screen.update()

def limpar_personagens():
    for t in turtle.turtles():
        t.hideturtle()
        t.clear()

def cena1(screen = turtle.Screen()):
    global nascimento, alanderson, douglas, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape
    rua_personagens(screen)
    movimento(screen)
    screen.tracer(1)
    fala(nascimento, "Cadê esse boy?", 225, 150, 5, nascimento_falando, nascimento_shape)
    fala(douglas, "Esse amostradinho vai gaziar é?", 225, 150, 5, douglas_falando, douglas_shape)
    movimento_2()
    fala(alanderson, "Perdi a hora galado, esqueci até da canelite de tanto correr", 45, 150, 5, alanderson_falando, alanderson_shape)
    fala(nascimento, "Corre lek, vamo atrasar", 225, 150, 5, nascimento_falando, nascimento_shape)
    screen.tracer(0)
    movimento_3()
    alanderson.hideturtle()
    douglas.hideturtle()
    nascimento.hideturtle()
    nascimento.clear()
    alanderson.clear()
    douglas.clear()

    nascimento.reset()
    alanderson.reset()
    douglas.reset()
    
    nascimento = None
    alanderson = None
    douglas = None
    balao = None
    alanderson_falando = None
    alanderson_shape = None
    douglas_falando = None
    douglas_shape = None
    nascimento_falando = None
    nascimento_shape = None

    limpar_personagens()

if __name__ == "__main__":
    cena1()