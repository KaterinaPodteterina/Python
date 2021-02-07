
input_list=list(input('введите список чисел без пробелов\n'))
print (input_list)
for i in range (1, len(input_list), 2) :
    input_list.insert(i - 1, input_list.pop(i))
print(input_list)