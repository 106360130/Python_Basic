class A2:
    def __init__(self):
        self.a = "A2"

    def print_a(self):
        print("self.a : {}".format(self.a))

    def print_cool(self):
        print("Cooooooool~")

class B2:
    def __init__(self):
        self.b = "B2"

    def print_b(self):
        print("self.b : {}".format(self.b))

class C2(A2, B2):
    def __init__(self):
        super().__init__()
        super(A2, self).__init__()
        super(B2, self).__init__()

c = C2()
c.print_a()
c.print_b()
c.print_cool()