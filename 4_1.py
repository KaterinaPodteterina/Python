from sys import argv

def payment ():
    time,rate,bonus = map(float, argv[1:])
    rez = time * rate + bonus
    return rez

payment()
print(f"зарплата сотрудника = {rez}")