def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def main():
    print("Conversor de Temperatura")
    print("Escolha a temperatura que deseja converter:")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")

    escolha = input("Digite o número da opção desejada: ")

    if escolha in ['1', '2', '3', '4', '5', '6']:
        temperatura = float(input("Digite a temperatura: "))
        
        if escolha == '1':
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura:.2f} °C é {resultado:.2f} °F")
        elif escolha == '2':
            resultado = celsius_para_kelvin(temperatura)
            print(f"{temperatura:.2f} °C é {resultado:.2f} K")
        elif escolha == '3':
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura:.2f} °F é {resultado:.2f} °C")
        elif escolha == '4':
            resultado = fahrenheit_para_kelvin(temperatura)
            print(f"{temperatura:.2f} °F é {resultado:.2f} K")
        elif escolha == '5':
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura:.2f} K é {resultado:.2f} °C")
        elif escolha == '6':
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura:.2f} K é {resultado:.2f} °F")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()