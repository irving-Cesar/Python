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
