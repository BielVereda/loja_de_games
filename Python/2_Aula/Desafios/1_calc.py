print("Seja bem vindo à calculadora!")
print("Vamos começar.")

nome = str(input("Digite o seu nome: "))

def subtracao (x, y):
  return x - y

def adicao (x, y):
  return x + y

def divisao (x, y):
  return x / y

def multiplicacao (x, y):
  return x * y

calc = int(input(f"{nome}, escolha a operação desejada: \n""1 - Adição.\n""2 - Subtração.\n""3 - Divisão.\n""4 - Multiplicação.\n"f"{nome}, Informe a operação desejada: "))
x = float(input(f"{nome}, digite o primeiro número: "))
y = float(input(f"{nome}, digite o segundo número: "))



if (calc == "1"):
  result = x + y
  print(f'{nome} "o resultado de" {x} "+" {y} "=" {result}') 

elif (calc == "2"):
  result = x - y
  print(f'{nome} "o resultado de" {x} "-" {y} "=" {result}') 
  

elif (calc == "3"):
  result = x/y
  print(f'{nome} "o resultado de" {x} ":" {y} "=" {result}') 
  

elif (calc == "4"):
  result = x*y
print(f'{nome} "o resultado de" {x} "x" {y} "=" {result}')