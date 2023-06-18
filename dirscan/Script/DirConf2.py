import sys,os
import time,random
import requests, threading, urllib3, re, argparse
import multiprocessing as mg


# 创建类
class DirConf(threading.Thread):
    def __init__(self,filename,min_num,max_num,args):
        super().__init__()
        self.args = args
        self.min_num = min_num
        self.max_num = max_num
        self.filename = filename
    def read_dict(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            a = f.read()
            return a.split("\n")
    # 判断url取消最后斜杠
    def panduan(self):
        list = []
        for i in self.args:
            list.append(i)
        # return list[len(args)-1]
        if list[len(self.args) - 1] != "/":
            url = self.args
        else:
            url = ""
            del list[-1]
            for ii in list:
                url = url + ii
        return url

    # 获取字典内容 拼接URL
    def getdir(self):
        list = []
        for i in self.read_dict():
            if i.startswith("/"):
                list.append(self.panduan() + i )
            else:
                list.append(self.panduan()+"/"+i)
        return list

    # 切换UA绕过封禁
    # GetUA
    def getuseragemt(slef):
        with open("./Script/dict/user-agent.txt", 'r', encoding="utf-8") as f:
            a = f.read()
            s = a.split("\n")
            return s[random.randint(0, len(s) - 1)]

    # 发送 网站请求
    # """
    #         - 红色：`\033[91m`
    #         - 绿色：`\033[1;32;40m`      \033[0m(结束)
    #         - 黄色：`\033[1;33;40m`
    #         - 蓝色：`\033[1;34;40m`
    #         - 紫色：`\033[1;35;40m`
    #         - 青色：`\033[1;36;40m`
    #         - 白色：`\033[1;37;40m`
    #             :param url:
    #             :return:
    #             """
    # print('\033[91m' + '红色' + '\033[0m')
    # print('\033[92m' + '绿色' + '\033[0m')
    # print('\033[93m' + '黄色' + '\033[0m')
    # print('\033[94m' + '蓝色' + '\033[0m')
    # 其中，属性值的含义如下：
    #
    # | 属性值 | 颜色 |
    # | ------ | ------ |
    # | 30 - 37 | 文字颜色 |
    # | 40 - 47 | 背景颜色 |
    # | 0 | 重置 |
    # | 1 | 粗体 |
    # | 2 | 粗体 |
    # | 3 | 斜体 |
    # | 4 | 下划线 |


    def run(self):
        list = []
        for i in range(self.min_num,self.max_num):
            url = self.getdir()[i]
            header = {
                "user-agent": f"{self.getuseragemt()}"
            }
            try:
                req = requests.get(url,verify=False,timeout=10,headers=header)

                if req.status_code == 404:
                    print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 400:
                    print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 502:
                    print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 200:  # 绿色
                    reqs = requests.get(url,verify=False,timeout=10,headers=header,allow_redirects=False)
                    if reqs == 200:
                        list.append(f"\033[1;32;40m{reqs.status_code}        {url}\033[0m")
                        print(f"\033[1;32;40m{reqs.status_code}        {url}\033[0m")
                    else:
                        list.append(f"\033[1;35;40m{reqs.status_code}        {url}\033[0m")
                        print(f"\033[1;35;40m{reqs.status_code}        {url}\033[0m")
                elif req.status_code == 302:  # 黄色
                    list.append(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
                    print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 301:  # 黄色
                    list.append(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
                    print(f"\033[1;33;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 403:  # 蓝色
                    list.append(f"\033[1;34;40m{req.status_code}        {url}\033[0m")
                    print(f"\033[1;34;40m{req.status_code}        {url}\033[0m")
                elif req.status_code == 500:  # 红色
                    list.append(f"\033[1;31;40m{req.status_code}        {url}\033[0m")
                    print(f"\033[1;31;40m{req.status_code}        {url}\033[0m")
                else:
                    print(f"\033[1;36;40m{req.status_code}        {url}\033[0m")
            except:
                print(f"\033[1;31;40m超时        {url}\033[0m")
                # pass
        for i in list:
            print(i)


# 请求输入地址
def req_url(args):
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    r = requests.get(args, headers=header, verify=False, timeout=3)
    print(f"\033[1;32;40m{r.status_code}        {args}\033[0m")

# 获取字典长度 调用线程
def reqopenfile(filename,args):
    with open(filename,"r",encoding='utf-8') as f:
        a = len(f.read().split("\n"))
    # 调用类创建线程请求url
    for i in range(0, a):
        DirConf(filename, i, i + 1,args).start()

def jincheng(args):
    # api
    apiname = "./Script/dict/Api.txt"
    mg.Process(target=reqopenfile(apiname, args)).start()
    # dir1
    dirname_1 = "./Script/dict/dir1.txt"
    mg.Process(target=reqopenfile(dirname_1,args)).start()
    # dir2
    dirname_2 = "./Script/dict/dir2.txt"
    mg.Process(target=reqopenfile(dirname_2,args)).start()
    # dir3
    dirname_3 = "./Script/dict/dir3.txt"
    mg.Process(target=reqopenfile(dirname_3,args)).start()
    # dir4
    dirname_4 = "./Script/dict/dir4.txt"
    mg.Process(target=reqopenfile(dirname_4,args)).start()

def alljincheng(ages):
    # dir1
    diralname_1 = "./Script/dict/Diral/1.txt"
    mg.Process(target=reqopenfile(diralname_1, args,)).start()
    # dir2
    diralname_2 = "./Script/dict/Diral/2.txt"
    mg.Process(target=reqopenfile(diralname_2, args,)).start()
    # dir3
    diralname_3 = "./Script/dict/Diral/3.txt"
    mg.Process(target=reqopenfile(diralname_3, args,)).start()
    # dir4
    diralname_4 = "./Script/dict/Diral/4.txt"
    mg.Process(target=reqopenfile(diralname_4, args,)).start()
    # dir1
    diralname_5 = "./Script/dict/Diral/5.txt"
    mg.Process(target=reqopenfile(diralname_5, args,)).start()
    # dir2
    diralname_6 = "./Script/dict/Diral/6.txt"
    mg.Process(target=reqopenfile(diralname_6, args,)).start()
    # dir3
    diralname_7 = "./Script/dict/Diral/7.txt"
    mg.Process(target=reqopenfile(diralname_7, args,)).start()
    # dir4
    diralname_8 = "./Script/dict/Diral/8.txt"
    mg.Process(target=reqopenfile(diralname_8, args,)).start()