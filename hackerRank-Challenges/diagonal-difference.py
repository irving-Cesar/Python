def diagonalDifference(arr):
    soma = 0
    sub = 0
    subA = []
    for x in range(1, len(arr)+1):
        for i, c in zip(arr, range(len(arr[0]))):
            if x == 1:
                soma += i[c]
            else:
                i.reverse()
                soma += i[c]
        
        subA.append(soma)
        soma = 0
        
    calc = subA[0] - subA[1]

    return calc if calc > 0 else calc*-1
