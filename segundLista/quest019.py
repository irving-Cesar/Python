#  326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = str(input('Insira um número inteiro menor que 1000: '))
tamanho_max = 3;
val_string = []
str_set = ''
arr_tipos = ['centenas', 'dezenas', 'unidades']

if int(num) < 1000 and num.isnumeric() and int(num) != 0:
    
    origin_len =len(num)    
    # inserir zero onde não há número. ex: 12 -> 012; 1 -> 001
    if len(num) < tamanho_max:
        calc = tamanho_max - len(num)
        num = num.zfill(len(num) + calc)
        
    if origin_len == 1:
        if int(num[2]) == 1:
            arr_tipos[num.index(num[2])] = arr_tipos[num.index(num[2])].replace('s', '')
        print(f'{num[2]} {arr_tipos[num.index(num[2])]}')
        
    elif origin_len == 2:
        for i in range(2):
            if int(num[i+1]) == 1:
                arr_tipos[num.index(num[i+1])] = arr_tipos[num.index(num[i+1])].replace('s', '')
            str_set = (f'{num[i+1]} {arr_tipos[num.index(num[i+1])]}')
            val_string.append(str_set)
            num = num.replace(num[num.index(num[i+1])], 'x', 1)
        print(' e '.join(val_string))
        
    elif origin_len == 3:
        for i in range(3):
            if int(num[i]) == 1:
                arr_tipos[num.index(num[i])] = arr_tipos[num.index(num[i])].replace('s', '')
            str_set = (f'{num[i]} {arr_tipos[num.index(num[i])]}')
            val_string.append(str_set)
            num = num.replace(num[num.index(num[i])], 'x', 1)
        str_set = ''
        for x, y in zip(val_string, range(len(val_string))):
            if y < 2:
                if y < 1:
                    str_set += x + ', '
                else:
                    str_set += x
            else:
                str_set += ' e ' + x
        print(str_set)
        
else:
    print('Não é um número ou é maior que 1000 ou igual a 0.')
