#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 06:41:13 2017

@author: user
画图
@author: Administrator
"""
import time
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit, poly1d
#from scipy.linalg import lstsq
#from scipy.stats import linregress
#from scipy.optimize import curve_fit
class plot(object):
    
    def getData(self,row,ratio):
        
        VG = []
        IDtarget = []          
        IDsimulate = []          #target and simulated I–V points
                 
        
        Gmtarget = []
        Gmsimulate = []
        Gdtarget = []
        Gdsimulate = []
        
        f = pd.read_table('/home/user/Desktop/Data/data20170913' , header=None)
        #f = pd.read_table('/home/user/Desktop/Data/data20180601', header=None)
        
        for i in range(row):
            IDtarget.append(f[2][i])
            VG.append(f[1][i])
        IDtarget = [i/ratio for i in IDtarget]    
        #print IDtarget
        for i in range(row,row*2):
            IDsimulate.append(f[2][i])
        IDsimulate = [-i for i in IDsimulate]
        #print IDsimulate                     
        #print (VG[j],IDtarget[j])
        #ratio 代表转换比例
        #IDtarget1 = [math.log10(x/ratio) for x in IDtarget]          
        #IDsimulate1 = [math.log10(x) for x in IDsimulate] 
        
        '''
        cofficient1 = polyfit(VG,IDtarget,2)
       
        print cofficient1 
        print poly1d(cofficient1)
        
        #slope, intercept, r_value, p_value, stderr = linregress(VG,IDtarget)
        #print slope, intercept
        print poly1d(cofficient1).deriv(1)
        print poly1d(cofficient1).deriv(1)[1],poly1d(cofficient1).deriv(1)[0]
       
        for i in IDtarget:
             Gmtarget.append(poly1d(cofficient1).deriv(1)[1]*i + poly1d(cofficient1).deriv(1)[0])   
        #print Gmtarget
        
        cofficient2 = -polyfit(VG,IDsimulate,2)
        
        print cofficient2
        print poly1d(cofficient2)   
        print poly1d(cofficient2).deriv(1)
        prin t poly1d(cofficient1).deriv(1)[1],poly1d(cofficient2).deriv(1)[0]
        
        for i in IDsimulate:
             Gmsimulate.append(poly1d(cofficient2).deriv(1)[1]*i + poly1d(cofficient2).deriv(1)[0])   
        #print Gmsimulate ,Gmtarget,Gmsimulate,IDsimulate1,IDtarget1
        '''
        return VG,IDsimulate,IDtarget
    
    def Draw(self,VG,IDsimulate,IDtarget,save):
        
        
        plt.figure(num =1,figsize=(9,6))
        #plt.title("Figure1")  
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("Id/A", size=20)
        #plt.grid()
        target, = plt.plot(VG,IDtarget,'rs',label="TCAD data")
        simulate, = plt.plot(VG,IDsimulate,'k-',label="Compact model") 
        '''
        for j in range(row):
            target, = plt.plot(VG[j],IDtarget[j]/ratio,'r>',label="TCAD data")    
        for j in range(row):
            simulate, = plt.plot(VG[j],-IDsimulate[j],'ko',label="Compact model")
        '''
        plt.legend(handles=[target, simulate],edgecolor='w',fontsize = 20)  
                          
        plt.ticklabel_format(scilimits=(-1,0))       
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig('/home/user/Desktop/LD100st0res.eps', format='eps', dpi=100)
        plt.show()
         
        plt.figure(num =2,figsize=(9,6))                  
        #plt.title("Figure2")  
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("log(Id/A)", size=20)
                
        #plt.legend("IDtarget","IDsimulate")
        #plt.grid()
        target1, = plt.semilogy(VG,IDtarget,'rs', label="TCAD data")
        simulate1, = plt.semilogy(VG,IDsimulate,'k-',label="Compact model")
        '''
        for j in range(row):
            target1, = plt.plot(VG[j],IDtarget1[j],'r^', label="TCAD data")    
        for j in range(row):
            simulate1, = plt.plot(VG[j],IDsimulate1[j],'k-',label="Compact model")
        '''
        plt.legend(handles=[target1, simulate1],edgecolor='w',fontsize = 20)        
        #plt.ticklabel_format(style='sci')                
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig('/home/user/Desktop/LD100st0logres.eps', format='eps', dpi=100) 
        plt.show()
        
save = 0        
plot = plot()
row,ratio = 61,1
VG,IDsimulate,IDtarget = plot.getData(row,ratio)    
plot.Draw(VG,IDsimulate,IDtarget,save)

f1 = math.sqrt(sum((IDtarget[i] - IDsimulate[i])**2 for i in range(row))/float(len(IDtarget)))/max(IDtarget) 
print f1

#square = [(IDtarget[i] - IDsimulate[i])**2 for i in range(row)]

#res1 = sum(math.sqrt(square[i])/IDtarget[i] for i in range(row))/len(IDtarget)

#print res1
