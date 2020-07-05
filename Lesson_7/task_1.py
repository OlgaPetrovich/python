mat_1 = [[8, 9, 6], [5, 4, -2], [6, 2, 4]]
mat_2 = [[4, 12, 5], [8, 6, 4], [5, 8, 2]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        mat_sum = []
        for i in range(len(self.lists)):
            mat_sum.append([])
            for j in range(len(self.lists[0])):
                mat_sum[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, mat_sum))


m_1 = Matrix(mat_1)
m_2 = Matrix(mat_2)

print(f"Матрица 1: \n{m_1} \n")
print(f"Матрица 2: \n{m_2} \n")
print(f"Сумма матриц: \n{m_1 + m_2} \n")