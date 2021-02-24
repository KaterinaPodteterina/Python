set_1 = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
set_2 = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        rez = []
        for i in range(len(self.lists)):
            rez.append([])
            for j in range(len(self.lists[0])):
                rez[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, rez))

matrix_1 = Matrix(set_1)
matrix_2 = Matrix(set_2)
print(f'Матрица 1\n{matrix_1}\n')
print(f'Матрица 2\n{matrix_2}\n')
print(f'Результирующая матрица\n{matrix_1+matrix_2}\n')