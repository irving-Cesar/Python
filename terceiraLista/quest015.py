'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

num = int(input('Insira um número: '))

result = []
for i in range(num):
  if i == 0:
    result += [1, 1]
  if (result[i+1] + result[i]) > num:
    break
  else:
    result.append(result[i+1] + result[i])

str_ints = [str(int) for int in result]
str_ints = ', '.join(str_ints)
print(f'{str_ints} -- {num}')

