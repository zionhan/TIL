N = 4
array = [ [ 0 for _ in range(N) ] for _ in range(N) ]
k=0
for i in range( N ) :
    for j in range( N ) :
        k+=1
        array[i][j] = k        
temp = [ [ 0 for _ in range(N) ] for _ in range(N) ]                                                                                                                                                                                                                                                                                                                                                     

for i in range( N ) :
    for j in range( N ) :
        if( i in (1,2) and j in (1,2) ) :
            if( j>=i and j<(N-1-i) ) :
                temp[i][j+1] = array[i][j]
            elif( j>i ) :
                temp[i+1][j] = array[i][j]
            elif( i>=j and j>(N-1-i) ) :
                temp[i][j-1] = array[i][j]
            elif( i>j ) :
                temp[i-1][j] = array[i][j] 
            else :
                temp[i][j] = array[i][j]
        else :
            if( j>=i and i>(N-1-j) ) :
                temp[i-1][j] = array[i][j]
            elif( j>i ) :
                temp[i][j-1] = array[i][j]
            elif( i>=j and i<(N-1-j) ) :
                temp[i+1][j] = array[i][j]
            elif( i>j ) :
                temp[i][j+1] = array[i][j] 
                
                
for i in range( N ) :
    for j in range( N ) :
        print( array[i][j], end="\t" )
    print()
            
print()
for i in range( N ) :
    for j in range( N ) :
        print( temp[i][j], end="\t" )
    print()