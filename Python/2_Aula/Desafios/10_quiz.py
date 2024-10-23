def main():
    # Lista de perguntas, onde cada pergunta é uma tupla
    perguntas = [
        ("Qual é a capital da França?", ["A) Londres", "B) Paris", "C) Berlim", "D) Madrid"], "B"),
        ("Qual é o maior planeta do sistema solar?", ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"], "C"),
        ("Quem escreveu 'Dom Casmurro'?", ["A) Machado de Assis", "B) José de Alencar", "C) Érico Veríssimo", "D) Clarice Lispector"], "A"),
        ("Qual é a fórmula da água?", ["A) H2O", "B) O2", "C) CO2", "D) NaCl"], "A"),
        ("Em que ano ocorreu a independência do Brasil?", ["A) 1822", "B) 1889", "C) 1500", "D) 1750"], "A")
    ]

    acertos = 0

    print("Bem-vindo ao Quiz!\n")

    # Loop para passar pelas perguntas
    for pergunta, opcoes, resposta_correta in perguntas:
        print(pergunta)
        for opcao in opcoes:
            print(opcao)
        
        resposta = input("Digite a letra da sua resposta: ").strip().upper()

        if resposta == resposta_correta:
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Incorreto! A resposta correta era {resposta_correta}.\n")

    # Exibe o total de acertos
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")

if __name__ == "__main__":
    main()