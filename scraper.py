import csv
import os
import threading
import time
import webbrowser
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from playsound import playsound

found = False



def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

urls = {
    "Shining": 'https://www.chaoscards.co.uk/shop/pokemon/shining-fates',
    "Voltage": 'https://www.chaoscards.co.uk/shop/pokemon/vivid-voltage',
    "Booster":  'https://www.chaoscards.co.uk/shop/pokemon/booster-boxes-pokemon',
    "ETB": 'https://www.chaoscards.co.uk/shop/pokemon/elite-trainer-boxes-pokemon',
    "Collections": 'https://www.chaoscards.co.uk/shop/pokemon/collection-boxes-pokemon'
}

print ("Il programma controlla:\n")
for k,v in urls.items():
    print(k + "\n")


def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

def startProgram():

    # SHINING FATES
    req = Request(urls["Shining"], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_shining = soup(page_html, "html.parser")
    containers_shining = [page_soup_shining.findAll(
        "li", {"class": "prod-list__element"}), "SHINING FATES"]

    # VIVID VOLTAGE

    req = Request(urls["Voltage"], headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_voltage = soup(page_html, "html.parser")
    containers_voltage = [page_soup_voltage.findAll(
        "li", {"class": "prod-list__element"}), "VIVID VOLTAGE"]

    # BOOSTER BOX

    req = Request(urls["Booster"],
                headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_booster = soup(page_html, "html.parser")
    containers_booster = [page_soup_booster.findAll(
        "li", {"class": "prod-list__element"}), "BOOSTER BOX"]

    # COLLECTION

    req = Request(urls["Collections"],
                headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_collection = soup(page_html, "html.parser")
    containers_collection = [page_soup_collection.findAll(
        "li", {"class": "prod-list__element"}), "COLLECTION"]

    # ETB

    req = Request(urls["ETB"],
                headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_etb = soup(page_html, "html.parser")
    containers_etb = [page_soup_etb.findAll(
        "li", {"class": "prod-list__element"}), "ELITE TRAINER BOX"]

    SudoContainer = [containers_shining, containers_voltage,
                    containers_booster, containers_etb]

    filename = "C:\\Users\\fatto\\OneDrive\\Desktop\\products.csv"
    filenameUpdated = "C:\\Users\\fatto\\OneDrive\\Desktop\\productsUpdated.csv"

    if os.path.exists(filename):
        path = filenameUpdated
    else:
        path = filename

    with open(path, 'w') as csvfile:
        headers = ["Name", "Price", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter="-")
        writer.writeheader()

        for cont in SudoContainer:
            for container in cont[0]:

                if cont[0].index(container) == 0:
                    writer.writerow(
                        {'Name': cont[1], 'Price': "!!", 'Status': "!!"})
                price = container.findAll(
                    "p", {"class": "prod-el__pricing"})[0].text[0:7]
                name = container.findAll(
                    "h6", {"class": "prod-el__title"})[0].span.text
                try:
                    status = container.findAll(
                        "span", {"class": "prod-el__label"})[0].text
                except:
                    status = ""

                writer.writerow(
                    {'Name': name, 'Price': price, 'Status': status})

        with open(filename, 'r') as t1, open(filenameUpdated, 'r') as t2:
            fileOne = t1.readlines()
            fileTwo = t2.readlines()
            print("Controllo Nuova Disponibilità...")
            found = False
            for line in fileTwo:
                if line not in fileOne:
                    found = True
            if found:
                for k, v in urls.items():
                    webbrowser.open(v)
                while True:
                    playsound("C:\\Users\\fatto\\Downloads\\ringtone.mp3")
                    print("C'è roba!!!")
                    time.sleep(1)



    print("Niente di nuovo per ora...")

    os.remove(filename)
    os.rename(filenameUpdated, filename)
  
       
    print("Nuovo controllo in:")
    countdown(60)

set_interval(startProgram,60)
startProgram()



