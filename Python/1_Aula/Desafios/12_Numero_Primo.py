num = int(input('Digite um número inteiro: '))

primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break

if primo:
    print(f'O número {num} é primo.')
    
else: 
    print(f'O número {num} não é primo.')