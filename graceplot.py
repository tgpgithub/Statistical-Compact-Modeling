#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:41:30 2017

@author: user
"""
import pandas as pd 
import os
import math
import numpy as np

#goaldata = "/home/user/Desktop/Data/goaldata.csv"
goaldata = "/home/user/Desktop/Data/state0_1_2.csv"
#goaldata = "/home/user/Desktop/Data/statis_varib_state2.csv"
outdata = "/home/user/Desktop/Data/outdata20170913"
data = "/home/user/Desktop/Data/data20170913"
dat = "/home/user/Desktop/Data/gracedata.csv"
dat1 = "/home/user/Desktop/Data/gracedata1.csv"
outdata1 = "/home/user/Desktop/Data/outdata20171013"
data1 = "/home/user/Desktop/Data/data20171013"
begin,end,col = 45,106,4
#begin,end,col = 44,105,2

def getData(goaldata,data,dat,outdata,col):
     
    VG = pd.read_table(goaldata,usecols=[1]) 
    ID_TCAD = pd.read_table(goaldata,usecols=[col])     
    #ID_Compac_mod = pd.read_table(outdata,nrows=61,skiprows=[i for i in range(44)],usecols=[2],header=None)
    ID_Compac_mod = pd.read_table(outdata,nrows=61,skiprows=[i for i in range(45)],usecols=[2],header=None)
    '''
    ID_TCAD1 = pd.DataFrame(np.zeros((len(VG),1)), columns=[0])
    ID_Compac_mod1 = pd.DataFrame(np.zeros((len(VG),1)), columns=[0])
    
    for i in range(len(ID_TCAD)):
        ID_TCAD1.values[i] = math.log10(ID_TCAD.values[i])
    for i in range(len(ID_Compac_mod)):    
        ID_Compac_mod1.values[i] = math.log10(-ID_Compac_mod.values[i])
    '''
    #data = pd.concat([VG,ID_TCAD,-ID_Compac_mod,ID_TCAD1,ID_Compac_mod1],axis=1)
    data = pd.concat([VG,ID_TCAD,-ID_Compac_mod],axis=1)
    data.to_csv(dat,index=False,header=False,sep='\t')

def xmgracePlot():
    os.system("xmgrace -nxy " + str(dat))
   # os.system("xmgrace -log y -nxy " + str(dat))

getData(goaldata,data,dat,outdata,col)
getData(goaldata,data1,dat1,outdata1,col+1)
#xmgracePlot()