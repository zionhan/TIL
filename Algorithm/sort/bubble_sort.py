# 시간 복잡도 O( N^2 )

def bubble_sort( data ):
    N = len( data )
    temp = 0
    
    for i in range( 1, N ) :
        SWAP = False
        for j in range( N-i ) :
            if( data[j] > data[j+1] ) :
                SWAP = True
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp                
        if( not SWAP ) :
            break
    return 


data = [ 5, 6, 2, 1, 7, 4, 3, 8, 10, 9 ]
bubble_sort( data );
print( data )