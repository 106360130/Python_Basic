import os

fileTest = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\test12.txt"

try:
    os.remove(fileTest)

except OSError as e:
    print(e)

else:
    print("File is deleted successfully")