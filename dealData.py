#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:52:07 2017

@author: user

@author: Administrator
本程序用于处理数据
"""
import pandas as pd
class dealData():
    
    def dealdata(self,goaldata,outdata,data,begin,end,col):
        #读取目标数据
        content = pd.read_table(goaldata,usecols=[0,1,col],)                         
        #读取输出数据          	 	
        f1 = open(outdata,"r");
        content1 = f1.readlines()[begin:end]
        
        #数据处理 
        f2 = open(data,"w");
        
        content = content.to_csv(data,header=False,index=False,sep="\t")
        
        #f2.write("%s"%content[0:61])
            
        
        #重置指针
        f2.seek(0,2) 
        for line in content1:
            #print line           
        #content1 = f1.read(410)     
            line = line[:-2]
            f2.write("%s\n"%line)                          
        f1.close()                
        f2.close()
'''
goaldata = "/home/user/Desktop/Data/goaldata.csv"
#goaldata = "/home/user/Desktop/Data/state0_1_2.csv"
#goaldata = "/home/user/Desktop/Data/statis_varib_state2.csv"
outdata = "/home/user/Desktop/Data/outdata20170908"
data = "/home/user/Desktop/Data/data20170908"
#begin,end,col = 45,106,2
begin,end,col = 44,105,8
#begin,end,col = 18,79,2
d = dealData()
d.dealdata(goaldata,outdata,data,begin,end,col)
'''