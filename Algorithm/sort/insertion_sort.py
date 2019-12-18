# 시간복잡도 O( N^2 ), 시간 복잡도는 항상 최악의 경우의 속도를 의미한다. 적어도 이 정도의 속도는 보장한다는 의미이기 때문.
# 정렬이 거의 되있는 상태에서는 매우 빠른 정렬이 될 수 있다.

import random

def insertion_sort( data ):
    N = len( data )    
    
    for i in range( 1, N ) :
        temp = data[i]
        
        for j in range( i, 0, -1 ):                        
            if( data[j-1] > temp ) :
                data[j] = data[j-1]
                data[j-1] = temp
            else :
                break           
    return

data = random.sample( range(100), 20 );
print( "시작값  : [" + ", ".join(map( str, data ) ) + "]" )
insertion_sort( data )
print( data )