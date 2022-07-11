import requests
from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def extract_img_tag(resp) -> list:
    try:
        soup = BeautifulSoup(resp.content, "html.parser")
        url_image = soup.findAll('img')
        task = [tag.get("src2") for tag in url_image if tag.get("src2")]
        return task
    except Exception as e:
        print(str(e))


async def get_character(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    img_tag = await extract_img_tag(resp)
    return img_tag


async def request_session(domain: str):
    url = "https://www.bing.com/images/search?q=" + domain + "&FORM=HDRSC2"
    async with ClientSession() as session:
        character = await get_character(url=url)
        return character
