import random

def marcas_monitor():
    marcas = ["BenQ", "LG", "AOC", "SAMSUMG", "Dell"]
    return random.choice(marcas)

def cor_gabinete():
    cores = ["azul", "vermelho", "verde", "roxo", "branco", "preto"]
    return random.choice(cores)

def placa_mae():
    placas = ["Asus", "AMD", "Gigabyte"]
    return random.choice(placas)

def ventoinhas():
    fans = ["Sem fans", "Com fans", "Com fans (RGB)"]
    return random.choice(fans)

def processador():
    processadores = ["Intel", "Ryzen"]

    if processadores == "Intel":
        tipo_intel = ["i3", "i5", "i7", "i9"]
        return random.choice(tipo_intel)
    
    else:
        tipo_ryzen = ["Ryzen 3", "Ryzen 5", "Ryzen 7", "Ryzen 9"]
        return random.choice(tipo_ryzen)

def memoria_ram():
    ram = ["4GB", "8GB", "16GB", "32GB"]
    return random.choice((ram))

def tipo_memoria():
    memoria = ["HD", "SSD"]
    return random.choice((memoria))

def tamanho_memoria():
    tamanho  = ["128GB","256GB", "512GB", "1TB", "2TB"]
    return random.choice((tamanho))

def marca_fonte():
    fontes  = ["Asus", "Corsair", "ATX"]
    return random.choice((fontes))

def placa_video():
    placa_de_video  = ["RTX","GTX", "GT", "RX"]
    return random.choice((placa_de_video))

def pc_completo():

    print("Esse são as peças que pensamos para colocar em seu PC:")
    print(f"\nMarca do monitor: {marcas_monitor()}")
    print(f"Cor do gabinete: {cor_gabinete()}")
    print(f"Placa-mãe: {placa_mae()}")
    print(f"Fans: {ventoinhas()}")
    print(f"Marca do processador: {processador()}")
    print(f"Memória RAM: {memoria_ram()}")
    print(f"Tipo de memória: {tipo_memoria()}")
    print(f"Tamanho da memória: {tamanho_memoria()}")
    print(f"Marca da fonte: {marca_fonte()}")
    print(f"Placa de vídeo: {placa_video()}")
##########################################################################################
nome = str(input("Digite o seu nome: "))

print(f"\nOlá, {nome.capitalize()}, seja bem-vindo à nossa loja!")
print("Vamos mostrar para você o melhor PC de acordo com o seu perfil, ok?\n")

print(pc_completo())