with open("合并.txt","r",encoding='utf-8') as f:
    a =f.read().split("\n")

list = []
lists = []
for i in a:
    if i not in list:
        list.append(i)
# print(len(list))
with open("dirall.txt","r",encoding='utf-8') as ff:
    aa =ff.read().split("\n")
for ii in aa:
    if ii not in list:
        lists.append(ii)
print(len(lists))
with open("1.txt","a",encoding='utf-8')as fa:
    for ia in lists:
        fa.write(ia+"\n")
