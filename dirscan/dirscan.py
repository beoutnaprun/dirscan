import concurrent.futures, json
import requests, urllib3, argparse, random

urllib3.disable_warnings()

name = '''

    |   |        |   |                     |   |  /   /
    |   |        |   |                     |   | /   /
    |   |________|   |  _______       _____|   |/   /   _______   ___  _____
    |    ________    |/  ____  \    /  ____|   |   /   /  ___   \|   |/ __  \ 
    |   |        |   |  /    \  \  /  /    |   |   \  /  /___\   |     /  \_/ 
    |   |        |   | |      |  \/  /     |   |\   \/  _________|    /  
    |   |        |   |  \____/ /\ \  \_____|   | \   \  \________|   |          
    |___|        |___|\_______/  \_\_______|___|  \___\__________|___|          

    Hello, welcome to use the url DirScan tool of Chinese hacker Xue 
    Please enter the - h parameter for help
'''
parser = argparse.ArgumentParser(description='This is the help!')
parser.add_argument('-u', '--url', help='\t要检测的url', default='')
parser.add_argument('-t', '--thread', help='\t指定线程 默认30', default='30')
parser.add_argument('-p', '--proxy', nargs='?', const='127.0.0.1:5000', default=None,
                    help='指定是否使用代理 无参数自动5000端口代理 指定格式:127.0.0.1:5000')
parser.add_argument('-d', '--dings', nargs='?', const='', default="None",
                    help='指定动态代理（读取代理txt文件）详情请看runproxy()函数')
args = parser.parse_args()
urllib3.disable_warnings()


# 定义要请求的URL列表
def req_list(urls):
    list = []
    with open("Script/dict/dir1.txt", "r", encoding='utf-8') as f:
        a = f.read().split("\n")
    for i in a:
        if i.startswith("/"):
            url = urls + i
        else:
            url = urls + "/" + i
        if url not in list:
            list.append(url)
    return list


# 获取随机 user-agent
def getuseragemt():
    with open("./Script/dict/user-agent.txt", 'r', encoding="utf-8") as f:
        a = f.read()
        s = a.split("\n")
        return s[random.randint(0, len(s) - 1)]


# 随机获取代理
def openfile():
    with open("Proxy代理爬取/Proxy/proxy.txt", 'r', encoding='utf-8') as f:
        a = f.read().split("\n")
        return a


# 定义请求函数
def request_url(url, proxy):
    try:
        s = openfile()[random.randint(0, len(openfile()) - 1)]
        proxys = {
            "http":s
        }
        header = {
            "user-agent": f"{getuseragemt()}"
        }
        if proxy == "d":
            req = requests.get(url, verify=False, allow_redirects=False, headers=header, proxies=proxys, timeout=5)
            if req.status_code == 404:
                # print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
                pass
            elif req.status_code == 400:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 502:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 200:  # 绿色
                print(f"\033[1;32;40m{reqs.status_code}        {url}\033[0m")
            elif req.status_code == 302:  # 黄色
                print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 301:  # 黄色
                print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 403:  # 蓝色
                print(f"\033[1;34;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 500:  # 红色
                print(f"\033[1;31;40m{req.status_code}        {url}\033[0m")
            else:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
        else:
            req = requests.get(url, verify=False, allow_redirects=False, headers=header, timeout=5)
            if req.status_code == 404:
                # print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
                pass
            elif req.status_code == 400:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 502:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 200:  # 绿色
                print(f"\033[1;32;40m{reqs.status_code}        {url}\033[0m")
            elif req.status_code == 302:  # 黄色
                print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 301:  # 黄色
                print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 403:  # 蓝色
                print(f"\033[1;34;40m{req.status_code}        {url}\033[0m")
            elif req.status_code == 500:  # 红色
                print(f"\033[1;31;40m{req.status_code}        {url}\033[0m")
            else:
                print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"Error : {url}: {str(e)}")
        # pass


# 创建 爆破线程
def threq(urls, num_threads, proxy):
    # 使用线程池执行请求
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交每个URL的请求任务给线程池
        futures = [executor.submit(request_url, url, proxy) for url in urls]
        # 等待所有请求任务执行完毕
        concurrent.futures.wait(futures)
    print("All requests have finished execution.")


# 第一次请求给出的地址
def onereq(url):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    reqs = requests.get(url, headers=header, verify=False, allow_redirects=False, timeout=3)
    print(f"\033[1;32;40m{reqs.status_code}        {url}\033[0m")


# 非动态代理调用
def run():
    a = "y"
    try:
        onereq(args.url)
    except:
        a = input("给出的地址 无效访问~~~是否继续爆破(Y/N)")
    if a == "y" or a == "Y":
        if args.url != "":
            if args.proxy:
                proxy = {
                    "http": args.proxy
                }
                print(
                    f"\033[1;36;40m爆破地址: \033[0m \033[1;34;40m{args.url}\033[0m      \033[1;36;40m爆破线程: \033[0m \033[1;34;40m{args.thread}\033[0m  \033[1;36;40m爆破代理: \033[0m \033[1;34;40m{args.proxy}\033[0m ")
                print("=" * 30 + "正在爆破目录~~请稍等~~" + "=" * 30)
                threq(req_list(args.url), int(args.thread), proxy)
            else:
                print(
                    f"\033[1;36;40m爆破地址: \033[0m \033[1;34;40m{args.url}\033[0m      \033[1;36;40m爆破线程: \033[0m \033[1;34;40m{args.thread}\033[0m  \033[1;36;40m爆破代理: \033[0m \033[1;34;40m无\033[0m ")
                print("=" * 30 + "正在爆破目录~~请稍等~~" + "=" * 30)
                threq(req_list(args.url), int(args.thread), {})
        else:
            print("Error : 请使用-h查看帮助信息")


def runproxy():
    a = "y"
    try:
        onereq(args.url)
    except:
        a = input("给出的地址 无效访问~~~是否继续爆破(Y/N)")
    if a == "y" or a == "Y":
        if args.url != "":
            # s = openfile()[random.randint(0, len(a) - 1)]
            print(
                f"\033[1;36;40m爆破地址: \033[0m \033[1;34;40m{args.url}\033[0m      \033[1;36;40m爆破线程: \033[0m \033[1;34;40m{args.thread}\033[0m  \033[1;36;40m爆破代理: \033[0m \033[1;34;40m无\033[0m ")
            print("=" * 30 + "正在爆破目录~~请稍等~~" + "=" * 30)
            threq(req_list(args.url), int(args.thread), "d")
        else:
            print("Error : 请使用-h查看帮助信息")


if __name__ == '__main__':
    print(name)
    if args.dings:
        run()
    else:
        runproxy()
