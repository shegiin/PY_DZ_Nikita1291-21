L = [3, 6, 7, 4, -5, 4, 3, -1]
print('1. Сумма элементов: ', sum(L))
if sum(L) > 2:
    print(' Длина строки: ', len(L))
diff = abs(max(L)-min(L))
print('2. ', diff)
if diff > 10:
    print(sorted(L))
else:
    print('Разность меньше или равна 10')
