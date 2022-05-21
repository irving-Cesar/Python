'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
b) A mensagem "Reprovado", se a média for menor do que sete;
c) A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
calc_media = (nota1 + nota2) / 2

if calc_media == 10:
    print('Aprovado com Distinção!')
elif calc_media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
