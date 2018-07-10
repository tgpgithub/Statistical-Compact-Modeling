#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:00:08 2018

@author: user
"""

import Statis_Comp_Modeling
import time


row,ratio,HD = 61,1,0
begin,end,col = 45,106,2
#begin,end,col = 44,105,2

#goaldata = "/home/user/Desktop/Data/goaldata.csv"
#goaldata = "/home/user/Desktop/Data/state0_1_2.csv"
#goaldata = "/home/user/Desktop/Data/statis_varib_state2.csv"
goaldata = "/home/user/Desktop/Data/statis_varib_state2_LD.csv"
outdata = "/home/user/Desktop/Data/outdata20170913"
data = "/home/user/Desktop/Data/data20170913"
outdata1 = "/home/user/Desktop/Data/outdata20171013"
data1 = "/home/user/Desktop/Data/data20171013"
dat = "/home/user/Desktop/Data/gracedata.csv"
sourcefile = "/home/user/Desktop/Data/Statistical_Compact_Model/nmodelcardpomLD18st2"
targetfile = "/home/user/Desktop/Data/Statistical_Compact_Model/nmodelcardpom" 

parameter = ["dvt0","u0","ub","k1"]
#parameter = ["dvt0","u0","ub"]
#parameter = ["dsub","eta0"]#,"vsat"
#parameter = ["nfactor","vth0","u0","voff","ub"]
#parameter = ["dsub","eta0","minv","u0","ub"]
#parameter = ["dvt0","voff","eta0","k1","u0","ub"]
#parameter = ["dsub","eta0","vsat","u0","ub"]
#parameter = ["dsub","eta0","vsat","cdscd","ub"]
#parameter = ["eta0","vsat","cdscd"]
#[" vth0 "] = 0.213313  [" ua "] = 1.07729e-09   [" eta0 "] = 0.31926    ["voff "] = -0.0836792
#[" nfactor "] = 0.940901    [" vsat "] = 137323
#rangeofgene =([[1.78,1.82],[6.2,6.4],[0.025,0.026],[-0.55,-0.45],[1.03e-19,1.06e-19]])
#rangeofgene =([[1.35,1.55],[18,22],[4,6],[0,0.04],[-7e-20,-3e-20]])
#rangeofgene =([[1.8e-7,2.4e-7],[-3.3,-2.8],[0.1,0.2],[1.4,2.2],[0.009,0.018],[-8e-19,-7.3e-19]])
#rangeofgene = [[0.009,0.018]]
#rangeofgene =([[1.14,1.18],[0.36,0.42],[85000,87000],[0.013,0.019],[-9.7e-19,-8.5e-19]])
#rangeofgene =([[-0.26,-0.24],[0.01,0.012],[-7.3e-19,-7.1e-19]])
#rangeofgene =([[1.15,1.17],[0.38,0.4],[80000,83000]])#st1-2
rangeofgene =([[-0.65,-0.45],[0.009,0.011],[-6.7e-19,-6.5e-19],[1.9,2.1]])
#rangeofgene =([[1,1.6],[0.4,0.8]])#,[81000,84000]
#rangeofgene =([[0.091,0.095],[84000,86000],[1e-5,4e-5]])  
#rangeofgene =([[0.071,0.1],[78000,96000],[1e-5,9e-5]]) 
#rangeofgene =([[0.53,0.57],[0.087,0.092],[84000,86000],[5e-5,7e-5],[-8.6e-19,-8.3e-19]])
#rangeofgene =([[0.43,0.67],[0.077,0.1],[78000,110000],[1e-5,9e-5],[-3.6e-19,-9.3e-19]])
#rangeofgene =[[0.091,0.095],[84000,86000],[1e-5,4e-5]]

if __name__ == "__main__":
    t1 = time.time()
    scm = Statis_Comp_Modeling.Statis_Comp_Modeling(begin, end, col, goaldata, outdata, data, outdata1, data1, row, dat, sourcefile)
    scm.iterator(5, rangeofgene, parameter, sourcefile, targetfile, HD)       
    t2 = time.time()
    print (t2 -t1) 
    
    