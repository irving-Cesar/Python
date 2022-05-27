'''
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
[76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

num = 0
arr_intervalo = [[0, 25], [26,50], [51,75], [76,100]]
arr_nums = []
# numeros_teste  = [0,1,2,3,4,5,20,26,31,40,53,80,90, -1]
while num >= 0:
    num = int(input('Insira um valor positivo: '))
    if num >= 0:
        arr_nums.append(num)
    else:
        for inter in arr_intervalo:
            check_qnt = 0
            for numeros in arr_nums:
                if numeros >= inter[0] and numeros <= inter[1]:
                    check_qnt += 1
            print(f'{check_qnt} no intervalo {inter}')
