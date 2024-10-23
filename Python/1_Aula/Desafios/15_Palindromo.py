frase = input('Digite uma frase: ')

frase_sem_espacos = ''.join(frase.split())

palindromo = True

for i in range(len(frase_sem_espacos) // 2):
    if frase_sem_espacos[i] != frase_sem_espacos[-i - 1]:
        palindromo = False
        break

if palindromo: print(f'A frase "{frase}" é um palíndromo.')
else: print(f'A frase "{frase}" não é um palíndromo.')