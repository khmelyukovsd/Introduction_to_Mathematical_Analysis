# Даны три множества a,b и с. Необходимо выполнить все изученные виды бинарных операций над всеми комбинациями множеств.
# *Выполнить задание на языке Python

a = set('12345')
b = set('651861521')
c = set('23')

print('Объединение множеств А и В:', a.union(b))
print('Пересечение множеств А и В:', a.intersection(b))
print('Разность множеств А и В:', a.difference(b))
print('Симметрическая разность множеств А и В:', a.symmetric_difference(b))
print()
print('Объединение множеств А и C:', a.union(c))
print('Пересечение множеств А и C:', a.intersection(c))
print('Разность множеств А и C:', a.difference(c))
print('Симметрическая разность множеств А и C:', a.symmetric_difference(c))
print()
print('Объединение множеств B и C:', b.union(c))
print('Пересечение множеств B и C:', b.intersection(c))
print('Разность множеств B и C:', b.difference(c))
print('Симметрическая разность множеств B и C:', b.symmetric_difference(c))