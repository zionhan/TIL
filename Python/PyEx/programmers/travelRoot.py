# DFS / BFS
def solution( tickets ) :
    answer = []
    tickets.sort()
    dic = {}
    for ticket in tickets :
        if ( ticket[0] in dic ) :
            dic[ticket[0]].append( ticket[1] )
        else :
            dic[ticket[0]] = [ticket[1]]
            
    s = []
    s.append( "ICN" )
    
    while( s ) :
        airport = s[-1]
        if( airport not in dic or len( dic[airport] ) == 0 ) :
            answer.append( airport ) 
            s.pop()
        else :
            s.append( dic[airport].pop(0) )
    
    answer.reverse()
    
            
    return answer