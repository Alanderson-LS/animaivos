from pacote.nucleo import fala_2, andar

import turtle
import time

def corredor_personagens(screen = turtle.Screen()):
    global alanderson, nascimento, douglas, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape, irapuan, jurandy, alanderson_mov, nascimento_mov, douglas_mov
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
    turtle.addshape("pacote/personagens/irapuan.gif")
    turtle.addshape("pacote/personagens/jurandy.gif")
    
    turtle.addshape("pacote/personagens/nascimento_andando_1.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_2.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_3.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_4.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_5.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_6.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_7.gif")
    turtle.addshape("pacote/personagens/nascimento_andando_8.gif")

    turtle.addshape("pacote/personagens/douglas_andando_1.gif")
    turtle.addshape("pacote/personagens/douglas_andando_2.gif")
    turtle.addshape("pacote/personagens/douglas_andando_3.gif")
    turtle.addshape("pacote/personagens/douglas_andando_4.gif")
    turtle.addshape("pacote/personagens/douglas_andando_5.gif")
    turtle.addshape("pacote/personagens/douglas_andando_6.gif")
    turtle.addshape("pacote/personagens/douglas_andando_7.gif")
    turtle.addshape("pacote/personagens/douglas_andando_8.gif")

    turtle.addshape("pacote/personagens/alanderson_andando_1.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_2.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_3.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_4.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_5.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_6.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_7.gif")
    turtle.addshape("pacote/personagens/alanderson_andando_8.gif")

    n_mov_1 = ("pacote/personagens/nascimento_andando_1.gif")
    n_mov_2 =("pacote/personagens/nascimento_andando_2.gif")
    n_mov_3 =("pacote/personagens/nascimento_andando_3.gif")
    n_mov_4 =("pacote/personagens/nascimento_andando_4.gif")
    n_mov_5 =("pacote/personagens/nascimento_andando_5.gif")
    n_mov_6 =("pacote/personagens/nascimento_andando_6.gif")
    n_mov_7 =("pacote/personagens/nascimento_andando_7.gif")
    n_mov_8 =("pacote/personagens/nascimento_andando_8.gif")

    d_mov_1 =("pacote/personagens/douglas_andando_1.gif")
    d_mov_2 =("pacote/personagens/douglas_andando_2.gif")
    d_mov_3 =("pacote/personagens/douglas_andando_3.gif")
    d_mov_4 =("pacote/personagens/douglas_andando_4.gif")
    d_mov_5 =("pacote/personagens/douglas_andando_5.gif")
    d_mov_6 =("pacote/personagens/douglas_andando_6.gif")
    d_mov_7 =("pacote/personagens/douglas_andando_7.gif")
    d_mov_8 =("pacote/personagens/douglas_andando_8.gif")

    a_mov_1 =("pacote/personagens/alanderson_andando_1.gif")
    a_mov_2 =("pacote/personagens/alanderson_andando_2.gif")
    a_mov_3 =("pacote/personagens/alanderson_andando_3.gif")
    a_mov_4 =("pacote/personagens/alanderson_andando_4.gif")
    a_mov_5 =("pacote/personagens/alanderson_andando_5.gif")
    a_mov_6 =("pacote/personagens/alanderson_andando_6.gif")
    a_mov_7 =("pacote/personagens/alanderson_andando_7.gif")
    a_mov_8 =("pacote/personagens/alanderson_andando_8.gif")

    alanderson_shape = ("pacote/personagens/alanderson_grande.gif")
    nascimento_shape = ("pacote/personagens/nascimento_grande.gif")
    douglas_shape = ("pacote/personagens/douglas_grande.gif")
    alanderson_falando = ("pacote/personagens/alanderson_falando_grande.gif")
    nascimento_falando = ("pacote/personagens/nascimento_falando_grande.gif")
    douglas_falando = ("pacote/personagens/douglas_falando_grande.gif")

    jurandy_shape = ("pacote/personagens/jurandy.gif")
    irapuan_shape = ("pacote/personagens/irapuan.gif")
    
    


    turtle.tracer(0)

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
    irapuan.shape(irapuan_shape)    
    irapuan.penup()
    

    jurandy = turtle.Turtle()
    jurandy.shape(jurandy_shape)
    jurandy.penup()

    alanderson.goto(-700, -250)
    douglas.goto(-600, -250)
    nascimento.goto(-450, -250)

    irapuan.goto(-60, -250)
    jurandy.goto(60, -250)
    jurandy.right(180)

    alanderson_mov = 0
    douglas_mov = 0
    nascimento_mov = 0

    screen.update()



