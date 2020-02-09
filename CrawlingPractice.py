from bs4 import BeautifulSoup
from urllib.request import urlopen

#response = urlopen('https://en.wikipedia.org/wiki/Main_Page')

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("a"):
        print(anchor.get('href','/'))

#python --version