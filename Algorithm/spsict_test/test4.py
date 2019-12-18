def count_str( s ):    
    count = 0
    for i in s :
        if( i != '' ) :
            count += 1    
    return count

s = input().split(" ");
print( count_str( s ) )

