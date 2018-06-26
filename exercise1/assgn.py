import os
from string import digits
list_files=os.listdir("C:\\Users\\Lab7\\Desktop\\ithoi\\prank\\prank")
print (list_files)
os.chdir("C:\\Users\\Lab7\\Desktop\\ithoi\\ithoi")
for file in list_files:
    old_name=file
    print (old_name)
    new_name=old_name.lstrip(digits)
    print(new_name)
    os.rename(old_name,new_name)