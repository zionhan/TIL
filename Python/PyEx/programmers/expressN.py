# Dynamic Programming

def solution(N, number):
    answer = -1
    dic = { i : { int( str(N)*i ) } for i in range( 1, 9 ) }
    print( dic )
    
    for i in range( 2, 9 ) :
        for j in range( 1, i ) :
            for value1 in dic[j] :
                for value2 in dic[ i-j ] :
                    dic[i].add( value1 + value2 )
                    dic[i].add( value1 - value2 )
                    dic[i].add( value1 * value2 )
                    if( value2 != 0 ) :
                        dic[i].add( value1 // value2 )
        if( number in dic[i] ) :
            answer = i
            break
        
    return answer