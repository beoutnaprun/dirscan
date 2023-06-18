import sys, os
import time, random
import requests, threading, urllib3, re, argparse
import multiprocessing as mg

sys.path.append("./Script/")  # 添加临时环境变量
import DirConf, ProxyPool, DirConf2,JSFinder,JSFinder2

name = '''

    |   |       |   |                              __________
    |   |       |   |                            /   -----   \          
    |   |_______|   |  _____           ______   /   /     \___\     _____     _______
    |    _______    |/  ___  \  \  /  /  ___  \ |   |             /      \  /   ___  \ 
    |   |       |   |  |___\  \  \/  /  /   \  \|   |     ______ /   ___  \/   /   \  \ 
    |   |       |   |  _____   |    |  |     |  \   \    |___   |   |___|  |  |     |  |
    |   |       |   |  \___/  /  /\  \  \___/ /\ \   \______/  / \        /|  |     |  |
    |___|       |___|\_______/  /  \  \______/  \_\___________/   \______/ |  |     |  |

    Hello, welcome to use the DirScan tool of HexaGon Laboratory
    The author of this article China Hacker X

    Please enter the - h parameter for help

'''
parser = argparse.ArgumentParser(description='This is the help!')
parser.add_argument('-u', '--url', help='要检测的url', default='')
parser.add_argument('-p', '--proxy', help="使用ProxyPool代理 输入 -p 1", default='')
args = parser.parse_args()
urllib3.disable_warnings()


def JSFind():
    urls = JSFinder.find_by_url(args.url)
    return JSFinder.giveresult(urls)

def Jsfreq_porxy(porxy):
    for i in JSFind():
        JSFinder.reqjsfurl(i, porxy)

def Jsfreq():
    for i in JSFind():
        JSFinder2.reqjsfurl(i)

if __name__ == '__main__':
    print(f"{name}")
    print("="*35+"正在检测请稍等！！！！！！！"+"="*35)
    if args.proxy == "1":
        if args.url != "":
            try:
                DirConf.req_url(args.url, ProxyPool.proxy())
            except:
                print("给出的url链接超时~~请等待爬取URL~~")
            try:
                Jsfreq_porxy(ProxyPool.proxy())
            except:
                print("爬取URL超时~~请等待爆破目录~~")
            try:
                DirConf.jincheng(args.url, ProxyPool.proxy())
            except:
                print("爆破失败~~请检查网络链接~~")
            try:
                a = input("是否继续爆破(消耗时间和发送大量请求严谨使用)（y/n）：")
                if a != "y" or a !="Y":
                    quit()
                else:
                    DirConf.alljincheng(args.url,ProxyPool.proxy())
            except:
                print("爆破失败~~请检查网络链接~~")

        else:
            print("\033[1;34;40m请输入-h查看使用方法\033[0m")

    # 不使用大力
    elif args.proxy == "":
        if args.url != "":
            try:
                DirConf2.req_url(args.url)      # 请求根目录
            except:
                print("给出的url链接超时~~请等待爬取URL~~")
            try:
                Jsfreq()  # 爬取url
            except:
                print("爬取URL超时~~请等待爆破目录~~")
            try:
                DirConf2.jincheng(args.url)  # 爆破目录
            except:
                print("爆破失败~~请检查网络链接~~")
            try:
                a = input("是否继续爆破(消耗时间和发送大量请求严谨使用)（y/n）：")
                if a != "y" or a !="Y":
                    quit()
                else:
                    DirConf2.alljincheng(args.url)
            except:
                print("爆破失败~~请检查网络链接~~")
        else:
            print("\033[1;34;40m请输入-h查看使用方法\033[0m")
    else:
        print("\033[1;34;40m请输入-h查看使用方法\033[0m")
