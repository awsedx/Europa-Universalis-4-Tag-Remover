# file_to_write_to = "only_Europe_Tags.txt"
# allowed_regions = ["Western Europe", "Eastern Europe", "Egypt", "Mashriq", "Anatolia", "Caucasia", "Maghreb"]
# file_to_write_to = "only_India_Tags.txt"
# allowed_regions = ["Tibet", "Central Asia", "Mongolia", "Persia / Persia", "Khorasan", "India", "China", "East Indies"]
# file_to_write_to = "ck3Convert_tags.txt"
# allowed_regions = ["North America", "Amazonia", "Andes", "Central America", "Southern Africa", "Oceania", "East Siberia"]


file_to_write_to = "editMyName.txt" # <-- here goes the name of the file that shall be created/edited
allowed_regions = [] # <-- here go the allowed regions and subcontinents


if allowed_regions == []:
    print("The list of allowed Regions is empty, and no Tags will be written into the file. Are you sure this is what you want?")
tags=[]
with open("list_of_all_tags.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        if any(region in line for region in allowed_regions):
            i = 0
            while i<len(line)-2:
                if line[i].isupper() and line[i+1].isupper() and line[i+2].isupper():
                    tags.append(line[i:i+3])
                    # break
                i+=1
with open(file_to_write_to,"w") as file:
    content = ""
    for tag in tags:
        content+=tag
        content+="\n"
        print(f"adding {tag}")
    content = content[0:-1]
    file.write(content)
    print("file written successfully!")
