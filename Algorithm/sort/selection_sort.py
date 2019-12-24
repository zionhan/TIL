# 정렬 알고리즘 만큼 시간 복잡도의 효율성의 차이를 극명하게 보여주는 것이 없다.
# 시간복잡도 O(N^2)
import random

def selection_sort( data ): 
    size = len(data)
    
    for i in range( 0, size-1 ) :
        min = i
        for j in range( i+1, size ) :
            if( data[min] > data[j] ) :
                min = j
        
        temp = data[i]
        data[i] = data[min]
        data[min] = temp
    
    return  
        
    
    
    
data = random.sample( range(100), 10 )      
selection_sort(data)
print( data )
    