class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os

    def play(self):
        print(f'{self.brand} original soundtrack')

sashaphone = Smartphone('Xiaomi', 'x10t', 'android')
sashaphone.play()
print(sashaphone.brand, sashaphone.model, sashaphone.os)