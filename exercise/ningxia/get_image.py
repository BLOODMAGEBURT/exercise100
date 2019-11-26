# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_image
   Description :   获取工信厅网站的图片
   Author :       Administrator
   date：          2019/11/26 0026
-------------------------------------------------
   Change Activity:
                   2019/11/26 0026:
-------------------------------------------------
"""
import requests


def download_img(url, index):
    try:
        response = requests.get(url=url)
        # 获取的文本实际上是图片的二进制文本
        img = response.content
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        path = '.\\img\\{}.png'.format(index)
        with open(path, 'wb') as f:
            f.write(img)
        print('已经下载好第{}长'.format(i))
    except Exception as ex:
        print('---------------------出错继续----------------')


if __name__ == '__main__':
    for i in range(10):
        download_img("http://47.95.198.10:8090/web-reader/reader/image?_b=3.2.0"
                     "&_d=http%253A%252F%252Fwww.nx.gov.cn%252Fzwgk%252Fgfxwj%252F201911%252FW020191112390286380428.ofd"
                     "&_i={}&_v=1573527034000&_p=96".format(i), i)
