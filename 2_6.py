goods = []
goods_analit = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analyt_value = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
n = 0
while True:
    if input('Для выхода Q, для продолжения Enter: ').upper() == 'Q':
        break
    n += 1
    for f in goods_analit.keys():
        prop = input(f'Введите значение свойства {f} - ')
        if (f == 'цена' or f == 'количество'):
            goods_analit[f] = int(prop)
        else :
            goods_analit[f] = prop
        analyt_value[f].append(goods_analit[f])
    goods.append((n, goods_analit.copy()))
    print(f"\nСтруктура товаров\n{goods}")