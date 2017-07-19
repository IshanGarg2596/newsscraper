import requests
from bs4 import BeautifulSoup

ndtvsoup = BeautifulSoup(ndtvpage.content, 'html.parser')


ndtv_news = ndtvsoup.find(class_="new_storylising")
# for more than 1 news:
headline = [hd['title'] for hd in ndtv_news.select(".nstory_header a")]
link = [l['href'] for l in ndtv_news.select(".nstory_header a") ]
#print (headline) with link
for hd,l in zip(headline,link):
    print (hd)
    print (l)
    print ("\n")


