# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


import random
import math

N = int(input())
_list = [random.randint(-100, 101)  for i in range(N)]
X = int(input())
_dict = dict()
dif = math.inf
res = None
for el in _list:
    _dict[el] = abs(X - el)
    if _dict[el] < dif:
        res = el
        dif = _dict[el]    
print(res)
