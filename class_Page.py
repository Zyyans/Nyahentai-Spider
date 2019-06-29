from bs4 import BeautifulSoup
from requests import get


class Page():

    def __init__(self):
        self.mainurl = 'https://zh.nyahentai.net/'

    def soup_init(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
        leWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        response = get(url, headers=headers)
        if response.ok:
            return BeautifulSoup(response.text, 'lxml')
        else:
            return None
