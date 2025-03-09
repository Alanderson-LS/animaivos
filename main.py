"""
Módulo principal
"""

import turtle

from pacote.nucleo import carrega_img_fundo, fala, habilita_clique

# Do módulo menus, do pacote ______, import o menu_principal
from pacote.menus import menu_principal

from cena1 import cena1
from cena2 import cena2
from cena3 import cena3
from cena4 import cena4

def criar_screen():
    screen = turtle.Screen()
    screen.setup(800, 800)
    return screen

screen = turtle.Screen()

def limpar_personagens():
    # Esconde e limpa todos os personagens
    for t in turtle.turtles():
        t.hideturtle()
        t.clear()

# Função principal
def main():
    op = int(input(menu_principal))
    limpar_personagens()
    screen.update()
    while op != 5:
        if op == 1:
            cena1(screen)
        elif op == 2:
            cena2(screen)
        elif op == 3:
            cena3(screen)
        elif op == 4:
            cena4(screen)
        else:
            print("Opção inválida.")
        op = int(input(menu_principal))

    # turtle.done()

# Chamada da função principal
if __name__ == "__main__":
    main()

