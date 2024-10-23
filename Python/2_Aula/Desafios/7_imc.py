def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            
            if peso <= 0 or altura <= 0:
                print("Por favor, digite valores positivos.")
                continue
            
            imc = calcular_imc(peso, altura)
            categoria = categoria_imc(imc)
            
            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Categoria: {categoria}")
            break
        except ValueError:
            print("Por favor, digite valores válidos.")

if __name__ == "__main__":
    main()