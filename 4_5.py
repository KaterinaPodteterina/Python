from functools import reduce

def mult (el_1,el_2):
    return el_1*el_2

new_list = [el for el in range (100,1001,2)]
print(reduce(mult, new_list))