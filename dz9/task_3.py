class Parallelogram():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        return "Parallelogram area = " + str(self.width * self.length)

first = Parallelogram(7,20)
print(first.get_area())

class Square(Parallelogram):
    def get_area(self):
        return "Width square area = " + str(self.width * self.width) + " and Length square area = " + str(self.length * self.length)


second = Square(10, 14)
print(second.get_area())

#