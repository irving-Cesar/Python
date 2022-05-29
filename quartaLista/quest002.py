'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
import random

vet = []
for i in range(10):
    vet.append(round(random.uniform(0.0, 99.9), 1))
print('Antes',vet)
vet = reversed(vet)
print('Depois',list(vet))
