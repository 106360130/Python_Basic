class Demo:
    def __init__(self):
        print("Demo")

    def show_good(self):
        print("So goooood~")

class Demo2(Demo):
    def __init__(self):
        super().__init__()
        print("Demo2")

    def show_peace(self):
        print("Peaaaace~")

    def show_good(self):
        super().show_good()
        print("So So good!")

d = Demo2()

print("\nd.show_peace() : ")
d.show_peace()

print("\nd.show_good() : ")
d.show_good()