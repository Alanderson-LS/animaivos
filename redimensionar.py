#nem toda imagem já vem no tamanho adequado, usando a biblioteca pillow é possível redimensionar as imagens

from pacote.personagens import *

import os
try:
    from PIL import Image
except ImportError:
    os.system("pip install pillow")

def redimensionar_imagem(caminho_entrada, caminho_saida, largura, altura):
    with Image.open(caminho_entrada) as img:
        img_redimensionada = img.resize((largura, altura))
        img_redimensionada.save(caminho_saida)

redimensionar_imagem("pacote/personagens/douglas.gif", "pacote/personagens/douglas_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/personagens/nascimento.gif", "pacote/personagens/nascimento_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/personagens/alanderson.gif", "pacote/personagens/alanderson_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/fundos/rua.png", "pacote/fundos/rua_redimensionada.gif", 800, 800)
redimensionar_imagem("pacote/personagens/alanderson_falando.png","pacote/personagens/alanderson_falando.gif", 100, 100)
redimensionar_imagem("pacote/personagens/gabriel_falando.png","pacote/personagens/nascimento_falando.gif", 100, 100)
redimensionar_imagem("pacote/personagens/douglas_falando.png","pacote/personagens/douglas_falando.gif", 100, 100)