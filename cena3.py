from pacote.nucleo import fala, fala_2, andar, exibir_coordenadas, habilita_clique

import turtle
import time

def corredor_personagens():
    global alanderson, nascimento, douglas, screen, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape, irapuan, jurandy, alanderson_mov, nascimento_mov, douglas_mov
    balao = turtle.Turtle()
    balao.hideturtle()
    turtle.addshape("pacote/personagens/nascimento_falando_grande.gif")
    turtle.addshape("pacote/personagens/alanderson_grande.gif")
    turtle.addshape("pacote/personagens/nascimento_grande.gif")
    turtle.addshape("pacote/personagens/douglas_grande.gif")
    turtle.addshape("pacote/personagens/alanderson_falando_grande.gif")
    turtle.addshape("pacote/personagens/douglas_falando_grande.gif")
    alanderson_shape = ("pacote/personagens/alanderson_grande.gif")
    nascimento_shape = ("pacote/personagens/nascimento_grande.gif")
    douglas_shape = ("pacote/personagens/douglas_grande.gif")
    alanderson_falando = ("pacote/personagens/alanderson_falando_grande.gif")
    nascimento_falando = ("pacote/personagens/nascimento_falando_grande.gif")
    douglas_falando = ("pacote/personagens/douglas_falando_grande.gif")
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

    alanderson.goto(-750, -250)
    douglas.goto(-600, -250)
    nascimento.goto(-450, -250)

    irapuan.goto(-60, -250)
    jurandy.goto(60, -250)
    jurandy.right(180)

    alanderson_mov = 0
    douglas_mov = 0
    nascimento_mov = 0

    screen.update()



def trocar_shape(personagem: turtle.Turtle(), shape_1: str, shape_2: str, shape_3: str, shape_4: str, shape_5: str, shape_6, shape_7, shape_8):
    global alanderson_mov, douglas_mov, nascimento_mov
    
    if personagem == alanderson:
        if alanderson_mov == 0:
            alanderson.shape(shape_1)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 1:
            alanderson.shape(shape_2)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 2:
            alanderson_shape(shape_3)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 3:
            alanderson.shape(shape_4)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 4:
            alanderson_shape(shape_5)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 5:
            alanderson.shape(shape_6)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 6:
            alanderson_shape(shape_7)
            alanderson_mov = 7 - alanderson_mov
        elif alanderson_mov == 7:
            alanderson.shape(shape_8)
            alanderson_mov = 7 - alanderson_mov
    
    elif personagem == nascimento:
        if nascimento_mov == 0:
            nascimento.shape(shape_1)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 1:
            nascimento.shape(shape_2)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 2:
            nascimento_shape(shape_3)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 3:
            nascimento.shape(shape_4)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 4:
            nascimento_shape(shape_5)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 5:
            nascimento.shape(shape_6)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 6:
            nascimento_shape(shape_7)
            nascimento_mov = 7 - nascimento_mov
        elif nascimento_mov == 7:
            nascimento.shape(shape_8)
            nascimento_mov = 7 - nascimento_mov
    
    elif personagem == douglas:
        if douglas_mov == 0:
            douglas.shape(shape_1)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 1:
            douglas.shape(shape_2)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 2:
            douglas_shape(shape_3)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 3:
            douglas.shape(shape_4)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 4:
            douglas_shape(shape_5)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 5:
            douglas.shape(shape_6)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 6:
            douglas_shape(shape_7)
            douglas_mov = 7 - douglas_mov
        elif douglas_mov == 7:
            douglas.shape(shape_8)
            douglas_mov = 7 - douglas_mov




def movimento1():
    
    while nascimento.xcor() != -210:
        
        andar(nascimento, 10, 0)
        time.sleep(0.1)
        trocar_shape(nascimento, nascimento_shape, nascimento_falando)
        screen.update()

        andar(douglas, 10, 0)
        time.sleep(0.1)
        trocar_shape(douglas, douglas_shape, douglas_falando)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()
    
    while douglas.xcor()!= -210:
        
        andar(nascimento, 10, 10)
        time.sleep(0.1)
        trocar_shape(nascimento, nascimento_shape, nascimento_falando)
        screen.update()

        andar(douglas, 10, 0)
        time.sleep(0.1)
        trocar_shape(douglas, douglas_shape, douglas_falando)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()

    while alanderson.xcor() != -210:

        andar(nascimento, 10, 10 if nascimento.ycor() < 13 else 0)
        time.sleep(0.1)
        trocar_shape(nascimento, nascimento_shape, nascimento_falando)
        screen.update()

        andar(douglas, 10, 10)
        time.sleep(0.1)
        trocar_shape(douglas, douglas_shape, douglas_falando)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()

    while nascimento.xcor() < 250:

        andar(nascimento, 10, 0)
        time.sleep(0.1)
        trocar_shape(nascimento, nascimento_shape, nascimento_falando)
        screen.update()

        andar(douglas, 10,  10 if douglas.ycor() < 13 else 0)
        time.sleep(0.1)
        trocar_shape(douglas, douglas_shape, douglas_falando)
        screen.update()

        andar(alanderson, 10, 10)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()

    nascimento.hideturtle()
    screen.update()
    
    while douglas.xcor() < 250:
        andar(douglas, 10,  0)
        time.sleep(0.1)
        trocar_shape(douglas, douglas_shape, douglas_falando)
        screen.update()

        andar(alanderson, 10, 10 if alanderson.ycor() < 13 else 0)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()

    douglas.hideturtle()
    screen.update()

    while alanderson.xcor() < 250:
        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, alanderson_shape, alanderson_falando)
        screen.update()

    alanderson.hideturtle()
    screen.update()


    pass

def cena3():
    corredor_personagens()
    habilita_clique()
    screen.tracer(1)
    #fala_2(irapuan, "Ei, esses galadinho de InfoV só fez bagunça no ônibus", 45, 50, 5)
    #fala_2(jurandy, "Oxi, quero ir denovo pra um passeio com essa galera, os caba é resenha demais", 135, 50, 5)
    #fala_2(irapuan, "Ixi, eu é que não vou denovo, tu que se lasque kkkk", 45, 50, 5)
    #fala_2(jurandy, "Oloco Pupu, tá desumilde hein", 135, 50, 5)
    #fala_2(irapuan, "Ai dento", 45, 50, 5)
    screen.tracer(0)
    movimento1()

    turtle.done()


cena3()