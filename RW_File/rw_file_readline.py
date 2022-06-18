file = open("test.txt", "r")
for line in file.readlines():
    line = line.strip()
    print("line : {}".format(line))