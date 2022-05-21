'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
turno = str(input('Digite seu turno:\nM - Matutino\nV - Verspertino\n'))
turno = turno.lower()
if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde!')
else: 
    print('Valor inválido.')
