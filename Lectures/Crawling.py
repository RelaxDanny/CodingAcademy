from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
result = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon", context=context)
bsObj = BeautifulSoup(result.read(), "html.parser")

for tag in bsObj.findAll("a"):
    if "href" in tag.attrs:
        print(tag.attrs["href"])

