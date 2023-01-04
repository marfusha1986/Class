class MyName():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

playing = MyName(6, 12)
print(playing.getX())
print(playing.getY())