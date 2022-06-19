# Reference
# https://www.delftstack.com/zh-tw/howto/python/rename-a-file-in-python/
# http://swaywang.blogspot.com/2013/01/pythonosrename.html
# 

import shutil
import os

def name_change(name_old, name_baseline):

    name_old = name_old.replace("_PD", "")

    str_temp = ""
    len_name_old = len(name_old)
    len_name_baseline = len(name_baseline)
    if len_name_old < len_name_baseline :
        for i in range(len_name_baseline - len_name_old) :
            str_temp = str_temp + "0"

    name_new = str_temp + name_old

    return name_new

# change filename to correct format
folder_path = "C:/Users/RTES/Desktop/Jakob/Python_Basic/File_manage/"
print("folder_path : {}".format(folder_path))


# correct format of filename : 00000945.txt
filename_baseline = "00000945.txt"
for filename in os.listdir(folder_path):
    # print("filename : {}".format(filename))
    if 'txt' in filename:
        # print("filename : {}".format(filename))
        filename_new = name_change(filename, filename_baseline)
        # print("{}".format(filename_new))

        file_oldname = os.path.join(folder_path, filename)
        file_newname = os.path.join(folder_path, filename_new)
        os.rename(file_oldname, file_newname)

print("done!\n")