lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

calcLado1 = (lado2 - lado3) < lado1 < lado2 + lado3
calcLado2 = (lado1 - lado3) < lado2 < lado1 + lado3
calcLado3 = (lado1 - lado3) < lado3 < lado1 + lado2

if calcLado1 and calcLado2 and calcLado3:
    print('PODE FORMAR um triângulo!')
    
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('Triângulo equilátero.')
        
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo Isósceles')
        
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Triângulo Escaleno')
else:
    print('NÂO PODE FORMAR um triângulo!')
