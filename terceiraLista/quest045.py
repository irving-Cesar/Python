'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
final comparar com o gabarito da prova e assim calcular o total de acertos e a 
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema 
deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos 
os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

    Gabarito da Prova:
    
    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A
    
Após concluir isto você poderia incrementar o programa permitindo que o
professor digite o gabarito da prova antes dos alunos usarem o programa.
'''
from random import randint

# Letras das alternativas (não o resultado)
arr_alter = ['A', 'B', 'C', 'D', 'E']

#guardar o resultado
arr_questoes = []

# verificar se o preenchimento vai ser automatico ou manual
professor = int(input('O professor deseja digitar o gabarito de antemão?\n0 - Não\n1 - Sim\n'))
for questao in range(1, 11):
    gabarit = ''
    pergunta = {}
    if professor == 1:
        while gabarit.upper() not in arr_alter:
            gabarit = str(input(f'Insira a alternativa da questao {questao}: '))
            gabarit = gabarit.upper()
            if gabarit not in arr_alter:
                print('Por Favor, insira um valor válido.')
    else: 
        gabarit = arr_alter[randint(0, 4)]
        
    pergunta = {
        'questao': questao,
        'alternativa': gabarit
    }
    arr_questoes.append(pergunta)
    gabarit = ''

arr_alunos = []
continuar = ''
media_turma = 0
cont_aluno = 0
loop = True
while loop:
    cont_aluno += 1 # contador de aluno
    cont_quest = 1 # contador de questao
    aluno_acertos = 0
    aluno_choose = '' 
    aluno = {} # guardar o número e acertos do aluno
    for c in range(len(arr_questoes)):
        
        # realizando o teste do aluno
        while aluno_choose.upper() not in arr_alter:
            aluno_choose = str(input(f'\nAluno {cont_aluno}, qual é a alternativa da questão {cont_quest}?\nResposta - '))
            if aluno_choose.upper() not in arr_alter:
                print('Opção inválida.\n')

        if aluno_choose.upper() == arr_questoes[c]['alternativa']:
            aluno_acertos += 1
        
        cont_quest += 1
        aluno_choose = ''

    aluno = {
        'numero': cont_aluno,
        'acertos': aluno_acertos
    }

    media_turma += aluno_acertos
    arr_alunos.append(aluno)

    continuar = str(input('Outro aluno irá utilizar? s - n\n'))
    loop = False if continuar.lower() in 'nnaonão' else loop


maior_acerto = max(arr_alunos, key=lambda acertos: acertos['acertos'])
menor_acerto = min(arr_alunos, key=lambda acertos: acertos['acertos'])

print(f'\nForam o total de {cont_aluno} Alunos.')
print(f"Maior Acerto -> Aluno {maior_acerto['numero']} - com {maior_acerto['acertos']} pontos!")
print(f"Menor Acerto -> Aluno {menor_acerto['numero']} - com {menor_acerto['acertos']} pontos.")
print(f'A média das notas da turma foi de {media_turma/cont_aluno:.2f}')
