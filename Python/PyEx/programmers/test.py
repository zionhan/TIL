# 삽질을 많이했다.
# 문제를 똑바로 못읽었다.
# 조합 순열 개념이 제대로 없었다
# 진짜..... 문제를 더 어렵게 생각하고 풀었다.
# 아까 1번도 그랬던거 같은데..... ㄷ ㄷ ㄷ ㄷ  1번 문제는 뭐였더르ㅏ...

from itertools import permutations 
def solution( n, m, k ):
    answer = ""
     
    lst1 = [ "a" for i in range( n ) ]
    lst2 = [ "b" for i in range( m ) ]
    lst = lst1 + lst2
    N = len(lst)
    lst = list( set( permutations( lst, N ) ) )
    lst.sort()
    
    try :
        answer = "".join( lst[k-1] )
        answer = answer.replace( "b", ")" ).replace( "a", "(" )
        return answer
    
    except IndexError :
        return answer
    
print( solution( 9, 5, 10 ) )