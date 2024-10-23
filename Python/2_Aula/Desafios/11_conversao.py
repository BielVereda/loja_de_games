def metros_para_quilometros(metros):
    return metros / 1000

def gramas_para_quilos(gramas):
    return gramas / 1000

def litros_para_mililitros(litros):
    return litros * 1000

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def main():
    print("Conversor de Unidades")
    
    while True:
        print("\nEscolha a unidade que deseja converter:")
        print("\n1. Metros para Quilômetros")
        print("2. Gramas para Quilos")
        print("3. Litros para Mililitros")
        print("4. Fahrenheit para Celsius")
        print("5. Celsius para Fahrenheit")
        print("6. Sair\n")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '6':
            print("Saindo do programa.")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            valor = float(input("Digite o valor a ser convertido: "))
            
            if escolha == '1':
                resultado = metros_para_quilometros(valor)
                print(f"{valor:.2f} metros é igual a {resultado:.2f} quilômetros.")
            elif escolha == '2':
                resultado = gramas_para_quilos(valor)
                print(f"{valor:.2f} gramas é igual a {resultado:.2f} quilos.")
            elif escolha == '3':
                resultado = litros_para_mililitros(valor)
                print(f"{valor:.2f} litros é igual a {resultado:.2f} mililitros.")
            elif escolha == '4':
                resultado = fahrenheit_para_celsius(valor)
                print(f"{valor:.2f} °F é igual a {resultado:.2f} °C.")
            elif escolha == '5':
                resultado = celsius_para_fahrenheit(valor)
                print(f"{valor:.2f} °C é igual a {resultado:.2f} °F.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()