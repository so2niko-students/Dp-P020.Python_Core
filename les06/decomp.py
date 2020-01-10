import numpy as np

dict = {1: [[1]]}

def decompose(n):
#Функция разбирает целое число на массив вариантов слагаемых


    try:
        return dict[n]
    except:
        pass
    result = [[n]]
    for i in range(1, n):
        a = n-i
        req_dict = decompose(i)
        for r in req_dict:
            if r[0] <= a:
                result.append([a] + r)
    dict[n] = result

    return result

def findPartMaxProd(n):
#Функция поиска максимального значения произведения слагаемых
    
    list_of_parts = decompose(n)
    max_prod = 0

    list_of_maxprod = []
    for i in list_of_parts:
        part_prod = np.prod(i)
        if part_prod > max_prod:
            list_of_maxprod = [i]
            max_prod = part_prod
        elif part_prod == max_prod:
            list_of_maxprod.append(i)
    list_of_maxprod.append(max_prod)

    return list_of_maxprod 

n = int(input("Введите число: "))
print(findPartMaxProd(n))
