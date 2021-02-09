def name_list(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите имя - ')
surname = input('Введите фамилию - ')
year = input('Введите год рождения - ')
town = input('Введите город - ')
email = input('Введите email - ')
phone = input('Введите номер телефона - ')

print (name_list(name=name,surname=surname, year=year,town=town, email=email, phone=phone))