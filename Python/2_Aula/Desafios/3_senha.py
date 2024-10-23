import random

def gerar_senha(comprimento):
    # Define os conjuntos de caracteres manualmente
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # Combina todos os caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    # Gera a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(comprimento))
    return senha

def main():
    # Solicita o comprimento da senha ao usuário
    while True:
        try:
            comprimento = int(input("Digite o comprimento da senha (mínimo 4): "))
            if comprimento < 4:
                print("O comprimento deve ser no mínimo 4.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    senha = gerar_senha(comprimento)
    print(f"Sua senha aleatória gerada é: {senha}")

if __name__ == "__main__":
    main()