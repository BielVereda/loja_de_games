n = int(input("Digite um número inteiro: "))

a, b = 0, 1
contador = 0
sequencia = ""

while contador < n:
    sequencia += str(a) + " –> "
    a, b = b, a + b
    contador += 1

print(f"Os {n} primeiros elementos da sequência de Fibonacci são:")
print(sequencia)