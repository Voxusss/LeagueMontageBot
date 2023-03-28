import os
import random
import solidBorder
import mastery
import cv2
folder_path = "splash"

def getSplash(champName):
    splashes = set()
    for filename in os.listdir(folder_path):
        if(champName in filename):
            splashes.add(filename)
    return random.choice(list(splashes))

def getIcon(champName):
    icons = set()
    for filename in os.listdir("tiles"):
        if(champName in filename):
            icons.add(filename)
    return random.choice(list(icons))
def createThumbnail(champ):
    imageborder = solidBorder.add_solid_border(getSplash(champ))
    imageicon = mastery.add_transparent_image(imageborder, "tiles/" + getIcon(champ), 930, 55, True)
    imagemastery = mastery.add_transparent_image(imageicon, "masteryseven.png", 900, 20)
    cv2.imwrite("output.png", imagemastery)
    print("Thumbnail created! Saved as output.png")