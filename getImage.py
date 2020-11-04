#该程序不仅可以获取图片，而是可以获取更多如视频动画等以二进制代码保存的文件
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "C://Users//Xia Li//Documents//NingYeDocument//python//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件己存在")
except:
    print("爬取失败")
            
