'''
Created on 2014-12-7

@author: alenma
'''

class Quote(object):
    '''
    classdocs
    '''

    def __init__(self, code,name,count,price_buy):
        '''
        Constructor
        '''
        self.code=code
        self.name=name 
        self.count=count
        self.price_buy=price_buy
    
    def ifgetprice(self,price):
        rate=(price-self.price_buy)/self.price_buy
        if rate>=0.2 :
            return True
        else:
            return False
    
    def getrate(self,price):
        return  (price-self.price_buy)/self.price_buy
            