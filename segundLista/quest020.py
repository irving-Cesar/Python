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
