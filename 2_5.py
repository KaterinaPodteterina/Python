new_list = [8, 6, 6, 5, 4, 4, 2]
number = int(input('введите целое число\n'))
j = 0
for i in new_list:
    if number <= i:
        j = j + 1
new_list.insert(j, float(number))
print(new_list)