'''
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média
de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
p = int(input('Insira a quantidade de pessoas: '))
arr_idade = []
media = 0
for i in range(p):
    idade = int(input(f'Insira a idade da {i+1}° pessoa: '))
    arr_idade.append(idade)

media = (sum(arr_idade))/(len(arr_idade))
if media > 60:
    print('Turma Idosa.')
elif media >= 26 and media <= 60:
    print('Turma Adulta.')
elif media >= 1 and media <= 25:
    print('Turma Jovem.')
