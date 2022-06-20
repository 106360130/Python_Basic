# increase
bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
bad.sort()
print("bad : {}".format(bad))

num = [23, 4, 53, 5 ,35, 6]
num.sort()
print("num : {}".format(num))
# increase

# decrease
bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
bad.sort(reverse=True)
print("bad : {}".format(bad))

num = [23, 4, 53, 5 ,35, 6]
num.sort(reverse=True)
print("num : {}".format(num))
# decrease

# sorted()
bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
bad_sorted = sorted(bad)
print("bad_sorted : {}".format(bad_sorted))

bad_sorted2 = sorted(bad, reverse = True)
print("bad_sorted2 : {}".format(bad_sorted2))
# sorted()