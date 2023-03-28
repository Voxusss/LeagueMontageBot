from bs4 import BeautifulSoup
import requests
from pathlib import Path
import random
import time


#Rune scrapping Tool for MetaSrc champion pages ----------------------------------------------------------------
def getBestRunes(url):
    """accepts URL of champion page returns array of untranslated rune names"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    best_rune_container = soup.find("div", class_="content-selected _g9pb7k")
    image_tag = best_rune_container.find_all("image")

    result = []
    for html in image_tag: 
        row = html["data-xlink-href"]
        row_segmented = row.split("/")
        rune = row_segmented[-1].replace(".png","")
        result.append(rune)
    
    #format of rune picker = Rune Orders/ primary runes/ secondary runes/ shards
    #swap elements to order list as above
    first_element = result.pop(1)
    second_element = result.pop(5-1)
    result.insert(1, second_element)
    result.insert(5,first_element)

    return result

#misc ------------------------------------------------------------------------------------------------
def allChampNames():
    """scraps the names of all champions and converts them to useable format for creating hyper links
    returns array of names"""
    page = requests.get("https://www.metasrc.com/aram")
    soup = BeautifulSoup(page.content, "html.parser")

    #names used in url have specific formating which is handled here
    result = []
    champion_grid = soup.find_all("div", class_="_9581uw")
    for champion in champion_grid:
        true_name = champion.get_text()
        if true_name == "Wukong": #url uses monkeyking for some fuckin reason
            true_name = "monkeyking"
        sweep_1 = true_name.replace(" ","")
        sweep_2 = sweep_1.replace("'","")
        sweep_3 = sweep_2.replace(".","")
        sweep_3 = sweep_3.lower()
        result.append(sweep_3)
    return result

#ARAM FUNCTIONS ----------------------------------------------------------------------------------------
def getAllChampLinksAram():
    print("getting all aram urls")
    page = requests.get("https://www.metasrc.com/aram")
    soup = BeautifulSoup(page.content, "html.parser")

    result = []
    champion_grid = soup.find_all("a", class_="_95ecnz champion-grid-item _v0k26j _c8xw44")
    for champion in champion_grid:
        link = champion["href"]
        print(link)
        result.append(link)
    return result


def scrapeAllAram(urls):
    """scrapes from list of urls, creates file with build in"""
    
    #create/check directoy to save scrapes to
    path = Path.cwd() / "saves" / "metasrcAram" 
    if path.exists() == False:
        print("Creating folder: saves//metasrcAram")
        path.mkdir()

    for url in urls:
        #champs name from url
        split = url.split("/")
        print(f"writting: {split[-1]}")

        #create file to store scrape in
        file_path = Path.cwd() / "saves" / "metasrcAram" / f"{split[-1]}_metasrc_ARAM.txt"
        
        file = open( file_path,"w")
        runes = getBestRunes(url)
        for rune in runes:
            file.write(rune + "\n")
        file.write(url)
        file.close()
        
        #dely to not spam the site
        time.sleep(random.randrange(0,2))

#5v5 functions ----------------------------------------------------------------------------------------
#this will only pull their default perfered rolls, e.g. kindred gets a jungle build
def getAllChampLinks5v5():
    """returns list of all 5v5 champion page urls"""
    print("getting all 5v5 build urls")
    page = requests.get("https://www.metasrc.com/5v5")
    soup = BeautifulSoup(page.content, "html.parser")

    
    result = []
    champion_grid = soup.find_all("a", class_="_95ecnz champion-grid-item _v0k26j _yq1p7n")
    for champion in champion_grid:
        link = champion["href"]
        print(link)
        result.append(link)
    return result

def scrapeAll5v5(urls):
    """scrapes from list of urls, creates file with build in"""
    
    #create/check directoy to save scrapes to
    path = Path.cwd() / "saves" / "metasrc5v5" 
    if path.exists() == False:
        print("Creating folder: saves//metasrc5v5")
        path.mkdir()
    


    for url in urls:
        #champs name from url
        split = url.split("/")
        print(f"writting: {split[-2]}")

        #create file to store scrape in
        file_path = Path.cwd() / "saves" / "metasrc5v5" / f"{split[-2]}_metasrc_5v5.txt"
        
        file = open( file_path,"w")
        runes = getBestRunes(url)
        for rune in runes:
            file.write(rune + "\n")
        file.write(url)
        file.close()
        
        #dely to not spam the site
        time.sleep(random.randrange(0,2))

#URF Functions---------------------------------------------------------------------------------------

def getAllChampLinksURF():
    """returns list of all URF champion page urls"""
    print("getting all URF build urls")
    page = requests.get("https://www.metasrc.com/urf")
    soup = BeautifulSoup(page.content, "html.parser")

    result = []
    champion_grid = soup.find_all("a", class_="_95ecnz champion-grid-item _v0k26j _qo5b4m")
    for champion in champion_grid:
        link = champion["href"]
        print(link)
        result.append(link)
    return result


def scrapeAllURF(urls):
    """scrapes from list of urls, creates file with build in"""
    
    #create/check directoy to save scrapes to
    path = Path.cwd() / "saves" / "metasrcURF" 
    if path.exists() == False:
        print("Creating folder: saves//metasrcURF")
        path.mkdir()


    for url in urls:
        #champs name from url
        split = url.split("/")
        print(f"writting: {split[-1]}")

        #create file to store scrape in
        file_path = Path.cwd() / "saves" / "metasrcURF" / f"{split[-1]}_metasrc_URF.txt"
        
        file = open( file_path,"w")
        runes = getBestRunes(url)
        for rune in runes:
            file.write(rune + "\n")
        file.write(url)
        file.close()
        
        #dely to not spam the site
        time.sleep(random.randrange(0,2))
