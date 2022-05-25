'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um 
programa que pergunte a cada um dos clientes da academia seu código, sua altura 
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar
0 (zero) no campo código. Ao encerrar o programa também deve ser informados os 
códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
'''
import random

cod_client = 1
id_client = 1
arr_altura = []
arr_peso = []
arr_clientes = []
arr_values = []
arr_tedio = ['Maior altura', 'Menor altura', 'Maior peso', 'Menor peso']

while cod_client != 0:
    cod_client = int(input(f'\nCliente N°{id_client}, insira seu código: '))
    # cod_client = random.randint(1000, 9999) # testes
    if cod_client != 0:
        # altura = round(random.uniform(1.5, 2.1), 2) # testes
        # peso = round(random.uniform(50, 110), 1)  # testes
        altura = float(input('Insira a sua altura: '))
        peso = float(input('Insira o seu peso: '))
        
        arr_altura.append(altura)
        arr_peso.append(peso)
        
        arr_clientes.append([id_client, altura, peso, cod_client])
        id_client += 1
        
    else:
        arr_values += [
            max(arr_clientes, key=lambda alt: alt[1]),
            min(arr_clientes, key=lambda alt: alt[1]),
            max(arr_clientes, key=lambda pes: pes[2]),
            min(arr_clientes, key=lambda pes: pes[2])
        ]
        for c, l in zip(arr_values, range(len(arr_tedio))):
            result = (f"{arr_tedio[l]} -> Id: {c[0]} - Altura: {c[1]} - Peso: {c[2]} - Código: {c[3]}")
            print(result)
            
        print(f'\nMédia Altura: {sum(arr_altura)/len(arr_altura):.1f} - Média Peso: {sum(arr_peso)/len(arr_peso):.1f}')
        
