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

B = ["Jeff", "Leo", "Jakob"]
StrE = "".join("{}".format(B))
print("StrE : {}".format(StrE))

# concatenate to a string and there have a blank between 2 words
a = [1,2,3]
StrF = "".join([" {}".format(str(_)) for _ in a])
print("StrF : {}".format(StrF))
# concatenate to a string and there have a blank between 2 words

# list to str