import shutil
import os

folder_path = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\File_manage"

file_oldname = os.path.join(folder_path, "1.txt")
file_newname_newfile = os.path.join(folder_path, "001.txt")

newFileName = shutil.move(file_oldname, file_newname_newfile)

print ("The renamed file has the name : ", newFileName)