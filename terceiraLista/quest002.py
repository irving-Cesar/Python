'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

user = ''
senha = ''

while senha == user:
    print('')
    user = str(input('Insira um usuário: '))
    senha = str(input('insira uma senha: '))
    
    if senha == user:
        print('A senha não pode ser igual ao usuario.\nTente novamente.')
    else:
        print('Conta criada com sucesso.')
