class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
    def getArms(self):
        return self.arms
    def getLegs(self):
        return self.legs

    def spidlimbs(self):
        return ((self.arms * 2) + (self.legs * 2))
spider = Animal(4, 4)
print(spider.getArms())
print(spider.getLegs())
print(spider.spidlimbs())