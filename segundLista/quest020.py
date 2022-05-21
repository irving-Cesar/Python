'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    °A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    °A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    °A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
notas = []
for n in range(3):
    nota = float(input(f'Insira a {n+1}° nota: '))
    notas.append(nota)
    
media = sum(notas) / len(notas)


if media == 10 and media:
    print(f'Aprovado com Distinção! Com a média de {media:.1f}!')
    
elif media >= 7 and media:
    print(f'Aprovado! Com a média de {media:.1f}!')

elif media < 7 and media:
    print(f'Reprovado! Com a média de {media:.1f}!')
