def adicionar_contato(agenda, nome, telefone):
    if nome in agenda:
        print(f"O contato '{nome}' já existe.")
    else:
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso.")

def visualizar_contatos(agenda):
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("Contatos na Agenda:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado.")

def main():
    agenda = {}
    
    while True:
        print("\nAgenda Telefônica:\n")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone: ")
            adicionar_contato(agenda, nome, telefone)
        
        elif escolha == '2':
            visualizar_contatos(agenda)
        
        elif escolha == '3':
            nome = input("Digite o nome do contato a ser removido: ")
            remover_contato(agenda, nome)
        
        elif escolha == '4':
            print("Saindo da agenda.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()