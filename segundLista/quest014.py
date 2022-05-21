'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A,
B ou C ou “REPROVADO” se o conceito for D ou E.
'''

arr_nota = []
for n in range(1, 3):
    nota = float(input('Insira a {} nota: '.format(n)))
    arr_nota.append(nota)
    
media = sum(arr_nota) / len(arr_nota)

print('Sua media foi: {:.1f}'.format(media))
if media >= 9 and media <= 10:
    print('Nota: A')
    print('Aprovado!')
elif media >= 7.5 and media < 9:
    print('Nota: B')
    print('Aprovado!')
elif media >= 6 and media < 7.5:
    print('Nota: C')
    print('Aprovado!')
elif media >= 4 and media < 6:
    print('Nota: D')
    print('Reprovado!')
elif media >= 0 and media < 4:
    print('Nota: E')
    print('Reprovado!')
