from fastapi import FastAPI
from utils.get_images import search_bing


domain = 'santander.com'
search_img = search_bing(domain)
data = search_img.conn_scraping()
print(data)
# Comando:  python3 -m uvicorn main:app --reload
"""
app = FastAPI()
@app.get("/domain/{domain}")
async def main(domain):
    search_img = search_bing(domain)
    data = search_img.conn_scraping()
    return {"data": data}
"""
