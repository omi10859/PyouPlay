from bs4 import BeautifulSoup
import requests
import webbrowser


def toplink(search, open_in_browser=0):
    SearchUrl=str('https://www.youtube.com/results?search_query='+search)
    page=requests.get(SearchUrl)
    soup = BeautifulSoup(page.text, "lxml")
    print(page)
    link=soup.findAll(attrs={'class':'yt-uix-tile-link'})
    links=link[0]

    if not open_in_browser:
        return 'https://www.youtube.com' + links['href']
    else:
        webbrowser.open_new('https://www.youtube.com' + links['href'])

def toplinks(search, open_in_browser=0):
    SearchUrl=str('https://www.youtube.com/results?search_query='+search)
    page=requests.get(SearchUrl)
    soup = BeautifulSoup(page.text, "lxml")
    print(page)
    link=soup.findAll(attrs={'class':'yt-uix-tile-link'})

    if not open_in_browser:
        return ['https://www.youtube.com' + vid['href'] for vid in link]

    for vid in link:
        webbrowser.open_new('https://www.youtube.com' + vid['href'])


