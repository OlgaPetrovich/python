class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f"Сумма количества клеток = {self.num + other.num}"

    def __sub__(self, other):
        sub = self.num - other.num
        return f"Разность количества клеток = {abs(sub)}"

    def __mul__(self, other):
        return f"Произведение количества клеток = {self.num * other.num}"

    def __truediv__(self, other):
        return f"Частное количества клеток = {round(self.num / other.num)}"

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range (self.num //rows)]) + '\n' + '*' * (self.num % rows)


cell_1 = Cell(11)
cell_2 = Cell(18)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(f"Первые клетки: \n{cell_1.make_order(5)} \n")

print(f"Вторые клетки: \n{cell_2.make_order(5)}")