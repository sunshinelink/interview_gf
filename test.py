#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Test():

    def __init__(self):
        self.da = []

    #将网页数据转化为json格式
    def get_data(self, url):
        re = requests.get(url)
        try:
            data = json.loads(re.text)
        except:
            print "wrong data type"
            raise
        return data

    #将符合low<=avg<=high的项添加到da数组中
    def check_data(self, data):
        if type(data) != type([]):
            print "Wrong data type"
            return False
        for d in data:
            if self.check_logic(d):
                self.da.append(d)
        self.simulator(data)
    
    #判断low<=avg<=high，返回true or false
    def check_logic(self, data):
        if 'low' not in data or 'avg' not in data or 'high' not in data:
            return False
        try:
            data['low'] = float(data['low'])
            data['avg'] = float(data['avg'])
            data['high'] = float(data['high'])
        except:
            return False

        if data['low'] <= data['avg'] <= data['high']:
            print 'true', data
            return True
        else:
            print 'false', data
            return False

    #统计所有符合的项.
    def simulator(self,data):
        b = len(data)
        a = len(self.da)
        print "have pass"+str(a)
        print "not pass"+str(b-a)

if __name__ == "__main__":
    test = Test()
    data = test.get_data("http://quote.gf.com.cn/kline/daily/sz/000776/20")
    test.check_data(data)
