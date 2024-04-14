# The EU4-Tag-Remover, from https://github.com/awsedx/Europa-Universalis-4-Tag-Remover

import shutil
from os import listdir, remove
from time import time


file_to_open = "editMyName.txt"
reverse_removal = True
enable_copying = False
destination = ""
overwrite = False


start_all = time()
tags=[]
with open(file_to_open, "r") as file:
    tags = file.readlines()
for tag in tags:
    if "\n" in tag:
        tags[tags.index(tag)] = tag.removesuffix("\n")

# ///////////////// delete existing files in output ///////////////
start_deletion = time()
dirs = listdir("output/provinces")
if "desktop.ini" in dirs:
    dirs.remove("desktop.ini")
for dir in dirs:
    print(f"deleting {dir} in output")
    remove("output/provinces/" + dir)
duration_deletion = time() - start_deletion
# /////////////////////////////////////////////////////////////////


# /////////////////// check all files in input whether the province is owned by an allowed tag, if so: do/do not copy the file to output, with all references to ownership removed ////////////////////
start_checking = time()
dirs = listdir("input/provinces")
if "desktop.ini" in dirs:
    dirs.remove("desktop.ini")
for dir in dirs:
    print(f"checking {dir} in input")
    with open("input/provinces/" + dir, "r") as file:
        check_content = ""
        write_content = ""
        lines = file.readlines()
        for line in lines:
            if not (
                "owner = " in line or "controller = " in line or "add_core = " in line
            ):
                write_content += line
            if line[0].isnumeric():
                if int(line[0 : line.find(".")]) < 1445:
                    check_content += line  # We dont want to let provinces which in 1444 are not owned by an allowed tag but later become owned by one to pass the filter. Thus, dates >1444 are ignored for the check
                    line_tag = ""
                    i = 0
                    while i < len(line) - 2:
                        if (
                            line[i].isupper()
                            and line[i + 1].isupper()
                            and line[i + 2].isupper()
                        ):
                            line_tag = line[i : i + 3]
                            break
                        i += 1
                    if line_tag != "":
                        if ((not reverse_removal) and (not (line_tag in tags))) or (
                            reverse_removal and (line_tag in tags)
                        ):
                            write_content += line  # for some files the actual ownership in 1444 is declared in pre 1444 history, which overrides "owner = TAG"
                else:
                    break
            else:
                if (
                    "owner = " in line
                    or "controller = " in line
                    or "add_core = " in line
                ):
                    check_content += line

        to_uncolonize = reverse_removal
        for tag in tags:
            if f"owner = {tag}" in check_content:
                to_uncolonize = (
                    not reverse_removal
                )  # as declared in the beginning, provinces owned by the given tags are/are not made unowned

        if to_uncolonize:
            print(f"copying {dir}")
            with open("output/provinces/" + dir, "w") as file:
                file.write(write_content)
        # if "4288" in dir:
        #     debug_log+=f"content: {write_content} \n to_uncolonize: {str(to_uncolonize)}"
duration_checking = time() - start_checking
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////// deleting from and copying output files to specified folder //////////////////////////////////////////////
start_copying = time()
if enable_copying:
    if overwrite:
        dirs = listdir(destination)
        if "desktop.ini" in dirs:
            dirs.remove("desktop.ini")
        for dir in dirs:
            print(f"deleting {dir} in " + destination)
            remove(destination + dir)
    dirs = listdir("output/provinces/")
    for dir in dirs:
        print(f"copying {dir} to { destination}")
        shutil.copy2("output/provinces/" + dir, destination)
duration_copying = time() - start_copying
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("done! check the output folder for results")

# //////////////////////// performance metrics ///////////////////////////////////
print("finished in " + str(time() - start_all) + " seconds")
print("deletion took " + str(duration_deletion) + " seconds")
print("checking and writing took " + str(duration_checking) + " seconds")
print("copying took " + str(duration_copying) + " seconds")
# ////////////////////////////////////////////////////////////////////////////////
