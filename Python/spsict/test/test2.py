lst = list( map( int, input().split(",") ) )
 
def my_sort( lst ):
    l = len( lst )
    temp_lst = lst
    temp = 0
    
    for _ in range( l-1 ) :                
        for j in range( l-1 ) :
            if( lst[j] > lst[j+1] ) :
                temp = lst[j];
                temp_lst[j] = lst[j+1]
                temp_lst[j+1] = temp
                                
        for j in range( l ) :
            lst[j] = temp_lst[j]  
    return lst   


print( my_sort( lst ) )