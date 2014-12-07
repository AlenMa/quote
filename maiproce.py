'''
Created on 2014-12-7

@author: alenma
'''
from model.quote import Quote
import sendmail
import sinaquote
import time

mail_list=['ay8mateng@qq.com','2713618273@qq.com','183019974@qq.com']
if __name__ == '__main__':
    try:
        f=open('/home/alenma/workspace/quote/quotecode.txt','r')
        line=f.readline()
        quotes=[]
        while line:
            data=line.split('|')
            q=Quote(data[0],data[1],int(data[2]),float(data[3]))
            quotes.append(q)
            line=f.readline()
    finally:
        if f:
            f.close()
    
    up=0
    while up<=10:
        for i in quotes:
            price=sinaquote.getprice(i.code)+up
            rate=i.getrate(price)
            if rate>=0.2:
                subject="%s(%s)'s price is %s,rate is %f"  %(i.name,i.code,price,rate)
                content="%s(%s) 's price is %s,rate is %f"  %(i.name,i.code,price,rate)
                sendmail.send_mail(mail_list,subject,content)
                time.sleep(10)
        time.sleep(10)
        up+=1
        
            