import json
import requests
from bs4 import BeautifulSoup


class search_bing:
    def __init__(self, domain: str):

        self.domain = domain
        self.url = "https://www.bing.com/images/search?q=" + self.domain + "&FORM=HDRSC2"
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        # self.url = "https://www.bing.com/images/search"
        # self.search = self.domain
        # self.params = {"q": self.search, "form": "HDRSC2", "first": "1", "scenario": "ImageBasicHover"}

    def conn_scraping(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            url_image = soup.findAll('img')
            for i in url_image:
                print(i)
           # return json_data
