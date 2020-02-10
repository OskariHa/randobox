from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen as uReq


my_url = "https://www.google.com/finance"

req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = uReq(req)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup)
names = page_soup.find("span", {"class":"z4Fov"})
price = page_soup.find("span", {"class":"IsqQVc i3ALRMeFasi0-zJFzKq8ukm8"})
# <span class="z4Fov">Neste Oyj</span>
# <span class="IsqQVc i3ALRMeFasi0-zJFzKq8ukm8" jsname="vWLAgc">39,53</span>