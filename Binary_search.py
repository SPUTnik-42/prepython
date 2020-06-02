# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:37:25 2020

@author: ATARAXIA
"""


def binary_search(seq,item):
    begin_index = 0 
    end_index = len(seq ) - 1 
    while begin_index <= end_index :
        mid_pos = (begin_index + end_index) // 2
        mid = seq[mid_pos]
        if mid == item :
            return mid + 1 
        elif item < mid:
            end_index = mid_pos
            
        elif item > mid:
            begin_index = mid_pos
    
    return None 


seq_a = [i for i in range(0,100) if i % 2 == 0]
item_a = 67
print(binary_search(seq_a,item_a))

        
            
            