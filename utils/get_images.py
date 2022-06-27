import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url: str):

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        self.url = url
        # self.search = self.domain
        # self.params = {"q": self.search, "form": "HDRSC2", "first": "1", "scenario": "ImageBasicHover"}

    def fetch(self) -> list:
        resp = requests.get(self.url, headers=self.headers)
        assert resp.status_code == 200
        img_tag = self.extract_img_tag(resp)
        return img_tag

    def extract_img_tag(self, resp) -> list:
        try:
            soup = BeautifulSoup(resp.content, "html.parser")
            url_image = soup.findAll('img')
            task = [tag.get("src2") for tag in url_image if tag.get("src2")]
            return task
        except Exception as e:
            print(str(e))
