# oh soldier prottify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

####################  START  ####################

import os
important = ["project.docx", "records.txt", "accounts.pptx"]
def prettify_folder(path, important, file_type):
    os.chdir(path)
    total_files = os.listdir()
    for files in total_files:
        extension = files.split(".")
        file_extension = extension[1]
        if files in important or file_extension==file_type:
            pass
        else:
            new_name = str(files.title())
            os.rename(files, new_name)

prettify_folder("E:/NITESH/Study/sample", important, "jpg" )