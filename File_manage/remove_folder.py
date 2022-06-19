import shutil

pathTest = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\test123"

try:
    shutil.rmtree(pathTest)

except OSError as e:
    print(e)
    
else:
    print("The directory is deleted successfully")