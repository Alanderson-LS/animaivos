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
    print ("feche e abra o executador do código para prosseguir")

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

redimensionar_imagem("pacote/personagens/alanderson.gif", "pacote/personagens/alanderson_grande.gif", 200, 200)
redimensionar_imagem("pacote/personagens/douglas.gif", "pacote/personagens/douglas_grande.gif", 240, 240)
redimensionar_imagem("pacote/personagens/nascimento.gif", "pacote/personagens/nascimento_grande.gif", 240, 240)
redimensionar_imagem("pacote/personagens/alanderson_falando.gif", "pacote/personagens/alanderson_falando_grande.gif", 240, 240)
redimensionar_imagem("pacote/personagens/nascimento_falando.gif", "pacote/personagens/nascimento_falando_grande.gif", 240, 240)
redimensionar_imagem("pacote/personagens/douglas_falando.gif", "pacote/personagens/douglas_falando_grande.gif", 240, 240)

arquivos_alan = sorted([arquivo for arquivo in os.listdir("pacote/personagens/alanderson_andando") if arquivo.endswith('.png')])
arquivos_douglas = sorted([arquivo for arquivo in os.listdir("pacote/personagens/douglas_andando") if arquivo.endswith('.png')])
arquivos_nascimento = sorted([arquivo for arquivo in os.listdir("pacote/personagens/nascimento_andando") if arquivo.endswith('.png')])


for i, arquivo in enumerate(arquivos_alan, start=1):
    caminho_entrada = os.path.join("pacote/personagens/alanderson_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"alanderson_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 200, 200)

for i, arquivo in enumerate(arquivos_douglas, start=1):
    caminho_entrada = os.path.join("pacote/personagens/douglas_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"douglas_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 240, 240)

for i, arquivo in enumerate(arquivos_nascimento, start=1):
    caminho_entrada = os.path.join("pacote/personagens/nascimento_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"nascimento_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 240, 240)

redimensionar_imagem("pacote/fundos/fundo_4.png.png", "pacote/fundos/sala.gif", 800, 800)
redimensionar_imagem("pacote/personagens/jurandy_lado.png", "pacote/personagens/jurandy.gif", 240, 240)
redimensionar_imagem("pacote/personagens/irapuan_lado.png", "pacote/personagens/irapuan.gif", 240, 240)

redimensionar_imagem("pacote/personagens/ProvinhaNormal.png.png", "pacote/personagens/prova_normal.gif", 150, 150)
redimensionar_imagem("pacote/personagens/ProvinhaAtk2,0.png.png", "pacote/personagens/prova_ataque.gif", 150, 150)
redimensionar_imagem("pacote/personagens/ProvinhaDerrotado2.png.png", "pacote/personagens/prova_dano.gif", 150, 150)
redimensionar_imagem("pacote/personagens/ProvinhaRindo1.png.png", "pacote/personagens/prova_rindo_1.gif", 150, 150)
redimensionar_imagem("pacote/personagens/ProvinhaRindo2.png.png", "pacote/personagens/prova_rindo_2.gif", 150, 150)

redimensionar_imagem("pacote/personagens/nascimento_costa.png", "pacote/personagens/nascimento_costa.gif", 100, 100)
redimensionar_imagem("pacote/personagens/alanderson_costa.png", "pacote/personagens/alanderson_costa.gif", 100, 100)
redimensionar_imagem("pacote/personagens/douglas_costa.png", "pacote/personagens/douglas_costa.gif", 100, 100)

redimensionar_imagem("pacote/fundos/foraif.png", "pacote/fundos/foraif.gif", 800, 800)

arquivos_alan_ = sorted([arquivo for arquivo in os.listdir("pacote/personagens/alanderson_andando") if arquivo.startswith('_alanderson_andando')])
arquivos_douglas_ = sorted([arquivo for arquivo in os.listdir("pacote/personagens/douglas_andando") if arquivo.startswith('_douglas_andando')])
arquivos_nascimento_ = sorted([arquivo for arquivo in os.listdir("pacote/personagens/nascimento_andando") if arquivo.startswith('_nascimento_andando')])

for i, arquivo in enumerate(arquivos_alan_, start=1):
    caminho_entrada = os.path.join("pacote/personagens/alanderson_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"_alanderson_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 50, 50)

for i, arquivo in enumerate(arquivos_douglas_, start=1):
    caminho_entrada = os.path.join("pacote/personagens/douglas_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"_douglas_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 60, 60)

for i, arquivo in enumerate(arquivos_nascimento_, start=1):
    caminho_entrada = os.path.join("pacote/personagens/nascimento_andando", arquivo)
    caminho_saida = os.path.join("pacote/personagens", f"_nascimento_andando_{i}.gif")
    redimensionar_imagem(caminho_entrada, caminho_saida, 60, 60)


print("imagens redimensionadas com sucesso")