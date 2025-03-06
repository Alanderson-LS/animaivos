#nem toda imagem já vem no tamanho adequado, usando a biblioteca pillow é possível redimensionar as imagens
#o usuário deve só ignorar isso aqui, é mais para desenvolvedores

#os é uma biblioteca que já vem instalada em qualquer executador python
import os
#a biblioteca pillow raramente vem instalada, então tenho que fazer o programa instalá-la caso dê erro

#tenta importar Image da PIL
try:
    from PIL import Image
#se der ImportError vai usar a biblioteca os pra instalar automaticamente
except ImportError:
    os.system("pip install pillow")

def redimensionar_imagem(caminho_entrada, caminho_saida, largura, altura):
    #deixa a imagem aberta na biblioteca pillow pra ela ler a imagem
    with Image.open(caminho_entrada) as img:
        #cria uma variavel nova, que usa a img que é a imagem aberta e a redimensiona com a função resize do img
        img_redimensionada = img.resize((largura, altura))
        img_redimensionada.save(caminho_saida)

redimensionar_imagem("pacote/personagens/douglas.gif", "pacote/personagens/douglas_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/personagens/nascimento.gif", "pacote/personagens/nascimento_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/personagens/alanderson.gif", "pacote/personagens/alanderson_redimensionado.gif", 100, 100)
redimensionar_imagem("pacote/fundos/rua.png", "pacote/fundos/rua_redimensionada.gif", 800, 800)
redimensionar_imagem("pacote/personagens/alanderson_falando.png","pacote/personagens/alanderson_falando.gif", 100, 100)
redimensionar_imagem("pacote/personagens/gabriel_falando.png","pacote/personagens/nascimento_falando.gif", 100, 100)
redimensionar_imagem("pacote/personagens/douglas_falando.png","pacote/personagens/douglas_falando.gif", 100, 100)
redimensionar_imagem("pacote/fundos/corredor.jpeg", "pacote/fundos/corredor_redimensionado.gif", 800, 800)
