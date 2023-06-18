**1、dirscan.py 目录爆破工具**
=
![image](https://github.com/beoutnaprun/dirscan/assets/133112969/6e38f629-7e59-4ded-9fd8-b1a05541a843)

使用方法：
-
```
正常使用:
    python dirscan.py -u http://192.168.0.155
    
设置线程：
    python dirscan.py -u http://192.168.0.155 -t 5
    
使用静态代理
    python dirscan.py -u http://192.168.0.155 -t 5 -p 127.0.0.1:5000
    
使用动态代理：
    python dirscan.py -u http://192.168.0.155 -t 5 -d
```
工具介绍：
    一款继承性目录爆破工具，可使用静态代理，动态代理，还可对根目录无法访问的页面进行爆破

**2、MyProxy.py免费代理爬取工具**
=
```
所在位置：Proxy代理爬取 文件夹下（位置请不要随意更换）
```
使用方法：
-
```
python MyProxy.py
```
**3、pageCrawling.py页面URL爬虫**
=
使用方法：
-
```
python pageCrawling.py -u https://www.baidu.com/
```

工具介绍：
-
```
自动爬取页面的 url链接 / JavaScript链接 / CSS链接 / 图片链接 / Js文件中的链接
```
![image](https://github.com/beoutnaprun/dirscan/assets/133112969/71496fc5-46d2-40a2-baf8-14db866757fb)


**4、Dos.py DOS工具**
=
```
慎用：
    基于多进程多线程发送大量请求，致使目标宕机
使用方法：
    python Dos.py -u http://192.168.0.152
工具介绍：
    伤敌一千自损八百，纯破坏性工具
```
