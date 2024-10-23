import random

num_ale = random.randint(1, 100)

while True:

    escolha = int(input("\nDigite um número (entre 1 e 100): "))

    if escolha < num_ale:
        print("O seu número é menor do que o escolhido pelo computador.")
        continue

    elif escolha > num_ale:
        print("O seu número é maior do que o escolhido pelo computador.")
        continue

    elif escolha == num_ale:
        print("Parabéns, você acertou o número escolhido pelo computador!")
        break

    else:
        print("Número inválido, tente novamente!")
        continue