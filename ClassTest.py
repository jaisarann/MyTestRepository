# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:40:57 2018

@author: 595244
"""
import sys
print(sys.path)

#%%

import spyder  #Folder Name

#%%
class ClassTest:
    def main():
        util = Utilities()
        #print('main called')
        print(util.sum(10,3))
        
    if __name__ == '__main__':
        main()
    
        