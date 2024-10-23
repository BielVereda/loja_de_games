num = float(input("Digite um número: "))

print(f"Tabuada do número... {num}:")

for numeros in range(1,11):
    print(f"{num} X {numeros} = {num*numeros}")