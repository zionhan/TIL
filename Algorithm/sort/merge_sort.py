'''
병합정렬( merge sort )
재귀 용법을 활용한 정렬 알고리즘
 1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다
 2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
 3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다
'''
import random

def divide( data ):
    if len(data) <= 1: return data
    left = data[:len(data)//2]
    right = data[len(data)//2:]
    return merge( divide(left), divide(right) ) 

def merge(left, right):    
    lst = []
    left_idx, right_idx = 0, 0    
    while( len(left)>left_idx and len(right)>right_idx ):
        if( left[left_idx] > right[right_idx] ):
            lst.append( right[right_idx] )
            right_idx += 1
        else:
            lst.append( left[left_idx] )
            left_idx += 1
    
    if( left_idx == len(left) ):
        lst.extend( right[right_idx:] )
    else :
        lst.extend( left[left_idx:] )        
    return lst

def merge_sort( data ):
    return divide(data)
    
data = random.sample( range(100), 7 )
print( data )
print( merge_sort(data) )
