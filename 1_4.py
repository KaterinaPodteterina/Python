input_num = int(input('Введите число\n'))
maximum = input_num % 10
num = input_num

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
        if digit == 9:
            break

    num = num // 10
print(maximum)