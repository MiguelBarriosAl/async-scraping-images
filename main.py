from fastapi import FastAPI
from utils.get_images import WebScraper

domain = 'santander.com'
url = "https://www.bing.com/images/search?q=" + domain + "&FORM=HDRSC2"
search_img = WebScraper(url)
data = search_img.fetch()
print(data)

# Comando:  python3 -m uvicorn main:app --reload /multihilo para analizar link en paralelo
"""
app = FastAPI()
@app.get("/domain/{domain}")
async def main(domain):
    search_img = search_bing(domain)
    data = search_img.conn_scraping()
    return {"data": data}
"""
