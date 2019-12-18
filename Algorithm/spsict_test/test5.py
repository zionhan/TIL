def solution( participant, completion ):
    answer = ""   
    dic_com = {}
    
    for name in completion :
        if( name in dic_com ) :
            dic_com[name] +=1
        else :
            dic_com[name] = 1        
    
    for name in participant :
        if( name not in dic_com or dic_com[name] == 0 ) :
            answer = name
            break                       
        else :
            dic_com[name] -= 1
    
    return answer

participant = ['mislav', 'stanko', 'mislav', 'ana' ]
completion = ['stanko', 'mislav', 'ana' ]

print( solution( participant, completion ) )
