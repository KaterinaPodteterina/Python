from functools import reduce
def sum (arg1,arg2):
    arg1, arg2 = int(arg1), int (arg2)
    return arg1 + arg2

new_list = [0]
num = 0
while num != 'q':
    num_list = input('Введите число или Q для выхода: ').split()
    for i in num_list:
        if i == 'q':
            num = 'q'
            break
        else:
            new_list.append(i)
    print (reduce(sum,new_list))