import requests, re, urllib3, argparse, sys
sys.path.append("./Script/")  # 添加临时环境变量
import JSFinder2,JSFinder

name = '''

    |   |        |   |                     |   |  /   /
    |   |        |   |                     |   | /   /
    |   |________|   |  _______       _____|   |/   /   _______   ___  _____
    |    ________    |/  ____  \    /  ____|   |   /   /  ___   \|   |/ __  \ 
    |   |        |   |  /    \  \  /  /    |   |   \  /  /___\   |     /  \_/ 
    |   |        |   | |      |  \/  /     |   |\   \/  _________|    /  
    |   |        |   |  \____/ /\ \  \_____|   | \   \  \________|   |          
    |___|        |___|\_______/  \_\_______|___|  \___\__________|___|          

    Hello, welcome to use the url DirScan tool of Chinese hacker X 
    Please enter the - h parameter for help
'''
parser = argparse.ArgumentParser(description='This is the help!')
parser.add_argument('-u', '--url', help='要检测的url', default='')
args = parser.parse_args()
urllib3.disable_warnings()
proxy = {
    # "http":"127.0.0.1"33210",
    # "https":"127.0.0.1"33210"
}


def paquurl(url):
    list = []
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    req = requests.get(url,verify=False,headers=header,timeout=5,proxies=proxy).text
    rjs = re.findall('="(/.*?\.js)',req) or re.findall('src="(.*?\.js)',req) or re.findall('href="(.*?\.js)',req)
    for js in rjs:
        if js not in list:
            list.append(js)
    rcss = re.findall('="(/.*?\.css)',req) or re.findall('href="(.*?\.css)',req) or re.findall('src="(.*?\.css)',req)
    for css in rcss:
        if css not in list:
            list.append(css)
    rurl =  re.findall('src="(.*?)"',req) or re.findall('href="(.*?)"',req)
    for i in rurl:
        if i not in list:
            list.append(i)
    return list


def getpathurl(url):
    list = []
    r = re.findall("(https://.*?)/", url) or re.findall("(http://.*?)/", url)
    rpath = re.findall("(https://.*/)", url) or re.findall("(http://.*/)", url)
    for ri in paquurl(url):
        if ri.startswith("../"):
            an_url = rpath[0] + ri
            if an_url not in list:
                list.append(an_url)
    for i in paquurl(url):
        if i.startswith("/"):
            resutl_url = r[0] + i
            if resutl_url not in list:
                list.append(resutl_url)
    return list
    # """
    #         - 红色：`\033[1;31;40m`
    #         - 绿色：`\033[1;32;40m`
    #         - 黄色：`\033[1;33;40m`
    #         - 蓝色：`\033[1;34;40m`      \033[0m
    #         - 紫色：`\033[1;35;40m`
    #         - 青色：`\033[1;36;40m`
    #         - 白色：`\033[1;37;40m`
    #             :param url:
    #             :return:
    #
def js_zhengli(url):
    js_list = []
    css_list = []
    list = []
    img_list = []
    for i in getpathurl(url):
        if ".js" in i :
            js_list.append(f"\033[1;33;40m{i}\033[0m")
        elif ".css" in i :
            css_list.append(f"\033[1;31;40m{i}\033[0m")
        elif ".png" in i or ".jpg" in i or ".gif" in i:
            img_list.append(f"\033[1;35;40m{i}\033[0m")
        else:
            list.append(f"\033[1;32;40m{i}\033[0m")
    img_list.insert(0, "+" * 35 + "图片链接" + "+" * 35)
    js_list.insert(0, "+" * 34 + "JavaScript链接" + "+" * 34)
    css_list.insert(0, "+" * 35 + "CSS链接" + "+" * 35)
    list.insert(0, "+" * 37 + "URL链接" + "+" * 37)

    return list,js_list,css_list,img_list

def JSFind():
    urls = JSFinder.find_by_url(args.url)
    return JSFinder.giveresult(urls)

if __name__ == '__main__':
    print(name)
    for i in js_zhengli(args.url):
        for ii in i:
            print(ii)
    print("="*30+"JS文件中的链接"+"="*30)
    for i in JSFind():
        # JSFinder2.reqjsfurl(i)          # 检测存活
        print(i)            # 不检测存活直接打印
