'''
Created on 2014-12-7

@author: alenma
'''
from model.quote import Quote
import sendmail
import sinaquote
import time

if __name__ == '__main__':
    try:
        f=open('/home/alenma/workspace/quote/quotecode.txt','r')
        line=f.readline()
        quotes=[]
        while line:
            data=line.split('|')
            q=Quote(data[0],float(data[3]))
            quotes.append(q)
            line=f.readline()
    finally:
        if f:
            f.close()
    
    while True:
        for i in quotes:
            price=sinaquote.getprice(i.code)
            if i.ifgetprice(price):
                sendmail.send_mail(['ay8mateng@qq.com'], i.code, i.code+'now is'+price)
        time.sleep(10)
        
            