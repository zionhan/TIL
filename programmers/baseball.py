def check( case, base ) :
    n, s, b = base
    
    for idx, num in enumerate( case ) :
        ts, tb, idx1 = 0, 0, 0         
        # print( num )
        for i in str(n) :            
            for idx2, k in enumerate( str(num) ) :                
                if( i==k and idx1==idx2 ) :
                    ts += 1                
                if( i==k and idx1!=idx2 ) :
                    tb += 1           
            idx1 += 1
        # print( num, ts, tb )
        if( ts!=s or tb!=b ) :
            case[idx] = 0
            case.remove( 0 )    # 도대체 이걸로는 왜 삭제가 제대로 안되는 것인가??

def solution(baseball):
    answer = 0
    case = []
    for i in range( 1, 10 ) :
        for j in range( 1, 10 ) :
            for k in range( 1, 10 ) :
                num = i*100 + j*10 + k
                if len( set( str( num ) ) ) == 3 :
                    case.append( num )       
    
    for base in baseball :        
        check( case, base )    
    
    print( case )
#     case = set( case )
#     case.remove(0)
#     answer = len( case )
    return answer

#Test Case
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print( solution( baseball ) )