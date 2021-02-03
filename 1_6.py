a = 0
b = 0
count = 0
a = int(input('введите результат первого дня '))
b = int(input('введите конечный результат '))
while a < b:
    count = count + 1
    a = a * 1.1
print (count)