from pacote.nucleo import fala, fala_2, andar, habilita_clique

import turtle
import random
import time
import math

def sala_personagens(screen = turtle.Screen()):
    global alanderson
    global nascimento
    global douglas
    global prova, prova_ataque, prova_normal, prova_dano, prova_rindo_1, prova_rindo_2
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
    hp_1.hideturtle()
    hp_2 = turtle.Turtle()
    hp_2.hideturtle()

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
    fala(prova, "Só porque é palhaço tá achando que é dono do circo?", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Então vou te mostrar o show de verdade", 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)

def mensagem_pergunta():
    global hits
    if hits == 0:
        mensagem = "Vamos para a primeira pergunta!"
    if hits == 1:
        mensagem = "Foi pura sorte! Dessa vez será diferente."
    if hits == 2:
        mensagem = "Estava apenas testado vocês, não será dessa vez!"
    if hits == 3:
        mensagem = "Ok, você não são tão ruins assim, a última pergunta vai ser pesada!"

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
    falas_1 = "O clima tá quente hoje"
    falas_2 = "Culpa do aquecimento global"
    resposta = "Essa Romero falou muito, \ntempo é temporário, \nclima é uma analise dos últimos 32 anos"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    quadro()
    for _ in range(7):
        hp_1.undo()
 

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
    for _ in range(7):
        hp_1.undo()


def bhaskara():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150, 5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Qual a formula de bhaskara?", 225, 150, 5, prova_ataque, prova_normal)
    falas_1 = "Vix, qual é mesmo o sinal hein?"
    falas_2 = "Num sei dividir"
    resposta = "Menos b, mais ou menos raíz de delta, \nsobre 2 a"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    quadro()
    for _ in range(7):
        hp_1.undo()
    fala_2(prova, "Os bixo ainda sabe matemática básica, tão paiando tudo!", 225, 150, 5)


def agua_gelo():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150 ,5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "Por que a água se expande ao se solidificar?", 225, 150, 5, prova_ataque, prova_normal)
    falas_1 = "Oxi, e água expande desde quando galado?"
    falas_2 = "O sugar daddy de Kaio tinha falado algo sobre isso"
    resposta = "A água expande ao congelar porque as \nligações de hidrogênio organizam as \nmoléculas em uma estrutura cristalina aberta"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    quadro()
    for _ in range(7):
        hp_1.undo()
    fala_2(prova, "AI", 225, 150, 5)

def mol():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150 ,5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "O que é um MOL?", 225, 150, 5, prova_ataque, prova_normal)
    falas_1 = "Eitchaaaaa"
    falas_2 = "Rapaz, um MOL eu não sei, \nmas o que tu quer tá mole"
    resposta = "MOL é a maneira de contas as \npartículas de uma substância"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    quadro()
    for _ in range(7):
        hp_1.undo()
    fala_2(prova, "O que tá ficando mole sou eu \nchorei tanto que to murchando", 225, 150, 5)

def equa_pri_grau():
    global hits
    fala(prova, mensagem_pergunta(), 225, 150 ,5, prova_rindo_1, prova_rindo_2)
    prova.shape(prova_normal)
    fala(prova, "O que é uma equação de primeiro grau?", 225, 150, 5, prova_ataque, prova_normal)
    falas_1 = "Vix, essa é tão fácil que dormi na aula"
    falas_2 = "Respondo até de olho fechado essa aí"
    resposta = "É uma equação polinomial que o \nexpoente da variável X é um \ne tem formato ax + b = 0"
    responde(falas_1)
    responde(falas_2)
    responde(resposta)
    hits += 1
    time.sleep(2)
    prova.shape(prova_dano)
    quadro()
    for _ in range(7):
        hp_1.undo()
    fala_2(prova, "O que tá ficando mole sou eu \nchorei tanto que to murchando", 225, 150, 5)


def final(personagem):
    velocidade_queda = -5  #velocidade da queda (mais lenta para parecer mais suave)
    velocidade_quique = 8  #velocidade do quique (um pouco mais rápido)
    angulo_quique = 10  #o ângulo para movimentar para a direita (menor para movimento mais controlado)

    #queda inicial
    for _ in range(10):  #um movimento pequeno para a direita e um pouco para cima
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), 5)
        time.sleep(0.005)

    #simulação da queda e quique
    while personagem.ycor() > -325:  #queda até o chão
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), velocidade_queda)  # Queda
        time.sleep(0.005)

    personagem.goto(personagem.xcor(), -325)  #mini-reajuste caso não tenha ficado no lugar certo

    #inicio da kickada
    while personagem.ycor() < -200:  #subida
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), velocidade_quique)  # Subindo para a direita
        time.sleep(0.01)

    personagem.goto(personagem.xcor(), -200)  #ajuste

    # Simulação de quique 2
    while personagem.ycor() > -325:
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), velocidade_queda)  # Queda
        time.sleep(0.005)

    personagem.goto(personagem.xcor(), -325)

   
    while personagem.ycor() < -250:
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), velocidade_quique)  # Subindo para a direita
        time.sleep(0.01)

    personagem.goto(personagem.xcor(), -250)

    #boss saindo da tela após a última kickada
    while personagem.ycor() > -450:
        andar(personagem, velocidade_quique * math.sin(math.radians(angulo_quique)), -10)
        time.sleep(0.005)


def limpar_personagens():
    for t in turtle.turtles():
        t.hideturtle()
        t.clear()

perguntas = [clima_tempo, pais_continente, bhaskara, agua_gelo, mol]

escolhidas = random.sample(perguntas, 4)

def cena4(screen = turtle.Screen()):
    habilita_clique()
    sala_personagens(screen)
    start(screen)
    for pergunta in escolhidas:
        pergunta()
        if hits < 4:
            time.sleep(3)
            prova.shape(prova_normal)
            time.sleep(2)
        else:
            final(prova)
    limpar_personagens()

if __name__ == "__main__":
    cena4()

