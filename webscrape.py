from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen as uReq

my_url = "http://services.runescape.com/m=itemdb_rs/Large+blunt+rune+salvage/viewitem?obj=47302"


req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = uReq(req)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

names = page_soup.findAll("div", {"class":"item-description"})
if names == "":
    names = page_soup.findAll("div", {"class":"item-description member"})

for item in names:
    temp = item.find("h2")
    if temp:
        print(temp.text)

prizes = page_soup.findAll("div", {"class":"stats"})

for prize in prizes:
    temp = prize.find("h3")
    if temp:
        print(temp.text)



# ge 6050 itemii obj=2 obj=6051
