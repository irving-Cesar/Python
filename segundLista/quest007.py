for n in range(1, 4):
    num = int(input('Insira o {}° numero: '.format(n)))
    if n == 1:
        maior = num
        menor = num
        
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
    
print('Maior {} e menor {}'.format(maior, menor))
