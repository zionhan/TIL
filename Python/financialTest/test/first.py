def is_perfect_number( n ):
    sum = 0
    for i in range( 1, n//2+1 ) :
        if( n % i == 0 ) :
            sum += i
            
    if( n != sum ) :
        return False
    
    return True

caseSize = int( input().strip() ) 
for i in range( caseSize ) :
    n = int( input().strip() ) 
    if is_perfect_number( n ) :
        print( "YES" )
    else :
        print( "NO" )
