class Duck:
    def name(self):
        print("Duck")

    def walk(self):
        print("+++++")
    
    def swim(self):
        print(")))(((")

    def sound(self):
        print("guagua")

class Unknown:
    def name(self):
        print("Unknown")

    def walk(self):
        print("*****")
    
    def swim(self):
        print("((()))")

    def sound(self):
        print("gegege")

d = [Duck(), Unknown()]

for i in d :
    i.name()
    i.walk()
    i.swim()
    i.sound()
    print()
