#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:29:22 2017

@author: user

画图
@author: Administrator
"""

import math
import pandas as pd
import matplotlib.pyplot as plt

class Plot(object):
    
    def getDataLD(self,row,ratio,data):
        
        VG = []
        IDtarget = []          
        IDsimulate = []          #target and simulated I–V points                                           
        f = pd.read_table(data, header=None)
        '''
        VG = f[1][:row]
        IDtarget = f[2][:row]
        IDsimulate = -f[2][row:]
        '''
        for i in range(row):
            IDtarget.append(f[2][i])
            VG.append(f[1][i])
        IDtarget = [i/ratio for i in IDtarget]    
        
        for i in range(row,row*2):
            IDsimulate.append(f[2][i])
        IDsimulate = [-i for i in IDsimulate]
        
        #IDtarget1 = [math.log10(x) for x in IDtarget]          
        #IDsimulate1 = [math.log10(x) for x in IDsimulate] 
        
        return VG,IDsimulate,IDtarget
    
    def DrawLD(self,VG,IDsimulate,IDtarget,save,saveimg,saveimg1): 
              
       
        plt.figure(num =1,figsize=(9,6))         
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("Id/A", size=20)
       
        target, = plt.plot(VG,IDtarget,'rs',label="TCAD data")
        simulate, = plt.plot(VG,IDsimulate,'k-',label="Compact model")     
        plt.legend(handles=[target, simulate],edgecolor='w',fontsize = 20)  
                          
        plt.ticklabel_format(scilimits=(-1,0))       
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1: # if want to  save image
            fig = plt.gcf() # 'get current figure'
            fig.savefig(saveimg, format='eps', dpi=100)
        plt.show()
         
        plt.figure(num =2,figsize=(9,6))                       
        plt.xlabel("Vg/V", size=20)  
        plt.ylabel("log(Id/A)", size=20)       
        target1, = plt.semilogy(VG,IDtarget,'rs', label="TCAD data")
        simulate1, = plt.semilogy(VG,IDsimulate,'k-',label="Compact model")        
        plt.legend(handles=[target1, simulate1],edgecolor='w',fontsize = 20)                              
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig(saveimg1, format='eps', dpi=100) 
        plt.show()
        
    def getDataHD(self,row,ratio,data,data1):
        
        VG = []
        IDtargetLD = []          
        IDsimulateLD = []          #target and simulated I–V points
        IDtargetHD = []          
        IDsimulateHD = []          #target and simulated I–V points                 
                               
        f = pd.read_table(data, header=None)
        '''
        VG = f[1][:row]
        IDtargetLD = f[2][:row]
        IDsimulateLD = -f[2][row:]
        '''
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
        '''
        IDtargetHD = f1[2][:row]
        IDsimulateHD = -f1[2][row:]
        '''
        for i in range(row):
            IDtargetHD.append(f1[2][i])        
        IDtargetHD = [i/ratio for i in IDtargetHD] 
        
       
        for i in range(row,row*2):
            IDsimulateHD.append(f1[2][i])
        IDsimulateHD = [-i for i in IDsimulateHD]  
        
        #IDtargetHD1 = [math.log10(x) for x in IDtargetHD]          
        #IDsimulateHD1 = [math.log10(x) for x in IDsimulateHD]        
        
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
        #plt.ticklabel_format(scilimits=(-1,0))       
        plt.xticks(size = 20)
        plt.yticks(size = 20)
        if save == 1:
            fig = plt.gcf() # 'get current figure'
            fig.savefig(saveimg3, format='eps', dpi=100) 
        plt.show()   
       
