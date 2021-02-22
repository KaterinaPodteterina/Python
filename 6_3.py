class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}

class Position (Worker):
    def full_name(self):
        return f"{self.name} {self.surname}"

    def total_salary(self):
        return f"{sum(self._income.values())}"

manager = Position("Mister", 'X', "jester", 10, 20)
print(manager.full_name())
print(manager.position)
print(manager.total_salary())