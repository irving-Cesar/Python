'''
Encontrar números primos é uma tarefa difícil
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
'''

intervalo = int(input('Insira o intervalo: '))
arr_primos = []

for i in range(1, intervalo+1):
    contador = 0
    for j in range(1, i+1):
        if i % j == 0:
            contador += 1
            
    if contador == 2:
        arr_primos.append(i)

print(arr_primos)
