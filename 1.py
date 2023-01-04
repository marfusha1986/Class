class NumberSet:
    # it is a new class
    def getT(self):
        return self.t


num1 = NumberSet()
num2 = NumberSet()
num1.t = 6
num2.t = 10

print(num1.getT())
print(num2.getT())