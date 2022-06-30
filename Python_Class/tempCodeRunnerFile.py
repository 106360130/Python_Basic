from time import sleep


class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    
    def open(self):
        self.file = open(self.name, mode = "r", encoding = "utf-8")

    def read(self):
        return self.file.read()

f1 = File("data1.txt")
f1.open()
data_f1 = f1.read()
print("data_f1 : {}".format(data_f1))

f2 = File("data2.txt")
f2.open()
data_f2 = f2.read()
print("data_f2 : {}".format(data_f2))