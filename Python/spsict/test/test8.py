data = [ 9, 9, 102, 100, 1, 1, 3, 2, 7, 8 ]

def quick_sort( data, start, end ) :    
    if( start >= end ) :
        return
    
    key = start
    low = start + 1
    high = end
    temp = 0
    
    while( low <= high ) :
        while( low <= end and data[key] >= data[low]  ):
            low += 1             
        while( high > start and data[key] <= data[high] ) :
            high -= 1    
        
        if( low > high ) :
            temp = data[start]
            data[start] = data[high]
            data[high] = temp
        else :
            temp = data[high]
            data[high] = data[low]
            data[low] = temp        
    
    print( data ) 
               
    quick_sort( data, start, high-1 )
    quick_sort( data, low, end )    
    return


quick_sort(data, 0, len(data)-1 )

print( data ) 
    
    