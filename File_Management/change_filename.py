import os

folder_path = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\File_manage"

file_oldname = os.path.join(folder_path, "00000001.txt")
file_newname_newfile = os.path.join(folder_path, "1.txt")

os.rename(file_oldname, file_newname_newfile)
print("Done!")