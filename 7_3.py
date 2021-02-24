class Cell:

    def __init__(self, num_in_rows, nums):
        self.num_in_rows = num_in_rows
        self.nums = nums

    def __add__(self, other):
        return self.nums + other.nums

    def __sub__(self, other):
        return f"вычитание невозможно" if self.nums-other.nums<0 else self.nums-other.nums

    def __mul__(self, other):
        return self.nums * other.nums

    def __truediv__(self, other):
        return self.nums//other.nums

    def make_order (self):
        return '\n'.join(['*' * self.num_in_rows for _ in range(self.nums // self.num_in_rows)]) + '\n' + '*' * (self.nums % self.num_in_rows)

cell_1 = Cell(8,10)
cell_2 = Cell(1,15)

print(cell_1 + cell_2)
print(cell_1.make_order())
