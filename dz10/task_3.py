class CheckNumber100(Exception):
    def __init__(self, text):
        self.text = text

num = input("Input integer: ")

try:
    num = int(num)
    if num > 100:
        raise CheckNumber100("NO NO NO, only 100 or less")
except ValueError:
    print("Error type of value!")
except CheckNumber100 as er:
    print(er)
else:
    print(num)