def solution( priorities, location ):
    answer = 0
    work = []    
      
    for i in range( 0, len(priorities) ) :
        work.append( (i, priorities[i] ) )    
        
    priorities = sorted( priorities, reverse=True )  
    while( work ) :         
        if( work[0][1] == priorities[0] ) :
            answer += 1
            priorities.pop(0)
            temp = work.pop(0)
            if( temp[0] == location ) :                
                break
        else :
            temp = work.pop(0)
            work.append( temp )     
       
    return answer
 
 
priorities = [1, 5, 9, 4, 1, 1 ]
location = 3
print( solution( priorities, location ) )
