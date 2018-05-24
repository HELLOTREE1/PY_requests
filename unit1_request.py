#-*-coding:utf-8-*-
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#如果不是200，引发HTTPError异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__=="__main__":
    url="https://www.jd.com/allSort.aspx"
    print(getHTMLText(url))