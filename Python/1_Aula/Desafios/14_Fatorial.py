num = int(input("Digite um número: "))
contador = num
fatorial = 1

if contador == 0:
    print("0! = 0")

print(f"{num}! = ", end="")

while contador >= 1:
    print(contador," X ", end="")
    fatorial *= contador
    contador -= 1

    if num == 1:
        print("=", end = "")

    else:
        print(num, end=" X ")

print(f"1 = {fatorial}")