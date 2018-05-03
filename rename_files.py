import os
def rename_files():
    file_list= os.listdir(r"C:\Users\Sayeef\Downloads\prank")
    print (file_list)
    for file_name in file_list:
        os.rename (file_name, file_name.translate (None, "0123456789"))
rename_files()
