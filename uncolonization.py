# use this file to remove every country that is NOT contained in the provided tag list file

import shutil
from os import listdir, remove

file_to_open = "editMyName.txt"

allowed_tags=[]
with open(file_to_open, "r") as file:
    allowed_tags = file.readlines()
for tag in allowed_tags:
    if "\n" in tag:
        allowed_tags[allowed_tags.index(tag)] = tag.removesuffix("\n")

dirs = listdir("output/provinces")
if "desktop.ini" in dirs:
    dirs.remove("desktop.ini")
for dir in dirs:
    print(f"deleting {dir}")
    remove("output/provinces/"+dir)

dirs = listdir("input/provinces")
if "desktop.ini" in dirs:
    dirs.remove("desktop.ini")
for dir in dirs:
    print(f"checking {dir}")
    with open("input/provinces/"+dir,"r") as file:
        content = ""
        lines = file.readlines()
        for line in lines:
            if line[0].isnumeric():
                if int(line[0:line.find(".")])<1445:
                    content+=line
                else:
                    break
            else:
                content+=line
                
        copyable = True
        for tag in allowed_tags:
            if f"owner = {tag}" in content:
                copyable = False
        if copyable:    
            print(f"copying {dir}")
            shutil.copy2("input/provinces/"+dir, "output/provinces")

dirs = listdir("output/provinces")
if "desktop.ini" in dirs:
    dirs.remove("desktop.ini")
for dir in dirs:
    content = ""
    with open("output/provinces/"+dir,"r") as file:
        lines = file.readlines()
        for line in lines:
            if "owner = " in line or "controller = " in line or "add_core = " in line:
                if line[0].isnumeric():
                    if  int(line[0:line.find(".")])<1445:
                        for tag in allowed_tags:
                            if tag in line:
                                content+=line
            else:
                content+=line
    with open("output/provinces/"+dir,"w") as file:
        print(f"writing {dir}")
        file.write(content)
print("done! check the output folder for results")