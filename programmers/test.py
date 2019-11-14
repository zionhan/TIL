# def solution( numbers ):
#     answer = ""
#     numbers = list( map( str, sorted( numbers, key=lambda x: str(x)*2 , reverse=True  ) ) )
# #     print( numbers )
#     return str( int( answer.join( numbers ) ) )
# 
# 
# 
# print( solution( [6, 10, 2] ) )
# print( solution( [0,0,0,0] ) )
# print( solution( [600, 603, 2] ) )



# def solution(citations):
#     citations = sorted(citations)
#     print( citations )
#     l = len(citations)
#     for i in range(l):
#         print( citations[i], l-i )
#         
#         if citations[i] >= l-i:            # l-i 자체가 가능한값 최대부터 찾는다는 의미네요.
#             return l-i
#     return 0
# 
# 
# print( solution([3, 0, 6, 1, 5] ) )
# print( "=====================" )
# print( solution( [ 50, 34, 4, 5, 5, 5, 30, 30 ]  ) )



s = 666
k = set( str( s ) ) 
print( len( k ) )

lst = [ 1,21312,0,0,10 ]
lst.remove(0)
print( lst )
