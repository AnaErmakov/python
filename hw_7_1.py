class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        """Переопределяем метод для вывода на экран в виде матрицы"""
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        """Переопределяем метод сложения для поэлементного сложения значений двух матриц"""
        add_matrix = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                add_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(add_matrix)


val1 = [[31, 22], [37, 43], [51, 86]]
val2 = [[3, 5], [2, 4], [-1, 64]]
m1 = Matrix(val1)
m2 = Matrix(val2)

print(f'Исходная матрица 1:\n{m1}')
print(f'Исходная матрица 2:\n{m2}')
print(f'Результат сложения матриц 1 и 2:\n{m1 + m2}')
