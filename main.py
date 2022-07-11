import asyncio
from scraping.get_images import request_session

if __name__ == '__main__':
    domain = 'santander.com'
    search_img = asyncio.run(request_session(domain))
    print(search_img)
