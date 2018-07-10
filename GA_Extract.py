#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:54:17 2018

@author: user
"""


import os
import Plot  
import dealData
import paramerCardUpdate
import GA
import matplotlib.pyplot as plt
import numpy as np
import time
import fitnessFunc

ratio = 1
class GA_Extract():
    def GA_extract(self, rangeofgene, parameter, goaldata, outdata, data, outdata1, data1, dat, begin, row, end, col, HD, sourcefile):     
        
        para = paramerCardUpdate.Parameters1()
        CrossRate = 0.4
        MutationRate = 0.01
        ga = GA.GA(100,100,rangeofgene,CrossRate,MutationRate,15)   
        pop = ga.initPopulation()  
        ft = fitnessFunc.FitnessFunc()
        if HD == 1:
            plot = Plot.Plot()
            os.system("bash /home/user/Desktop/Code/PythonCode/iterngsp20170913.sh")       
            d = dealData.dealData()        
            d.dealdata(goaldata,outdata,data,begin,end,col)        
            os.system("bash /home/user/Desktop/Code/PythonCode/iterngsp20171013.sh")
            d.dealdata(goaldata,outdata1,data1,begin,end,col) 
            #d.dealdata(goaldata,outdata1,data1,begin,end,col+8) 
            VG,IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD = plot.getDataHD(row,ratio,data,data1)               
            fitness = ft.fitnessfuncHD(IDsimulateLD,IDtargetLD,IDsimulateHD,IDtargetHD,row)
            
        elif HD == 0:
            plot = Plot.Plot()
            os.system("bash /home/user/Desktop/Code/PythonCode/iterngsp20170913.sh")       
            d = dealData.dealData()        
            d.dealdata(goaldata,outdata,data,begin,end,col)
            VG,IDsimulate,IDtarget = plot.getDataLD(row,ratio,data)
            fitness = ft.fitnessfuncLD(IDsimulate,IDtarget,row)
            
        result = [] 
        result.append(fitness)
            
        
        for i in range(ga.maxgen):  
                                          
            fitness = ga.getfitness(goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop,HD,sourcefile)               
           #print fitness
            gbestpara,gbestfitness,pbestpara,pbestfitness = ga.getbest(pop,fitness)        
            result.append(gbestfitness.tolist()) 
            newpop,bestpara = ga.select(goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop,HD,sourcefile)
            newpop1 = ga.crossover(newpop)      
            newpop2 = ga.mutation(newpop1)
            newpop2[0] = bestpara  
            pop = newpop2
            #print gbestpara
            for i in range(len(parameter)):
               space =" "
               para.m[space + parameter[i] + space] = gbestpara[i]       
            para.updateCard(sourcefile)
           
        print gbestpara,gbestfitness          
        plt.figure(3)  
        plt.title("Figure3")  
        plt.xlabel("iteration", size=14)  
        plt.ylabel("error", size=14) 
        plt.plot(result) 
        plt.show()
        
        f = open(dat,"w")
        for i in range(len(result)):
            f.write("%s\t%s\n"%(i,result[i])) 
'''    
if __name__ == '__main__':
    t1 = time.time()
    GA_extract()
    t2 = time.time()
    print (t2 -t1)  
'''