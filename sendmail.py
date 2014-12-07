'''
Created on 2014-12-7

@author: alenma
'''
import smtplib
from email.mime.text import MIMEText

mail_host='smtp.sina.com'
mail_user='ay8mateng'
mail_pass='mtaixq1314'
mail_postfix='sina.com'

mailto_list=['16709732@qq.com']

def send_mail(to_list,sub,content):
    me=mail_user+'<'+mail_user+'@'+mail_postfix+'>'
    msg=MIMEText(content)
    msg['Subject']=sub
    msg['From']=me
    msg['To']=';'.join(to_list)

    try:
        s=smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

def test():
    if send_mail(mailto_list,'subject','content'):
        print 'success'
    else :
        print 'fail'
        
if __name__=='__main__':
    test()