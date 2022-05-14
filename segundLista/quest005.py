nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
calc_media = (nota1 + nota2) / 2

if calc_media == 10:
    print('Aprovado com Distinção!')
elif calc_media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
