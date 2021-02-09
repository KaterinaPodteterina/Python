def my_func(a, b, c):
    my_list = [a, b, c]
    return sum(sorted(my_list)[1:])

print (my_func(int(input ('введите первое число\n')), int(input ('введите второе число\n')),\
    int(input ('введите третье число\n'))))