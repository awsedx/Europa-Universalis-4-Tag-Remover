import shutil
from os import listdir, remove
from time import time


file_to_write_to = ("editMyName.txt")  # <-- this will be the name of your file containing all tags within the specified regions
allowed_regions = []  # <-- here go the allowed regions and subcontinents, who'se tags you would like to filter for
reverse_removal = False  # <--- set to False to remove all counries within the specified regions, set to True to remove every country EXCEPT those in the specified regions
enable_copying = False  # if you want the output files automatically copied to another directory, like a mod, set this to True
destination = ""  # add the path to copy the files to here. Dont forget a trailing "/" at the end
overwrite = False  # if automatic copying is enabled, this will delete preexisting files in your specified folder. WARNING: if you specify the wrong folder, ALL FILES WITHIN WILL BE DELETED!

# Here are some examples on this might look
# file_to_write_to = "only_Europe_Tags.txt"
# allowed_regions = [
#     "Western Europe",
#     "Eastern Europe",
#     "Egypt",
#     "Mashriq",
#     "Anatolia",
#     "Caucasia",
#     "Maghreb",
# ]
# reverse_removal = True  # (because we want to delete all tags EXCEPT the european ones)
# enable_copying = True
# destination = "c:/Users/USERNAME/Documents/Paradox Interactive/Europa Universalis IV/mod/test/history/provinces/"
# overwrite = True


# file_to_write_to = "only_India_Tags.txt"
# allowed_regions = [
#     "Tibet",
#     "Central Asia",
#     "Mongolia",
#     "Persia / Persia",
#     "Khorasan",
#     "India",
#     "China",
#     "East Indies",
# ]
# reverse_removal = True
# enable_copying = False
# destination = ""
# overwrite = False

# file_to_write_to = "no_Natives.txt"
# allowed_regions = ["North America", "Amazonia", "Andes", "Central America", "Oceania"]
# reverse_removal = False  # (because we want to explicitly remove the Natives, while leaving the rest of the world as is)
# enable_copying = True
# destination = "c:/Users/USERNAME/Documents/Paradox Interactive/Europa Universalis IV/mod/test/history/provinces/"
# overwrite = True




# /////////////////////// the remainder of the file is code /////////////////////////////




start_all = time()
# ///////////////// gather all allowed tags ///////////////
start_tag_gathering = time()
if allowed_regions == []:
    print(
        "The list of allowed Regions is empty, and no Tags will be written into the file. Are you sure this is what you want?"
    )
tags = []
with open("list_of_all_tags.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if any(region in line for region in allowed_regions):
            i = 0
            while i < len(line) - 2:
                if (
                    line[i].isupper()
                    and line[i + 1].isupper()
                    and line[i + 2].isupper()
                ):
                    tags.append(line[i : i + 3])
                    break
                i += 1
with open(file_to_write_to, "w") as file:
    content = ""
    for tag in tags:
        content += tag
        content += "\n"
        print(f"adding {tag}")
    content = content[0:-1]
    file.write(content)
    print("list of tags file written successfully!")
duration_tag_gethering = time() - start_tag_gathering
# ///////////////////////////////////////////////////////


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
    if destination == "":
        "no destination entered. files will not be copied or deleted."
    else:
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
print("tag gathering took " + str(duration_tag_gethering) + " seconds")
print("deletion took " + str(duration_deletion) + " seconds")
print("checking and writing took " + str(duration_checking) + " seconds")
print("copying took " + str(duration_copying) + " seconds")
# ////////////////////////////////////////////////////////////////////////////////
