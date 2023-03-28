import createThumbnail
import runes
import os
import random

folder_path = "splash"
def getChampSet():
    unique_names = set()
    for filename in os.listdir(folder_path):
        name = filename.split("_")[0]
        unique_names.add(name)

    return unique_names
def getChamp():
    champSet = getChampSet()
    champList = list(champSet)
    champ = random.choice(champList)
    return champ

champ = getChamp()
runes = runes.getBestRunes("https://www.metasrc.com/5v5/champion/" + champ.lower())[2:-3]
print(runes)
runeList = []
for rune in runes:
    for filename in os.listdir("runes"):
        if(rune in filename.lower()):
            runeList.append(filename)
print(runeList)
    
createThumbnail.createThumbnail(champ)