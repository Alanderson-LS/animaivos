from glob import glob
import os
import time
import turtle
from pathlib import Path

# Configurações do balão

def carrega_personagens():
    """Carrega os personagens da animação.

    Carrega os personagens da animação, que são arquivos .gif
    presentes no diretório 'personagens' do pacote.
    """

    cam_personagens = Path(__file__).parent / "personagens"
    cam_atual = Path.cwd()

    os.chdir(cam_personagens.as_posix())
    for img in glob("*.gif"):
        turtle.register_shape(img)

    os.chdir(cam_atual.as_posix())


def andar(personagem: turtle.Turtle, horizontal: int, vertical: int):
    personagem.goto(personagem.xcor() + horizontal, personagem.ycor() + vertical)

def fala(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int, 
         distancia: int,
         tempo: int,
         personagem_falando,
         personagem_shape
         ):
    global balao
    balao = turtle.Turtle()
    balao.hideturtle()
    """Exibe um balão de fala para um personagem.

    Exibe um balão de fala para um personagem, com o texto
    passado como parâmetro, em um ângulo e distância específicos.
    """
    
    balao.up()
    x,y = personagem.pos()

    balao.goto(x, y) 
    balao.down() 
    balao.left(angulo) 
    balao.forward(distancia)
    balao.write(texto)
    for i in range(tempo):
        personagem.shape(personagem_falando)
        time.sleep(0.5)
        personagem.shape(personagem_shape)
        time.sleep(0.5)
    balao.undo()
    balao.undo()
    balao.undo()

def fala_2(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int, 
         distancia: int,
         tempo: int
         ):
    global balao
    balao = turtle.Turtle()
    balao.hideturtle()
    """Exibe um balão de fala para um personagem.

    Exibe um balão de fala para um personagem, com o texto
    passado como parâmetro, em um ângulo e distância específicos.
    """
    
    balao.up()
    x,y = personagem.pos()

    balao.goto(x, y) 
    balao.down() 
    balao.left(angulo) 
    balao.forward(distancia)
    balao.write(texto)
    time.sleep(tempo)
    balao.undo()
    balao.undo()
    balao.undo()

def carrega_img_fundo(img_fundo: str):
    """Carrega uma imagem de fundo para a tela.

    Carrega uma imagem de fundo para a tela, que é um arquivo .gif
    presente no diretório 'fundos' do pacote.
    """

    cam_img_fundo = Path(__file__).parent / "fundos" / img_fundo

    if cam_img_fundo.exists() and cam_img_fundo.is_file():
        turtle.bgpic(cam_img_fundo.as_posix())
    else:
        print(cam_img_fundo.as_posix())
        print('Imagem de fundo não encontrada!')


def exibir_coordenadas(x: float, y: float) -> None:
    """Exibe as coordenadas de um clique do mouse.
    """

    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")
    
    # Exibe as coordenadas na tela com o turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"({x:0.0f}, {y:0.0f})", font=("Arial", 12, "normal"))
    turtle.stamp()

def habilita_clique() -> None:
    """Habilita o clique do mouse na tela.
    """

    tela = turtle.Screen()
    tela.title("Clique para ver as coordenadas do mouse")
    tela.onclick(exibir_coordenadas)

