# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:11:43 2018

@author: 595244
"""
import pandas as pd
from sklearn.model_selection import train_test_split

#%%
class Utilities:
    
    @staticmethod
    def sum(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def loadData(filePath):
        dataset = pd.read_csv(filePath)
        return dataset
    
    def splitData(dataset):
        x_data = dataset.values[:,2:4]
        y_data = dataset.values[:,4]
        return x_data, y_data

    def trainDataSplit(x_data, y_data):
        return train_test_split(x_data, y_data)

    def main():
        #obj = Utilities()
        #print(obj.sum(4,2))
        print(Utilities.sub(3,4))
    #%%

    
    if __name__ == '__main__':
        main()