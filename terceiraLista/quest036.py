'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro
que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar
em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35

Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''

num = int(input('Insira o numero: '))
inicial =  int(input('Valor inicial: '))
final =  int(input('Valor Final: '))

if inicial < final:
    print(f'Montando a tabuada de {num} começando em {inicial} e terminando em {final}:')
    for i in range(inicial, final+1):
        print(f'{num} x {inicial} = {num*inicial}')
        inicial+=1
else:
    print('Valor inicial maior que o valor final.')
    
