import random

print("random.randrange() : ")
for i in range(3) :
    print(random.randrange(10, 51), end = '   ')

print("\n\nrandom.random() : ")
for i in range(3) :
    print(random.random(), end = '   ')

print("\n\nrandom.uniform() : ")
for i in range(3) :
    print(random.uniform(60, 95), end = '   ')