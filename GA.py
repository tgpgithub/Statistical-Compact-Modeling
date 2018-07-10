# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:01:42 2017

@author: Administrator
"""

import random 
import numpy as np  
import fitnessFunc
 

class GA(object):
    
    def __init__(self, maxgen, sizeofpop, rangeofgene, CrossRate, MutationRate,m): 
                 
        self.maxgen = maxgen                      #最大迭代次数 
        self.sizeofpop = sizeofpop                #种群规模                    
        self.rangeofgene = rangeofgene            #基因的位置的范围限制
        self.crossRate = CrossRate                #交叉概率  
        self.mutationRate = MutationRate          #突变概率
        self.m = m                                #保留最优个体数
        self.k = 0.4
        self.r = 0.3
                                                         
    def initPopulation(self):  
        """初始化种群"""  
        pop = np.zeros((self.sizeofpop,len(self.rangeofgene)))                     
        rangeofgene = []
        for i in range(self.sizeofpop):
            for j in range(len(self.rangeofgene)):
                rangeofgene.append([])
                rangeofgene[j] = self.rangeofgene[j][0]+(self.rangeofgene[j][1]-self.rangeofgene[j][0])*random.uniform(0,1)                                   
                pop[i][j] = rangeofgene[j]                        
        return pop         
    
    def getfitness(self,goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop,HD,sourcefile):
        
        fitnessfunc = fitnessFunc.FitnessFunc()
        fitness = np.zeros(self.sizeofpop)
        for i in range(self.sizeofpop):                                             
            fitness[i] = fitnessfunc.GetFitness(goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop[i],HD,sourcefile) 
        return fitness 
        
     
    def select(self,goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop,HD,sourcefile):
        #选择操作
        fitness = self.getfitness(goaldata,outdata,data,outdata1,data1,begin,row,ratio,end,col,parameter,pop,HD,sourcefile)
        index = fitness.argsort() #argsort 返回从小到大的排列在数组中的索引位置         
        bestpara = pop[index[0]]  #保存这一代中最好的个体
        #选择概率
        '''
        p = []
        for i in range(self.sizeofpop):
            p[i] = (2 - random.uniform(1.5,2) + 2 * (random.uniform(1.5,2) - 1) * (self.sizeofpop - i) / (self.sizeofpop -1)) / self.sizeofpop
        '''
        for i in range(self.m):# m个适应度好的个体
            pop[i] = pop[index[i]]        
            pop[i+self.m] = pop[index[i]]
        for i in range(self.m,self.sizeofpop-self.m):
            pop[i+self.m] = pop[index[i]]            
        newpop = pop
        return newpop,bestpara
    
    def crossover(self,pop):
        newpop = np.zeros((self.sizeofpop,len(self.rangeofgene)))
        for j in range(self.sizeofpop-1):               
            #p1 = random.randint(0,self.sizeofpop)
            #p2 = random.randint(0,self.sizeofpop)
            #list1 = [c for c in combinations(range(self.sizeofpop),2)]#组合排列中的组合操作
            p1, p2 = random.sample(pop, 2)
            #print p1,p2
            #newpop[j] = p1
            #newpop[j+1] = p2
            pc = random.random() 
            a = random.uniform(0,self.r)
            b = random.uniform(0,self.r)
            if pc < self.crossRate:
                for i in range(len(self.rangeofgene)): 
                     
                    p1[i] = ( 1 - a) * p1[i] + b * p2[i]                                                 
                    p2[i] = ( 1 - b) * p2[i] + a * p1[i]
                        
                    if  p1[i] < self.rangeofgene[i][0] or p1[i] > self.rangeofgene[i][1]:
                        p1[i] = self.rangeofgene[i][0]+(self.rangeofgene[i][1]-self.rangeofgene[i][0])*random.uniform(0,1)                       
                    if  p2[i] < self.rangeofgene[i][0] or p2[i] > self.rangeofgene[i][1]:
                        p2[i] = self.rangeofgene[i][0]+(self.rangeofgene[i][1]-self.rangeofgene[i][0])*random.uniform(0,1) 
            
                newpop[j] = p1
                newpop[j+1] = p2
            else:
                newpop[j] = p1
                newpop[j+1] = p2                                        
        return  newpop
            
    def mutation(self,pop):
        newpop = np.zeros((self.sizeofpop,len(self.rangeofgene)))  #数组维数注意一致！！！！！！！！       
        for i in range(self.sizeofpop):
            m1 = random.randint(0,len(self.rangeofgene)-1)
            pm = random.random()
            if pm < self.mutationRate:               
                if  random.randint(0,1) == 0:
                    pop[i][m1] = pop[i][m1] + self.k * (self.rangeofgene[m1][1] - pop[i][m1]) * random.random() 
                if  random.randint(0,1) == 1:
                    pop[i][m1] = pop[i][m1] + self.k * (pop[i][m1] -self.rangeofgene[m1][0]) * random.random() 
            else :
                pop[i] = pop[i] 
        newpop = pop
        return newpop
    
    def getbest(self,pop,fitness):
         
        # 群体最优的基因位置及其适应度值
        gbestpos,gbestfitness = pop[fitness.argmin()].copy(),fitness.min()
        #个体最优的基因位置及其适应度值,使用copy()使得对pos的改变不影响pbestpos，pbestfitness类似
        pbestpos,pbestfitness = pop.copy(),fitness.copy()
    
        return gbestpos,gbestfitness,pbestpos,pbestfitness 
            
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    