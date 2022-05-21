'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
gen = str(input('Insira um letra: '))
gen = gen.lower()

if gen == 'f':
    print('Feminino')
elif gen == 'm':
    print('Masculino') 
else:
    print('Sexo inválido.')
