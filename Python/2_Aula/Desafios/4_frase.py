def contar_palavras(frase):
    palavras = frase.split()
    contagem = {}

    for palavra in palavras:
        palavra = palavra.lower()

        if palavra in contagem:
            contagem[palavra] += 1
            
        else:
            contagem[palavra] = 1
    
    return contagem

def main():

    frase = input("Digite uma frase: ")
    contagem = contar_palavras(frase)
    total_palavras = sum(contagem.values())
    print(f"Número total de palavras: {total_palavras}")
    print("Frequência de cada palavra:")

    for palavra, frequencia in contagem.items():
        print(f"{palavra}: {frequencia}")

if __name__ == "__main__":
    main()