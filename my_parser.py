import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

async def main(music_name: str) -> list:
    BASE_URL = "https://rum.muzikavsem.org/search/" + music_name
    HEADERS = {"User-Agent": UserAgent().random}
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items_name = soup.find_all("span", {"class": "top-tracks__track"})
            items_artist = soup.find_all("span", {"class": "top-tracks__artist"})
            links = []
            for link in soup.find_all('a', {"class": "top-tracks__download-btn clr-btn"}, href=True):
                links.append(link['href'])

            #link = soup.find_all("a", {"class": "top-tracks__download-btn clr-btn"})
            #get_link = link.get("href")
            #print(link)
            res = []
            print()
            n = len(links)

            if n >= 5:
                for i in range(5):
                    #get_link = link[i].text
                    res.append(items_name[i].text + " " + items_artist[i].text + " " + "https://rum.muzikavsem.org" + links[i])
            else:
                for i in range(n):
                    res.append(items_name[i].text + " " + items_artist[i].text + " " + "https://rum.muzikavsem.org" + links[i])

            return res

def start_main(text : str) -> list:
    loop = asyncio.get_event_loop()
    lst = loop.run_until_complete(main(text))
    #lst = main(text)
    return lst

#lst = start_main("я знаю какая ты")
#print(lst)