class Car(object):
    def __init__(self, name, colour, volume):
        self.name = name
        self.colour = colour
        self.volume = volume
    @classmethod
    def classmethod1(cls):
        return "Move forward"
    def classmethod2(cls):
        return "Move backward"

ford = Car("Ford", "Red", 5.0)
print(ford.name)
print(ford.classmethod2())

class NewCar(Car):
    def __init__(self, name, colour, volume):
        super().__init__(self, colour, volume)
    @classmethod
    def classmethod3(cls):
        return "Move left"
    def classmethod4(cls):
        return "Move right"

vw = NewCar("VW","black", 3)
print(vw.classmethod2())