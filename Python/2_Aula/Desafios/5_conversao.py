def converter_moeda(valor_em_reais, moeda):
    # Taxas de câmbio fictícias
    taxas_de_cambio = {
        'USD': 5.20,  # 1 Real = 5.20 Dólares
        'EUR': 6.10,  # 1 Real = 6.10 Euros
    }
    
    if moeda in taxas_de_cambio:
        valor_convertido = valor_em_reais / taxas_de_cambio[moeda]
        return valor_convertido
    else:
        return None

def main():
    # Solicita o valor em reais
    while True:
        try:
            valor_em_reais = float(input("Digite o valor em Reais (BRL): "))
            if valor_em_reais < 0:
                print("Por favor, digite um valor positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    # Solicita a moeda para conversão
    moeda = input("Digite a moeda para a qual deseja converter (USD, EUR): ").strip().upper()
    
    # Converte o valor
    valor_convertido = converter_moeda(valor_em_reais, moeda)
    
    if valor_convertido is not None:
        print(f"{valor_em_reais} Reais equivalem a {valor_convertido:.2f} {moeda}.")
    else:
        print("Moeda não reconhecida. Por favor, escolha USD ou EUR.")

if __name__ == "__main__":
    main()