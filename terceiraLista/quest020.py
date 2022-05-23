'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando
o fatorial a números inteiros positivos e menores que 16.
'''
loop = True
while loop:
    num = int(input('Insira um número inteiro positivo: '))
    if num < 0 or num > 16:
        print('Insira números inteiros positivos e menores que 16.')
        continue
    else:
        v = num
        for i in range(num):
            v = (v-1)
            if num * v != 0:
                num  = num * v
                
        print(f'Resultado: {num} ')
    
    exit = str(input('Finalizar programa?\ns - n: '))
    loop = False if exit == 's' else loop
