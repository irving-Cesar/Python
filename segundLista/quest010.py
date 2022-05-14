turno = str(input('Digite seu turno:\nM - Matutino\nV - Verspertino\n'))
turno = turno.lower()
if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde!')
else: 
    print('Valor inválido.')
