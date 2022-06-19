import shutil
import os

path_source = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\File_manage"
path_destination = r"C:\Users\RTES\Desktop\Jakob\Python_Basic\File_RW"

file_oldname = os.path.join(path_source, "1.txt")
file_newname_newfile = os.path.join(path_destination, "001.txt")

newFileName = shutil.move(file_oldname, file_newname_newfile)

print ("The renamed file has the name : ", newFileName)