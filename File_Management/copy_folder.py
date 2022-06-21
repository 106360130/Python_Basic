import shutil

src=r'C:\Users\RTES\Desktop\Jakob\Python_Basic\File_Management\folder_test'
des=r'C:\Users\RTES\Desktop\Jakob\Python_Basic\File_Management\folder_test2'

shutil.copytree(src, des)

print("Done!")