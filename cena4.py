from pacote.nucleo import fala, fala_2, andar, habilita_clique

import turtle
import random
import time

def sala_personagens(screen = turtle.Screen()):
    global alanderson
    global nascimento
    global douglas
    global prova, prova_ataque, prova_normal, prova_dano, prova_rindo_1, prova_rindo_2
    global balao
    global hp_1, hp_2
    global hits

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

    hp_1 = turtle.Turtle()
    hp_2 = turtle.Turtle()

    hp_1.color("white")
    hp_2.color("white")

    alanderson_costa = "pacote/personagens/alanderson_costa.gif"
    douglas_costa = "pacote/personagens/douglas_costa.gif"
    nascimento_costa = "pacote/personagens/nascimento_costa.gif"

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

    prova.shape(prova_normal)

    hp_1.penup()
    hp_2.penup()
    hp_1.goto(-200, 370)
    hp_2.goto(-200, 370)
    hp_1.pendown()
    hp_2.pendown()
    for i in range(4):
        hp_1.begin_fill()
        hp_1.fillcolor()
        andar(hp_1, 0, -35)
        andar(hp_1,  75, 0)
        andar(hp_1, 0, 35)
        andar(hp_1, - 75, 0)
        hp_1.end_fill()
        andar(hp_1,  75, 0)
    for i in range(4):
        andar(hp_2, 0, -35)
        andar(hp_2,  75, 0)
        andar(hp_2, 0, 35)
        andar(hp_2, - 75, 0)
        andar(hp_2,  75, 0)
    hp_1.hideturtle()
    hp_2.hideturtle()
    hp_2.penup()
    andar(hp_2, -200, -60)
    hp_2.pendown()
    hp_2.write("boss HP: 100%")

    hits = 0
    screen.update()

def start(screen = turtle.Screen()):
    screen.tracer(1)
    fala(prova, "MWAHAHAHA, VOCÊS IRÃO REPROVAR", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala_2(alanderson, "ih ala, só pq é grande acha q é 2", 135, 100, 5)
    fala(prova, "Que? de quem você está falando?", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala_2(alanderson, "MEU PAU KKKKKKKKK", 135, 100, 5)
    fala(prova, "HA, HA, HA, MUITO ENGRAÇADINHO, NÉ?", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "ok, chega de gracinha, vamos começar a parada séria", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)

def mensagem_pergunta():
    global hits
    if hits == 0:
        mensagem = "Ok, vamos para a primeira pergunta."
    if hits == 1:
        mensagem = "Foi pura sorte! Dessa vez será diferente."
    if hits == 2:
        mensagem = "Estava apenas te testando, não será dessa vez!"
    if hits == 3:
        mensagem = "Ok, você não é tão mal assim, a última pergunta vai ser pesada!"

    return mensagem

def responde(resposta):
    nomes = [alanderson, nascimento, douglas]
    aluno = random.choice(nomes)
    if aluno == alanderson:
        fala_2(alanderson, resposta, 150, 150, 5)
    elif aluno == douglas:
        fala_2(douglas, resposta, 100, 150, 5)
    else:
        fala_2(nascimento, resposta, 60, 100, 5)

def quadro():
    global hits
    hp_2.undo()
    if hits == 1:
        hp_2.write("boss HP: 75%")
    if hits == 2:
        hp_2.write("boss HP: 50%")
    if hits == 3:
        hp_2.write("boss HP: 25%")
    if hits == 4:
        hp_2.write("boss DEFEATED!")

def clima_tempo():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Qual a diferença entre clima e tempo?", 225, 150, 5, prova_ataque, prova_normal)
    resposta = "Essa Romero falou muito, tempo é temporário, clima é uma analise dos últimos 32 anos"
    responde(resposta)
    hits += 1
    prova.shape(prova_dano)
    quadro()
    time.sleep(3)
    prova.shape(prova_normal)

def pais_continente():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Qual o maior país em território, Europa ou Espanha?", 225, 150, 5, prova_ataque, prova_normal)

    falas_1 = "Rapaz, tá certo isso?"
    falas_2 = "Pera lá, tem pegadinha nisso aí"
    falas_3 = "(pensamentos pensantes)"
    resposta = "Mas Europa não é país, é continente."
    responde(falas_1)
    responde(falas_2)
    responde(falas_3)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    fala_2(prova, "nem em pegadinha vocês caíram? T_T", 225, 150, 5)
    quadro()
    time.sleep(3)
    prova.shape(prova_normal)

def bhaskara():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Qual a formula de bhaskara?", 225, 150, 5, prova_ataque, prova_normal)
    falas_1 = "Vix, qual é mesmo o sinal hein?"
    falas_2 = "Essa pergunta tá amostradinha demais pro meu gosto"
    resposta = "Menos b, mais ou menos raíz de delta, sobre 2 a"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    fala_2(prova, "Os bixo ainda sab")


perguntas = [clima_tempo, pais_continente]

def cena4(screen = turtle.Screen()):
    habilita_clique()
    sala_personagens(screen)
    start(screen)
    clima_tempo()
    pais_continente()
    turtle.done()

if __name__ == "__main__":
    cena4()