from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen as uReq


def get_air_rune():

    my_url = "http://services.runescape.com/m=itemdb_rs/Air+rune/viewitem?obj=556"

    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    names = page_soup.findAll("div", {"class": "item-description"})
    if names == "":
        names = page_soup.findAll("div", {"class": "item-description member"})

    for item in names:
        temp = item.find("h2")
        if temp:
            print(temp.text)

    prizes = page_soup.findAll("div", {"class": "stats"})
    returned = ""
    for prize in prizes:
        temp = prize.find("h3")
        if temp:
            returned = temp.text
            print(temp.text)

    return returned

