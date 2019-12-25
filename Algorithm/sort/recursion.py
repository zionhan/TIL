# 재귀 호출은 스택의 전형적인 예
# 파이썬에서 재귀 함수는 깊이가 1000회 이하가 되어야 함. 스택 공간이 한정돼 있다는 의미.
def factorial( num ):
    if num > 1 :
        return num * factorial( num-1 )
    else :
        return num
    
for num in range( 10 ) :
    print( factorial( num ) )


def factorial2( num ):
    if num <= 1 :
        return num
    return num * factorial( num-1 )

for num in range( 10 ) :
    print( factorial2( num ) )
print( '======================' )
    
# 재귀 용법 활용한 연습
def multiple( num ): 
    if num > 1 :
        return num * multiple( num-1 )
    else :
        return 1
    
print( multiple( 4 ) )
print( '======================' )

import random
data = random.sample( range(100), 10 )

def sum_list( data ):
    if len(data) > 1 :
        return data[0] + sum_list( data[1:] )
    else :
        return data[0]

print( data )
print( sum_list( data ) )
print( '======================' )


def palindrome( string ):
#     print( string )
#     if len(string) <= 1 :
#         return True
#     
#     if string[0] == string[-1] :
#         return palindrome( string[1:-1] )            
#     else :
#         return False    
    
    if len(string) > 1 :
        if( string[0] == string[-1] ) :
            return palindrome( string[1:-1] )            
        else :
            return False
    else :
        return True
    
print( palindrome( "ledvel" ) )
# string = 'level'
# print( string[0] )
# print( string[-1] )
# print( string[1:-1] )
# print( len(string) )
print( '==================' )

def operation( n ):
    print(n)
    if n == 1 :        
        return n
    
    if n%2 == 1 :                 
        return operation( 3*n+1 )
    else :            
        return operation( n//2  )
    

operation( 3 )



