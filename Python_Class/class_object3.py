class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("self.x : {}, self.y : {}".format(self.x, self.y))

    def distance(self, targetX, targetY):
        return ((self.x - targetX)**2 + (self.y - targetY)**2)**0.5

    def test(num1, num2):
        print("num1 : {}, num2 : {}".format(num1, num2))


p = Point(3, 4)
p.show()

distance = p.distance(0, 0)
print("distance : {}".format(distance))

p.test(6)