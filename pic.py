from bs4 import BeautifulSoup
import urllib,requests
import os
import sys
import re

file_path=r"./pic"




def start(giveurl,id,name):
    #url=r"https://www.ivsky.com/tupian/taohua_t1434/"+"index_"+str(id)+".html"
    url=giveurl+"index_"+str(id)+".html"
    r=requests.get(url).text

    soup = BeautifulSoup(r,'html.parser')
    pic_list = soup.find_all('img')

    pattern = re.compile(r'src=".+')#正则对象   

    pic_name=name
    filename = '{}{}{}{}'.format(file_path,os.sep,str(pic_name),".jpg")

    for item in pic_list:
        x=re.findall(pattern,str(item))
        y=x[0].split('"')[1].replace("/t/","/pre/",1)
        y="http:"+y

        urllib.request.urlretrieve(y,filename)
        print(pic_name)

        pic_name+=1
        filename = '{}{}{}{}'.format(file_path,os.sep,str(pic_name),".jpg")

    return pic_name    

def main():
    if len(sys.argv)==2:
        id=1
        name=1
        giveurl=sys.argv[1]
        while 1:
            name=start(giveurl,id,name)
            id+=1
    else:
        print(r'''
        输入错误，请自行去网站查找对应图片集的链接
        ----->https://www.ivsky.com/tupian/<-----

        示例：https://www.ivsky.com/tupian/taohua_t1434/
        命令为：python .\pic.py https://www.ivsky.com/tupian/taohua_t1434/''')
   

if __name__ == "__main__":
    main()