import urllib2
import requests
from bs4 import BeautifulSoup

class ScrapeSite:
    def __init__(self):
        self.site = "https://ada.com/conditions/"

    def scrapeSite(self):
        page = requests.get(self.site)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.diseaseNames = soup.find_all("a",{"class":"sc-1lrc7ah-2 iHLyPt"})
        for diseaseName in self.diseaseNames:
            print diseaseName.text




obj = ScrapeSite()
obj.scrapeSite()
