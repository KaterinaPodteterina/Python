from random import randint
new_list = [randint(1,25) for i in range (20)]
rez_list = [num for num in new_list if new_list.count(num)==1]
print (f"исходный список\n {new_list}")
print (f"результирующий список\n {rez_list}")