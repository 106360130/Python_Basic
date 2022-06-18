# type()
myInt = 50
print("type(myInt) : {}".format(type(myInt)))

myFloat = 10.50
print("type(myFloat) : {}".format(type(myFloat)))

myString = "My name is Adam"
print("type(myString) : {}".format(type(myString)))
# type()

# split()
str1 = '1 2 3'
print("str1 : {}".format(str1))
str2 = str1.split(' ')
print("str2 : {}".format(str2))
print("str1.split() : {}".format(str1.split()))

str1 = 'hello world 1 2 3 4 5'
print("str1 : {}".format(str1))
str2 = str1.split(' ', 2)
print("str2 : {}".format(str2))
print("str2[0] : {}".format(str2[0]))
print("str2[1] : {}".format(str2[1]))
print("str2[2] : {}".format(str2[2]))
# split()