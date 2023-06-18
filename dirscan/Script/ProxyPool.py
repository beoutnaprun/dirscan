import requests

# 获取代理池内代理
def get_proxy():
    # 5000：settings中设置的监听端口，不是Redis服务的端口
    return requests.get("http://127.0.0.1:5010/get/").json()

# 从代理池删除代理
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

def proxy():
    a = get_proxy().get("proxy")
    proxys = {"http": "http://{}".format(a)}
    return proxys
