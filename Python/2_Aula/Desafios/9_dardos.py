import random

def lançar_dado():
    return random.randint(1, 6)

def main():
    print("Simulador de Lançamento de Dados")
    
    while True:
        input("Pressione Enter para lançar o dado...")
        resultado = lançar_dado()
        print(f"O resultado do lançamento é: {resultado}")

        continuar = input("Deseja lançar o dado novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()