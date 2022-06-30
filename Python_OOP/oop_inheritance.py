class Demo:
    def __init__(self):
        print("Demo")

class Demo2(Demo):
    def __init__(self):
        print("Demo2\n")

d = Demo2()

print("isinstance(d, Demo) : {}".format(isinstance(d, Demo)))
print("isinstance(d, Demo2) : {}\n".format(isinstance(d, Demo2)))

print("issubclass(Demo2, Demo) : {}".format(issubclass(Demo2, Demo)))
print("issubclass(Demo, Demo2) : {}".format(issubclass(Demo, Demo2)))


