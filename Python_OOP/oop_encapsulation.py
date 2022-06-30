class Demo2:
    __x = 0
    num = 0

    def __init__(self, i):
        self.__i = i
        Demo2.__x += 1

        self.num2 = 2

    def show_x_and_i(self):
        print("self.__x : {}".format(self.__x))
        print("self.__i : {}".format(self.__i))

    def get_x(cls):
        return cls.__x

    def get_i(self):
        return self.__i



d = Demo2(1)

# print("d.__x : {}".format(d.__x))
# print("d.__i : {}".format(d.__i))

print("d.num : {}".format(d.num))
print("d.num2 : {}".format(d.num2))

d.show_x_and_i()

x = d.get_x()
i = d.get_i()

print("x : {}, i : {}".format(x, i))
