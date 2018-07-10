#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 00:44:17 2018
statistical compact modeding
@author: user
"""

import numpy as np
import pandas as pd
import math
from multiprocessing import Process, Pool
import GA_Extract


#进行统计式模型提取
class Statis_Comp_Modeling(object):
    '''
    statistical compact modeding
    '''
    def __init__(self, begin, end, col, goaldata, outdata, data, outdata1, data1, row, dat, sourcefile):   
        #初始化文件读取流的位置 col =  the readed column
        self.begin, self.end, self.col = begin, end, col
        self.goaldata, self.outdata, self.data = goaldata, outdata, data
        self.row, self.outdata1, self.data1 = row, outdata1, data1            
        self.dat, self.sourcefile = dat, sourcefile
    def param_extraction(self, rangeofgene, parameters, HD, col):
        #设置对应参数提取范围
        #parameters = ["eta0","vsat","cdscd"] parameters are dictionary or list, key is the name of parameters
        #,value are the value of parameters 
        ga = GA_Extract.GA_Extract()
        ga.GA_extract(rangeofgene, parameters, self.goaldata, self.outdata, self.data, self.outdata1, 
                      self.data1, self.dat, self.begin, self.row, self.end, col, HD, self.sourcefile)
                
    
    def iterator(self, n_model, rangeofgene, parameters, sourcefile, targetfile, HD):
        # 首先一个一个model 提取 ————之后考虑多进程提取。
        #n_model means the number of models are extracted
        for i in range(n_model):
            self.param_extraction(rangeofgene, parameters, HD, self.col+i)
            if HD == 0:
                with open(targetfile+"LD18st2stv"+str(i),"wb") as fn:
                    fn.write(open(sourcefile,"rb").read())
                    fn.close() 
            else:
                with open(targetfile+"hD18st2stv"+str(i),"wb") as fn:
                    fn.write(open(sourcefile,"rb").read())
                    fn.close() 
'''        
    def run_proc(name):        ##定义一个函数用于进程调用
        for i in range(5):    
            time.sleep(0.2)    #休眠0.2秒
            print 'Run child process %s (%s)' % (name, os.getpid())
         #执行一次该函数共需1秒的时间

if __name__ =='__main__': #执行主进程
    scm = Statis_Comp_Modeling()
    print 'Run the main process (%s).' % (os.getpid())
    mainStart = time.time() #记录主进程开始的时间
    p = Pool(8)           #开辟进程池
    for i in range(16):                                 #开辟14个进程
        p.apply_async(scm.run_proc,args=('Process'+str(i),))#每个进程都调用run_proc函数，
                                                        #args表示给该函数传递的参数。

    print 'Waiting for all subprocesses done ...'
    p.close() #关闭进程池
    p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
    print 'All subprocesses done'
    mainEnd = time.time()  #记录主进程结束时间
    print 'All process ran %0.2f seconds.' % (mainEnd-mainStart)  #主进程执行时间            
'''        
        
        
        