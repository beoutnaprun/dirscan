import re
import requests,threading
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()

class GetProxy(threading.Thread):
    def __init__(self,url,localproxy,filename,curl):
        super().__init__()
        self.url = url
        self.filename = filename
        self.curl = curl
        self.localproxy =  localproxy
    """爬取稻壳代理"""
    def getdk(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        req = requests.get(self.url, headers=header, proxies=self.localproxy, verify=False, timeout=10)  # 请求代理网站
        return req.json()["data"]

    """将稻壳代理写入txt文件中  url(爬取的页面)"""

    def daoke(self):
        for i in self.getdk():
            with open("Proxy/daokedaili.txt", "a+", encoding='utf-8') as f:
                f.write(str(i["ip"]) + "\n")


    """ 89 免费代理"""
    def get89(self):
        """ 89免费代理 """
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        r = requests.get(self.url, verify=False, timeout=10,headers=header)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        # print(proxies)
        for proxy in proxies:
            a = ':'.join(proxy)
            with open("Proxy/89.txt", "a+", encoding='utf-8') as f:
                f.write(a + "\n")
    """ 小幻代理"""
    def getxh(self):
        """ 小幻代理 """
        r = requests.get(self.url,verify=False, timeout=10)
        proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
        for proxy in proxies:
            a = ":".join(proxy)
            with open("Proxy/xh.txt", "a+", encoding='utf-8') as f:
                f.write(a + "\n")
    """ 云代理 """
    def getyun(self):
        """ 云代理 """
        r = requests.get(self.url, timeout=10)
        proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
        for proxy in proxies:
            a = ":".join(proxy)
            with open("Proxy/yun.txt", "a+", encoding='utf-8') as f:
                f.write(a + "\n")
    """ 开心代理 """
    def getkx(self):
        # """ 开心代理 """
        for u in range(1, 10):
            urls = self.url + f"{u}.html"
            r = requests.get(urls, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                a = ":".join(proxy)
                with open("Proxy/kx.txt", "a+", encoding='utf-8') as f:
                    f.write(a + "\n")

    """读取爬取的代理文件，拼接url请求测试"""
    def requrl(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        with open(self.filename, "r") as f:
            a = f.read().split("\n")
            for i in range(0, len(a) - 1):
                proxy = {
                    "http": a[i]
                }
                try:
                    req = requests.get(self.curl, verify=False, headers=header, proxies=proxy, timeout=10)
                    if req.status_code == 200:
                        print(f"正在写入可用代理:{a[i]}")
                        with open("Proxy/proxy.txt", "a+", encoding='utf-8') as f:
                            f.write(a[i] + "\n")
                except:
                    print(f"代理不可用:{proxy}")
#　爬取写入函数
def getproxys(url,proxy):
    GetProxy(url,proxy,"","").daoke()
def get89(url,proxy):
    GetProxy(url,proxy,"","").get89()
def getxh(url,proxy):
    GetProxy(url,proxy,"","").getxh()
def getyun(url,proxy):
    GetProxy(url,proxy,"","").getyun()
def getkx(url,proxy):
    GetProxy(url,proxy,"","").getkx()


# 检测函数
def requrls(proxy,filename,curl):
    GetProxy(0,proxy,filename,curl).requrl()