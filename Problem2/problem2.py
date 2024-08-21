class Calc:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self

    def subtract(self, value):
        self.value -= value
        return self

    def out(self):
        return self.value

calculator = Calc(0)
result = calculator.add(4).add(5).subtract(3).out()
print(result)
