import numpy as np

class MyMatrixError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f"Неможливо здійснити операцію: {self.message}"

class Matrix:
    def __init__(self, lst):
        self.lst = lst
        self.A = np.array(lst)

    def sum(self, col):
        if len(self.A) < len(col.A):
            delta = len(col.A) - len(self.A)
            list = []
            for i in range(len(self.A[0])):
                list.append(0)
            for i in range(delta):
                self.lst.append(list)
            self.A = np.array(self.lst)
        if len(self.A) > len(col.A):
            delta = len(self.A) - len(col.A)
            list = []
            for i in range(len(col.A[0])):
                list.append(0)
            for i in range(delta):
                col.lst.append(list)
            col.A = np.array(col.lst)
        if len(self.A[0]) < len(col.A[0]):
            delta = len(col.A[0]) - len(self.A[0])
            for j in range(delta):
                for i in self.lst:
                    i.append(0)
            self.A = np.array(self.lst)
        if len(self.A[0]) > len(col.A[0]):
            delta = len(self.A[0]) - len(col.A[0])
            for j in range(delta):
                for i in col.lst:
                    i.append(0)
            col.A = np.array(col.lst)
        D = self.A + col.A
        return D

    def dif(self, col):
        if len(self.A) < len(col.A):
            delta = len(col.A) - len(self.A)
            list = []
            for i in range(len(self.A[0])):
                list.append(0)
            for i in range(delta):
                self.lst.append(list)
            self.A = np.array(self.lst)
        if len(self.A) > len(col.A):
            delta = len(self.A) - len(col.A)
            list = []
            for i in range(len(col.A[0])):
                list.append(0)
            for i in range(delta):
                col.lst.append(list)
            col.A = np.array(B.lst)
        if len(self.A[0]) < len(col.A[0]):
            delta = len(col.A[0]) - len(self.A[0])
            for j in range(delta):
                for i in self.lst:
                    i.append(0)
            self.A = np.array(self.lst)
        if len(self.A[0]) > len(col.A[0]):
            delta = len(self.A[0]) - len(col.A[0])
            for j in range(delta):
                for i in col.lst:
                    i.append(0)
            col.A = np.array(B.lst)
        D = self.A - col.A
        return D

    def mult_number(self, num):
        return self.A * num

    def mult_matrix(self, col):
        try:
            if len(self.A[0]) == len(col.A):
                D = self.A.dot(col.A)
                return D
            else:
                raise MyMatrixError("Кількість стовпчиків однієї матриці не дорівнює кількості рядків іншої матриці")
        except Exception as ex:
            return ex

    def transposition(self):
        return self.A.transpose()


matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

matrix_3 = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0]]

matrix_1 = Matrix(matrix_1)
matrix_2 = Matrix(matrix_2)
matrix_3 = Matrix(matrix_3)

print("Результат додавання матриць:\n", matrix_1.sum(matrix_2))
print("Результат віднімання матриць:\n", matrix_2.dif(matrix_1))
print("Результат множення матриці на число:\n", matrix_1.mult_number(5))
print("Результат множення матриці на матрицю:\n", matrix_1.mult_matrix(matrix_2))
print("Результат транспонування матриці:\n", matrix_1.transposition())
print("Результат додавання матриць після приведення їх у відповідність до операції:\n", matrix_1.sum(matrix_3))
print("Результат віднімання матриць після приведення їх у відповідність до операції:\n", matrix_1.dif(matrix_3))
print("Обробка виключної ситуації для множення\n", matrix_1.mult_matrix(matrix_3))

