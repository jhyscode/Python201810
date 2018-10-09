import requests
from bs4 import BeautifulSoup
def get_list():
    headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }

    article_list = []
    for i in range(80):
        url = "http://www.carrotchou.blog/page/" + str(i);
        response = requests.get(url,headers = headers)
        # print(str(i+1),'页面编码',response.status_code)
        soup = BeautifulSoup(response.text,'lxml')
        article_list = soup.select('article[class*="excerpt"]')
        for article in article_list:
            title = article.header.h2.string
            print(title)
get_list()
