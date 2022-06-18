# 直接串接
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_combined = list_1 + list_2
print(list_combined)
# 直接串接

# 對齊合併
list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 7]

list_combined = list(zip(list_1, list_2))
print(list_combined)
print("list_combined[0][0] : {}".format(list_combined[0][0]))
print("list_combined[0][1] : {}".format(list_combined[0][1]))

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c', 'd']

list_combined = list(zip(list_1, list_2))
print(list_combined)
print("list_combined[0][0] : {}".format(list_combined[0][0]))
print("list_combined[0][1] : {}".format(list_combined[0][1]))

# print("list_combined[0][1] : {}".format(list_combined[3][1]))
# 對齊合併

# 直接合併
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_combined = [list_1, list_2]
print(list_combined)
# 直接合併

# len()
len_list_1 = len(list_1)
print(len_list_1)
# len()

# append()
aList = [123, 'xyz', 'zara', 'abc']
aList.append(2009)
print( "Updated List : {}".format(aList))
# append()

# insert()
li = ['a', 'b']
li.insert(0, 'c')
print("li : {}".format(li))
# insert()

# extend()
li = ['a', 'b']
li.extend([2, 'e'])
print("li : {}".format(li))
# extend()