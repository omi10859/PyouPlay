from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from bs4 import BeautifulSoup
import requests


def PyouPlay(search):
    SearchUrl=str('https://www.youtube.com/results?search_query='+search)
    page=requests.get(SearchUrl)
    soup = BeautifulSoup(page.text, "lxml")
    print(page)
    link=soup.findAll(attrs={'class':'yt-uix-tile-link'})
    links=link[0]
    return (links['href'])
    for vid in link:
        return ('https://www.youtube.com' + vid['href'])
