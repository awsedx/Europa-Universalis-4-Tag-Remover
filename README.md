## Welcome to the EU4 Tag Remover!

### What is this?
The EU4 Tag Remover is a collection of Python scripts, with which you can generate a list of tags based on their capital Super Region (Subcontinent), Region, or province, and then generate history files that either uncolonize (make unowned at game start) all provinces owned by the specified tags in 1444, or uncolonize every province **except** those owned by the tags specified in the list.

### Why?
To improve performance. If you're playing a non-colonial game in europe, you probably don't really care about what those natives in the new world or them there sub saharan Africans are up to, but your Computer has to spend ressources on them all the same. Culling these countries drastically increases performance, especially on speed 5.

### Prerequisites
First off, you need Python. Here's a link to the official Website https://www.python.org/downloads/.

Then you need a file which contains all Tags and their capital locations. One is already included in the file list_of_all_tags.txt, based on the wiki at https://eu4.paradoxwikis.com/Countries. In case of future game updates, you should update the list from there.

The scripts need a copy of all province files from the history folder of your game. Copy them from yourInstallDirectory\Europa Universalis IV\history\provinces into the sub-folder input\provinces of this directory. If playing a megacampaign or other mod, copy your history files from there to input\provinces instead.

### How do I use this?
To get started, download a zipped archive by clicking the green "code" button above, and select "Download Zip"; create a new folder, and extract all contents to there. Copy your game's province history files to input/provinces, or create the folders in the main directory (the one where all the python files are stored) if they dont exist. Also check if the folders output/provinces exist, if they dont create them.

Open the file "all_in_one.py" in a text editor of your choice (right-click -> "open with" -> text editor). At the top, edit the variables to your liking. Explanations and examples of their meaning can be found commented out just below. Then, close your text editor, and run "all_in_one.py", either with a double click, or through the console. The script will then generate a file containing all Tags that match any of the provided Regions in allowed_regions, under the name you gave it. (Fun fact: you can put any string literal in allowed_regions, and the script will check for its existance in every line of the provided list_of_all_tags.txt file, so for example if you always wanted to get a list of all tags of formable nations, this is your dream come true). Afterwards, the script will generate, based off of the province files in the input folder, all necesarry province files to make the undesired countries disappear at game start. These can be found in the output folder, from where you may copy them to your mod. And thats it, youre done! Enjoy the faster game experience! (I do highly recommend also editing the provinces.bmp file in the map directory, and surrounding regions of the world you dont want the remaining countries to recolonize with wasteland. I recommend against removing the now empty provinces from the map, as when countries do remain in these provinces, for example when spawned in via event after game start, diplomats can get stuck there and become unusable for the remainder of the campaign)

### I'm inexperienced with EU4 modding, what do I do with my new province history files?
Start the EU4 launcher, click on "all installed mods" on the left, and then on "upload mod" near the top right. Then, in the pop-up, click "create a mod". Enter a name for your mod, and provide a name for the folder in which your mod shall be saved. You can enter the current version of EU4 into the version text box, but putting nonsense there also does no harm. Tick at least one checkbox for a tag, and then click the green "create mod" button at the bottom right. You should then see your new mod pop up in the all installed mods section of the launcher. When hovering over it, 3 dots will appear on the right. Clicking them allows you to instantly navigate to the folder containing your mod.

In there, create a folder called history, and then inside of there another folder called provinces (When modding any paradox game, youre usually replacing existing files or adding onto them with new content. The game stores its setup at game start in the folder "history", and as we're editing the starting setup, we'll be overriding part of it). Copy all files from the folder output\provinces to the provinces folder of your new mod. Reload the mod in the launcher (or close and restart the launcher), add your mod to a play set, and start up the game. You're done!

### Extra Features
The scripts tag-finder and tag-remover allow you to generate the tag-list-file and generate province history files from such a file independantly of one another. This can be useful if you want to manually add or remove tags from the list. For example, when playing in europe, you may want to have levantine countries present to form the perifferie. However, even though Qara Quyunlu covers most of Mesopotamia, because it's capital is located in the persia region, this would decolonize it's region of Mesopotamia, leaving a rather jarring gap. To fix this, one may generate the tag list file, manually add QAR, and then run the second script to generate new province history files, this time including Qara Quyunlu.

### May I Modify, or Redistribute this elsewhere?
Feel free, but please give credit in the form of a link to this github page. Thanks!
