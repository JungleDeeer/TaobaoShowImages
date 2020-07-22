import requests
from bs4 import BeautifulSoup
import re
import random


ipList = []
class proxy():
    def __init__(self):
        self.key = 'proxy'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

    def getContent(self):

        url = 'http://www.goubanjia.com/'
        data = requests.get(url, headers=self.headers)
        self.parse(data.text)

    def parse(self, data):

        soup = BeautifulSoup(data, 'html.parser')
        result = soup.find_all('td', class_='ip')
        for x in result:
            port = x.find(name='span', class_='port').attrs
            port = port['class'][-1]
            port = self.parse_port(port)
            # print('port:',port)
            data = re.compile('<p.*?/p>|<span class="port.*">.*</span>?|<.*?>', re.S)
            res = re.sub(data, '', str(x))
            # print('res:',res)
            ipList.append(res + str(port))

    def parse_port(self, port):

        string = 'ABCDEFGHIZ'
        arr = list(port)
        lists = []
        for x in range(0, len(arr)):
            lists.append(string.find(arr[x]))

        ports = ''.join(str(x) for x in lists)
        return int(ports) >> 3

    def random(self):

        url = 'https://www.baidu.com'

        self.getContent()
        value = ipList[random.randint(1, len(ipList))]
        proxies = {"http": "http://" + value}
        try:
            data = requests.get(url=url, headers=self.headers, proxies=proxies, timeout=5)
            if data.status_code is not 200:
                print('连接失败删除')
                ipList.delete(self.key, value)
                self.random()
            else:
                print("http://" + value)
                return "http://" + value
        except Exception as err:
            print(err)
            print('异常删除')
            print()
            ipList.remove(value)
            self.random()




proxy = proxy()
