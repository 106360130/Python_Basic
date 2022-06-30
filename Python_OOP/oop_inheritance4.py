class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class B:
    def __init__(self, x, z):
        self.x = x*10
        self.z = z*100

# error
# class C(A, B):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)
#         super(A, self).__init__(x, y)
#         super(B, self).__init__(x, z)
# error

class C(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, y)
        B.__init__(self, x, z)

d = C(1, 2, 3)
print("d.z : {}".format(d.z))