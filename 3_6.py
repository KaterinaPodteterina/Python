def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else ''

input_string = input('Введите слова через пробел\n').split()
for i in input_string:
    res = int_func(i)
    print(int_func(i), end=' ')