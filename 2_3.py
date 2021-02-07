month = int(input('введите номер месяца\n'))
#year_dict = {0:'зима', 1:'весна', 2:'лето', 3:'осень', 4:'зима'}
#year = month//3
#print (year_dict[year])
year_list = [[12,1,2], [3,4,5], [6,7,8], [9,10,11]]
for i in  range (len (year_list)) :
    for j in range (len (year_list [i])) :
        if year_list[i][j] == month:
            year = int(i)
            print (year)
            if year == 1:
                print('зима')
            elif year == 2:
                print('весна')
            elif year == 3:
                print('лето')
            elif year == 4:
                print('осень')
        break
    else: print('ошибка')