def trocar_shape(personagem: turtle.Turtle, shape_1: str, shape_2: str, shape_3: str, shape_4: str, shape_5: str, shape_6, shape_7, shape_8):
    global alanderson_mov, douglas_mov, nascimento_mov
    global alanderson, nascimento, douglas, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape, irapuan, jurandy, alanderson_mov, nascimento_mov, douglas_mov
    global n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8
    global d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8
    global a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8
    
    if personagem == alanderson:
        if alanderson_mov == 0:
            alanderson.shape(shape_1)
            alanderson_mov += 1
        elif alanderson_mov == 1:
            alanderson.shape(shape_2)
            alanderson_mov +=1
        elif alanderson_mov == 2:
            alanderson.shape(shape_3)
            alanderson_mov += 1
        elif alanderson_mov == 3:
            alanderson.shape(shape_4)
            alanderson_mov += 1
        elif alanderson_mov == 4:
            alanderson.shape(shape_5)
            alanderson_mov += 1
        elif alanderson_mov == 5:
            alanderson.shape(shape_6)
            alanderson_mov += 1
        elif alanderson_mov == 6:
            alanderson.shape(shape_7)
            alanderson_mov += 1
        elif alanderson_mov == 7:
            alanderson.shape(shape_8)
            alanderson_mov %= 7
    
    elif personagem == nascimento:
        if nascimento_mov == 0:
            nascimento.shape(shape_1)
            nascimento_mov += 1
        elif nascimento_mov == 1:
            nascimento.shape(shape_2)
            nascimento_mov += 1
        elif nascimento_mov == 2:
            nascimento.shape(shape_3)
            nascimento_mov += 1
        elif nascimento_mov == 3:
            nascimento.shape(shape_4)
            nascimento_mov += 1
        elif nascimento_mov == 4:
            nascimento.shape(shape_5)
            nascimento_mov += 1
        elif nascimento_mov == 5:
            nascimento.shape(shape_6)
            nascimento_mov += 1
        elif nascimento_mov == 6:
            nascimento.shape(shape_7)
            nascimento_mov += 1
        elif nascimento_mov == 7:
            nascimento.shape(shape_8)
            nascimento_mov %= 7
    
    elif personagem == douglas:
        if douglas_mov == 0:
            douglas.shape(shape_1)
            douglas_mov += 1
        elif douglas_mov == 1:
            douglas.shape(shape_2)
            douglas_mov += 1
        elif douglas_mov == 2:
            douglas.shape(shape_3)
            douglas_mov += 1
        elif douglas_mov == 3:
            douglas.shape(shape_4)
            douglas_mov += 1
        elif douglas_mov == 4:
            douglas.shape(shape_5)
            douglas_mov += 1
        elif douglas_mov == 5:
            douglas.shape(shape_6)
            douglas_mov += 1
        elif douglas_mov == 6:
            douglas.shape(shape_7)
            douglas_mov += 1
        elif douglas_mov == 7:
            douglas.shape(shape_8)
            douglas_mov %= 7




