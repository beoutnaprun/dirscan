import sys, requests,os, shutil
import threading
sys.path.append("Script")
import GetProxy



localproxy = {
        # "http":"127.0.0.1:33210",
        # "https":"127.0.0.1:33210"
    }

if __name__ == '__main__':
    # 删除文件夹
    shutil.rmtree("Proxy")
    # 创建代理文件夹
    os.mkdir("Proxy")
    CURL = 'https://www.baidu.com'     # """ 检测地址 常量"""

    """　稻壳代理爬取检测　"""
    url1 = "https://www.docip.net/data/free.json"
    GetProxy.getproxys(url1,localproxy)      # 获取稻壳代理 写入文件 接受一个爬取页面时的代理参数，默认为
    filename = "Proxy/daokedaili.txt"       # 稻壳代理文件名
    threading.Thread(target=GetProxy.requrls,args=(localproxy,filename,CURL)).start()   # 检测可用代理地址 写入ok.txt  参数 1、代理 2、文件路径及名称 3、检测地址

    """ 89 代理爬取检测"""
    url2 = "https://www.89ip.cn/index_1.html"
    GetProxy.get89(url2,localproxy)
    filename = "Proxy/89.txt"
    threading.Thread(target=GetProxy.requrls,args=(localproxy,filename,CURL)).start()   # 检测可用代理地址 写入ok.txt  参数 1、代理 2、文件路径及名称 3、检测地址

    """ 小幻代理  """
    url3 = "https://ip.ihuan.me/address/5Lit5Zu9.html"
    GetProxy.getxh(url3, localproxy)
    filename = "Proxy/xh.txt"
    threading.Thread(target=GetProxy.requrls,args=(localproxy, filename, CURL)).start()  # 检测可用代理地址 写入ok.txt  参数 1、代理 2、文件路径及名称 3、检测地址

    """ 云代理 """
    url4 = "http://www.ip3366.net/free/?stype=1"
    GetProxy.getyun(url4, localproxy)
    filename = "Proxy/yun.txt"
    threading.Thread(target=GetProxy.requrls,args=(localproxy, filename, CURL)).start()  # 检测可用代理地址 写入ok.txt  参数 1、代理 2、文件路径及名称 3、检测地址

    """ 开心代理 """
    url5 = "http://www.kxdaili.com/dailiip/1/"
    GetProxy.getkx(url5, localproxy)
    filename = "Proxy/kx.txt"
    threading.Thread(target=GetProxy.requrls, args=(localproxy, filename, CURL)).start()  # 检测可用代理地址 写入ok.txt  参数 1、代理 2、文件路径及名称 3、检测地址