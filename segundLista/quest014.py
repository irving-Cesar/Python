arr_nota = []
for n in range(1, 3):
    nota = float(input('Insira a {} nota: '.format(n)))
    arr_nota.append(nota)
    
media = sum(arr_nota) / len(arr_nota)

if media >= 9 and media <= 10:
    print('Nota: A')
elif media >= 7.5 and media < 9:
    print('Nota: B')
elif media >= 6 and media < 7.5:
    print('Nota: C')
elif media >= 4 and media < 6:
    print('Nota: D')
elif media >= 0 and media < 4:
    print('Nota: E')
