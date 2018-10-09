import requests
from bs4 import BeautifulSoup
def get_list():
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }

    article_list = []
    for i in range(100):
        url = "https://www.waitsun.com/page/" + str(i+1);
        response = requests.get(url,headers = headers)
        # print(str(i+1),'页面编码',response.status_code)
        soup = BeautifulSoup(response.text,'lxml')
        article_list = soup.find_all('div',class_='posts-default-title')
        for article in article_list:
            text = article.h2.a.string
            print(text)

get_list()