def movimento1(screen = turtle.Screen()):
    while nascimento.xcor() != -210:
        
        andar(nascimento, 10, 0)
        time.sleep(0.1)
        trocar_shape(nascimento, n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8)
        screen.update()

        andar(douglas, 10, 0)
        time.sleep(0.1)
        trocar_shape(douglas, d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()
    
    while douglas.xcor()!= -210:
        
        andar(nascimento, 10, 10)
        time.sleep(0.1)
        trocar_shape(nascimento, n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8)
        screen.update()

        andar(douglas, 10, 0)
        time.sleep(0.1)
        trocar_shape(douglas, d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()

    while alanderson.xcor() != -210:

        andar(nascimento, 10, 10 if nascimento.ycor() < 13 else 0)
        time.sleep(0.1)
        trocar_shape(nascimento, n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8)
        screen.update()

        andar(douglas, 10, 10)
        time.sleep(0.1)
        trocar_shape(douglas, d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8)
        screen.update()

        andar(alanderson, 10, 0)
        time.sleep(0.1)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()

    while nascimento.xcor() < 250:

        andar(nascimento, 10, 0)
        time.sleep(0.1)
        trocar_shape(nascimento, n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8)
        screen.update()

        andar(douglas, 10,  10 if douglas.ycor() < 13 else 0)
        time.sleep(0.1)
        trocar_shape(douglas, d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8)
        screen.update()

        andar(alanderson, 10, 10)
        time.sleep(0.1)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()

    nascimento.hideturtle()
    screen.update()
    
    while douglas.xcor() < 250:
        andar(douglas, 10,  0)
        time.sleep(0.15)
        trocar_shape(douglas, d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8)
        screen.update()

        andar(alanderson, 10, 10 if alanderson.ycor() < 0 else 0)
        time.sleep(0.15)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()

    douglas.hideturtle()
    screen.update()

    while alanderson.xcor() < 250:
        andar(alanderson, 10, 0)
        time.sleep(0.3)
        trocar_shape(alanderson, a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8)
        screen.update()

    alanderson.hideturtle()
    screen.update()

def cena3(screen = turtle.Screen()):
    global alanderson, nascimento, douglas, balao, alanderson_falando, alanderson_shape, douglas_falando, douglas_shape, nascimento_falando, nascimento_shape, irapuan, jurandy, alanderson_mov, nascimento_mov, douglas_mov
    global n_mov_1, n_mov_2, n_mov_3, n_mov_4, n_mov_5, n_mov_6, n_mov_7, n_mov_8
    global d_mov_1, d_mov_2, d_mov_3, d_mov_4, d_mov_5, d_mov_6, d_mov_7, d_mov_8
    global a_mov_1, a_mov_2, a_mov_3, a_mov_4, a_mov_5, a_mov_6, a_mov_7, a_mov_8
    corredor_personagens()
    screen.tracer(1)
    fala_2(irapuan, "Ei, esses galadinho de InfoV só fez bagunça no ônibus", 70, 140, 5)
    fala_2(jurandy, "Oxi, quero ir denovo pra um passeio com essa galera, os caba é resenha demais", 135, 160, 5)
    fala_2(irapuan, "Ixi, eu é que não vou denovo, tu que se lasque kkkk", 70, 140, 5)
    fala_2(jurandy, "Oloco Pupu, tá desumilde hein", 135, 160, 5)
    fala_2(irapuan, "Ai dento", 70, 140, 5)
    screen.tracer(0)
    movimento1()
    screen.tracer(1)
    fala_2(irapuan, "Vix, os doido quase escuta nois", 70, 140, 5)
    fala_2(jurandy, "Tu que ia se lascar, KKKKKKKK", 135, 160, 5)
    fala_2(irapuan, "Ai dento²", 70, 140, 5)
    fala_2(jurandy, "Relaxe nóia, tem uma provinha bem massa esperando eles", 135, 160, 5)
    fala_2(irapuan, "É O KARMA PELO PASSEIO HAHWAHAHHAHAHHA", 135, 140, 5)

    time.sleep(5)

    irapuan.hideturtle()
    jurandy.hideturtle
    alanderson.hideturtle()
    douglas.hideturtle()
    nascimento.hideturtle()
    irapuan.clear()
    jurandy.clear()
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
    alanderson_mov = None
    douglas_mov = None
    nascimento_mov = None
    a_mov_1 = None
    a_mov_2 = None
    a_mov_3 = None
    a_mov_4 = None
    a_mov_5 = None
    a_mov_6 = None
    a_mov_7 = None
    a_mov_8 = None
    d_mov_1 = None
    d_mov_2 = None
    d_mov_3 = None
    d_mov_4 = None
    d_mov_5 = None
    d_mov_6 = None
    d_mov_7 = None
    d_mov_8 = None
    n_mov_1 = None
    n_mov_2 = None
    n_mov_3 = None
    n_mov_4 = None
    n_mov_5 = None
    n_mov_6 = None
    n_mov_7 = None
    n_mov_8 = None

    
    screen.resetscreen()

if __name__ == "__main__":
    cena3()
