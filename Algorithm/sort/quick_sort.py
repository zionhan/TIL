# 시간복잡도  평균 O( NlogN ) 최악의 경우 O( N^2 ) 
import random

def quick_sort( data, start, end ):
    if( start >= end ) :
        return
    
    low = start + 1
    high = end
    temp = 0
    
    while( low <= high ) : 
        while( low < end and data[low] <= data[start] ) :
            low += 1
            
        while( high > start and data[high] >= data[start]  ) :
            high -= 1
            
        if( low < high ) :
            temp = data[high]
            data[high] = data[low]
            data[low] = temp
        else :
            temp = data[high]
            data[high] = data[start]
            data[start] = temp
    
    quick_sort( data, start, high-1 )
    quick_sort( data, low, end )    
    return


data = random.sample( range(100), 10 )     
quick_sort( data, 0, len( data )-1 )
print( data )