#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 05:09:52 2017

@author: user
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:29:22 2017

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
    
    def getDataHD(self,row,ratio,data,data1):
        
        VG = []
        IDtargetLD = []          
        IDsimulateLD = []          #target and simulated I–V points
        IDtargetHD = []          
        IDsimulateHD = []          #target and simulated I–V points                 
                               
        f = pd.read_table(data, header=None)
        
        for i in range(row):
            IDtargetLD.append(f[2][i])
            VG.append(f[1][i])
        IDtargetLD = [i/ratio for i in IDtargetLD]     
        for i in range(row,row*2):
            IDsimulateLD.append(f[2][i])
        IDsimulateLD = [-i for i in IDsimulateLD]
        
        #IDtargetLD1 = [math.log10(x) for x in IDtargetLD]          
        #IDsimulateLD1 = [math.log10(x) for x in IDsimulateLD] 
        
        f1 = pd.read_table(data1, header=None)
        
        for i in range(row):
            IDtargetHD.append(f1[2][i])             
        IDtargetHD = [i/ratio for i in IDtargetHD]  
        for i in range(row,row*2):
            IDsimulateHD.append(f1[2][i])
        IDsimulateHD = [-i for i in IDsimulateHD]  
        
        #IDtargetHD1 = [math.log10(x) for x in IDtargetHD]          
        #IDsimulateHD1 = [math.log10(x) for x in IDsimulateHD]  ,IDsimulateLD1,IDtargetLD1,IDsimulateHD1,IDtargetHD1      
        
        return VG,IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD
    
    
    def DrawHD(self,VG,IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD,save,saveimg2,saveimg3):
        
        plt.figure(num =1,figsize=(9,6))        
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("Id/A", size=20)        
        target, = plt.plot(VG,IDtargetLD,'rs',label="TCAD data LD")                   
        simulate, = plt.plot(VG,IDsimulateLD,'k-',label="Compact model LD")         
        target1, = plt.plot(VG,IDtargetHD,'gs',label="TCAD data HD")  
        simulate1, = plt.plot(VG,IDsimulateHD,'b-',label="Compact model HD") 
        plt.legend(handles=[target, simulate, target1, simulate1],edgecolor='w',fontsize = 20)
        plt.ticklabel_format(scilimits=(-1,0))       
        plt.xticks(size = 20)
        plt.yticks(size = 20) 
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig(saveimg2, format='eps', dpi=100)        
        plt.show()
        
        plt.figure(num =2,figsize=(9,6))  
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("Id/A", size=20)
        target1, = plt.semilogy(VG,IDtargetLD,'rs',label="TCAD data LD")    
        simulate1, = plt.semilogy(VG,IDsimulateLD,'k-',label="Compact model LD")                       
        target2, = plt.semilogy(VG,IDtargetHD,'gs',label="TCAD data HD")            
        simulate2, = plt.semilogy(VG,IDsimulateHD,'b-',label="Compact model HD")
        plt.legend(handles=[target1, simulate1,target2, simulate2],edgecolor='w',fontsize = 20)
       # plt.ticklabel_format(scilimits=(-1,0))       
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig(saveimg3, format='eps', dpi=100) 
        plt.show()   
        
        
        
        
data ='/home/user/Desktop/Data/data20170913'
data1 = '/home/user/Desktop/Data/data20171013'
saveimg = '/home/user/Desktop/LD100st0res.eps'
saveimg1 = '/home/user/Desktop/LD100st0logres.eps'
saveimg2 = '/home/user/Desktop/HD100st0res.eps'
saveimg3 = '/home/user/Desktop/HD100st0logres.eps' 
save = 0     
plot = plot()
row,ratio = 61,1
VG,IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD = plot.getDataHD(row,ratio,data,data1)    
plot.DrawHD(VG,IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD,save,saveimg2,saveimg3)

res1 = (math.sqrt(sum((IDtargetLD[i] - IDsimulateLD[i])**2 for i in range(row))/len(IDtargetLD)))/max(IDtargetLD)
res2 = (math.sqrt(sum((IDtargetHD[i] - IDsimulateHD[i])**2 for i in range(row))/len(IDtargetHD)))/max(IDtargetHD)
#squareLD = [(IDtargetLD[i] - IDsimulateLD[i])**2 for i in range(row)]
#squareHD = [(IDtargetHD[i] - IDsimulateHD[i])**2 for i in range(row)]

#res1 = sum(math.sqrt(squareLD[i])/IDtargetLD[i] for i in range(row))/len(IDtargetLD)
#res2 = sum(math.sqrt(squareHD[i])/IDtargetHD[i] for i in range(row))/len(IDtargetHD)

print res1,res2,res1+res2
