'''
Created on 2014-12-7

@author: alenma
'''
import urllib

def request(code):
    url=''
    if code.startswith('6'):
        url='http://hq.sinajs.cn/list=sh%s'  %code
    else:
        url='http://hq.sinajs.cn/list=sz%s'  %code
    
    return urllib.urlopen(url).readlines()

def getprice(code):
    data=request(code)
    return float(data[0].split('"')[1].split(',')[3])

if __name__ == '__main__':
    print getprice('000587')