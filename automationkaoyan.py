import requests
from bs4 import BeautifulSoup
def get_list():
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36'
    }

    article_list = []
    for i in range(233):
        url = "http://bbs.kaoyan.com/f21p" + str(i+1);
        response = requests.get(url,headers = headers)
        # print(str(i+1),'页面编码',response.status_code)
        soup = BeautifulSoup(response.text,'lxml')
        article_list = soup.find('table',id='threadlisttableid').select('tbody[id*=normalthread]')
        # print(article_list)
        for item in article_list:
            result = item.select_one('a[class="s xst"]').get_text()
            href = item.select_one('a[class="s xst"]')['href']
            num = str(item.select_one('td[class="num"]').em.string)
            reply_num = str(item.select_one('td[class="num"]').a.string)
            print("%-40s" % result + "-----点击数:" + num + "-"+"回复数:"+reply_num +"---" + href)

get_list()
