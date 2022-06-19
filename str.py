# list to str
A = ["a", "b", "c"]
StrA = "".join(A)
print("StrA : {}".format(StrA))


a = [1,2,3]
StrB = "".join([str(_) for _ in a])
print("StrB : {}".format(StrB))

a = [1,2,3]
StrC = "".join(map(str, a))
print("StrC : {}".format(StrC))

B = ["Jeff", "Leo", "Jakob"]
StrD = "".join(B)
print("StrD : {}".format(StrD))
# list to str