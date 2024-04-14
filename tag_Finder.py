# The EU4-Tag-Remover, from https://github.com/awsedx/Europa-Universalis-4-Tag-Remover

from time import time


file_to_write_to = (
    "editMyName.txt"
)
allowed_regions = [
    "Western Europe",
    "Eastern Europe",
    "Egypt",
    "Mashriq",
    "Anatolia",
    "Caucasia",
    "Maghreb",
]


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


print("done! check your specidief file for results")

# //////////////////////// performance metrics ///////////////////////////////////
print("finished in " + str(time() - start_all) + " seconds")