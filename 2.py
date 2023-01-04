class NumberSet:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def getT1(self):
        return self.t1
    def getT2(self):
        return self.t1

num1 = NumberSet(6, 10)
num2 = NumberSet(10, 12)
print(num1.getT1())
print(num2.getT2())