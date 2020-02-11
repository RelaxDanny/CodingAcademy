#if bs4 is not working, use selenium

from bs4 import BeautifulSoup
from urllib.request import urlopen

#response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
i = 1
f = open("test.txt", 'w')
with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("a"):
        data = str(i) + ". " + anchor.get('href', '/') + "\n" 
        i = i + 1
        f.write(data)
f.close()