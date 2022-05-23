'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''

num = 500
arr_fibo = []

for i in range(num):
    if i == 0:
        arr_fibo += [0, 1]
    print(arr_fibo[i+1], arr_fibo[i])
    if arr_fibo[i+1] + arr_fibo[i] > num:
        arr_fibo.append(arr_fibo[i+1] + arr_fibo[i])
        break
    else:
        arr_fibo.append(arr_fibo[i+1] + arr_fibo[i])
print(arr_fibo)
