'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = str(input('Insira um letra: '))
vogais = ['a', 'e', 'i', 'o', 'u']

print('Vogal' if letra in vogais else 'Consoante')
