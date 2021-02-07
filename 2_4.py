user_list = input('Введите строку\n').split()
for i, item in enumerate (user_list,1) :
    print (f"{i}. {item[:10]}\n")
