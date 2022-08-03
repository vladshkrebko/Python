# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

sp1 = [1, 5, 2, 3, 4, 6, 1, 7]
sp2 = [1, 5, 2, 3, 4, 1, 7]

def max_num(sp):
    maxnum = min(sp)
    while maxnum + 1 in sp:
        maxnum += 1
    return maxnum

def result(sp):
    return [min(sp), max_num(sp)]
    
print(result(sp1))
print(result(sp2))