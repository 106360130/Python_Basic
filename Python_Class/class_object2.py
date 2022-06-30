class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last

name1 = FullName("Jeff", "Hunag")
print("name1.first : {}, name1.last : {}".format(name1.first, name1.last))

name2 = FullName("Leo", "Chen")
print("name2.first : {}, name2.last : {}".format(name2.first, name2.last))