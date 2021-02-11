import csv
import os
import threading
import time
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup
from playsound import playsound


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def countdown(t=30):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)


def startProgram():
    # SHINING FATES
    req = Request('https://www.chaoscards.co.uk/shop/pokemon/shining-fates', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_shining = soup(page_html, "html.parser")
    containers_shining = [page_soup_shining.findAll("li", {"class": "prod-list__element"}), "SHINING FATES"]

    # VIVID VOLTAGE

    req = Request('https://www.chaoscards.co.uk/shop/pokemon/vivid-voltage', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_voltage = soup(page_html, "html.parser")
    containers_voltage = [page_soup_voltage.findAll("li", {"class": "prod-list__element"}), "VIVID VOLTAGE"]

    # BOOSTER BOX

    req = Request('https://www.chaoscards.co.uk/shop/pokemon/booster-boxes-pokemon',
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_booster = soup(page_html, "html.parser")
    containers_booster = [page_soup_booster.findAll("li", {"class": "prod-list__element"}), "BOOSTER BOX"]

    # COLLECTION

    req = Request('https://www.chaoscards.co.uk/shop/pokemon/collection-boxes-pokemon',
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_collection = soup(page_html, "html.parser")
    containers_collection = [page_soup_collection.findAll("li", {"class": "prod-list__element"}), "COLLECTION"]

    # ETB

    req = Request('https://www.chaoscards.co.uk/shop/pokemon/elite-trainer-boxes-pokemon',
                  headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    page_html = webpage.read()
    webpage.close()
    page_soup_etb = soup(page_html, "html.parser")
    containers_etb = [page_soup_etb.findAll("li", {"class": "prod-list__element"}), "ELITE TRAINER BOX"]

    SudoContainer = [containers_shining, containers_voltage, containers_booster, containers_etb]

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
                    writer.writerow({'Name': cont[1], 'Price': "!!", 'Status': "!!"})
                price = container.findAll("p", {"class": "prod-el__pricing"})[0].text[0:7]
                name = container.findAll("h6", {"class": "prod-el__title"})[0].span.text
                try:
                    status = container.findAll("span", {"class": "prod-el__label"})[0].text
                except:
                    status = ""

                writer.writerow({'Name': name, 'Price': price, 'Status': status})

    with open(filename, 'r') as t1, open(filenameUpdated, 'r') as t2:
        fileOne = t1.readlines()
        fileTwo = t2.readlines()
        print("Controllo Nuova Disponibilità...")

        for line in fileTwo:
            if line not in fileOne:
                playsound("C:\\Users\\fatto\\Downloads\\ringtone.mp3")
                print("C'è roba!!!")

    print("Niente di nuovo per ora...")
    os.remove(filename)
    os.rename(filenameUpdated, filename)
    print("Nuovo controllo in:")
    countdown()


set_interval(startProgram, 30)
