from pacote.nucleo import fala_2, andar, habilita_clique

import turtle
import time

def caminho_personagens():
    global alanderson, nascimento, douglas, screen, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape, irapuan, jurandy, alanderson_mov, nascimento_mov, douglas_mov
    global n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8
    global d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8
    global a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8

    balao = turtle.Turtle()
    balao.hideturtle()
    turtle.addshape("pacote/personagens/nascimento_falando_grande.gif")
    turtle.addshape("pacote/personagens/alanderson_grande.gif")
    turtle.addshape("pacote/personagens/nascimento_grande.gif")
    turtle.addshape("pacote/personagens/douglas_grande.gif")
    turtle.addshape("pacote/personagens/alanderson_falando_grande.gif")
    turtle.addshape("pacote/personagens/douglas_falando_grande.gif")
    
    turtle.addshape("pacote/personagens/_nascimento_andando_1.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_2.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_3.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_4.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_5.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_6.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_7.gif")
    turtle.addshape("pacote/personagens/_nascimento_andando_8.gif")

    turtle.addshape("pacote/personagens/_douglas_andando_1.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_2.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_3.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_4.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_5.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_6.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_7.gif")
    turtle.addshape("pacote/personagens/_douglas_andando_8.gif")

    turtle.addshape("pacote/personagens/_alanderson_andando_1.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_2.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_3.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_4.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_5.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_6.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_7.gif")
    turtle.addshape("pacote/personagens/_alanderson_andando_8.gif")

    n_mov_1 = ("pacote/personagens/_nascimento_andando_1.gif")
    n_mov_2 =("pacote/personagens/_nascimento_andando_2.gif")
    n_mov_3 =("pacote/personagens/_nascimento_andando_3.gif")
    n_mov_4 =("pacote/personagens/_nascimento_andando_4.gif")
    n_mov_5 =("pacote/personagens/_nascimento_andando_5.gif")
    n_mov_6 =("pacote/personagens/_nascimento_andando_6.gif")
    n_mov_7 =("pacote/personagens/_nascimento_andando_7.gif")
    n_mov_8 =("pacote/personagens/_nascimento_andando_8.gif")

    d_mov_1 =("pacote/personagens/_douglas_andando_1.gif")
    d_mov_2 =("pacote/personagens/_douglas_andando_2.gif")
    d_mov_3 =("pacote/personagens/_douglas_andando_3.gif")
    d_mov_4 =("pacote/personagens/_douglas_andando_4.gif")
    d_mov_5 =("pacote/personagens/_douglas_andando_5.gif")
    d_mov_6 =("pacote/personagens/_douglas_andando_6.gif")
    d_mov_7 =("pacote/personagens/_douglas_andando_7.gif")
    d_mov_8 =("pacote/personagens/_douglas_andando_8.gif")

    a_mov_1 =("pacote/personagens/_alanderson_andando_1.gif")
    a_mov_2 =("pacote/personagens/_alanderson_andando_2.gif")
    a_mov_3 =("pacote/personagens/_alanderson_andando_3.gif")
    a_mov_4 =("pacote/personagens/_alanderson_andando_4.gif")
    a_mov_5 =("pacote/personagens/_alanderson_andando_5.gif")
    a_mov_6 =("pacote/personagens/_alanderson_andando_6.gif")
    a_mov_7 =("pacote/personagens/_alanderson_andando_7.gif")
    a_mov_8 =("pacote/personagens/_alanderson_andando_8.gif")

    alanderson_shape = ("pacote/personagens/alanderson_grande.gif")
    nascimento_shape = ("pacote/personagens/nascimento_grande.gif")
    douglas_shape = ("pacote/personagens/douglas_grande.gif")
    alanderson_falando = ("pacote/personagens/alanderson_falando_grande.gif")
    nascimento_falando = ("pacote/personagens/nascimento_falando_grande.gif")
    douglas_falando = ("pacote/personagens/douglas_falando_grande.gif")
        


    turtle.tracer(0)

    

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgpic("pacote/fundos/foraif.gif")

    alanderson = turtle.Turtle()
    alanderson.shape(alanderson_shape)
    alanderson.penup()

    nascimento = turtle.Turtle()
    nascimento.shape(nascimento_shape)
    nascimento.penup()

    douglas = turtle.Turtle()
    douglas.shape(douglas_shape)
    douglas.penup()


    alanderson.goto(645, -4)
    douglas.goto(554, -4)
    nascimento.goto(465,-4)

    alanderson_mov = 0
    douglas_mov = 0
    nascimento_mov = 0

    screen.update()



def cena2():
    caminho_personagens()
    habilita_clique()
    turtle.done()
if __name__ == "__main__":
    cena2()