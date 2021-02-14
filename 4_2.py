new_list = input ("введите набор целых чисел через пробел\n").split()
#rez_list = []
#for i in range(1,len(new_list)):
#    if new_list[i] > new_list[i-1]:
#        rez_list.append(new_list[i])
rez_list = [new_list[i] for i in range (1, len(new_list)) if new_list[i] > new_list[i-1]]

print (rez_list)