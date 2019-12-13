a = int( input() )


if( a % 3 == 0 and a % 5 == 0 ) :
    print( "Hello World" )
elif( a % 3 == 0 ) :
    print( "Hello" )
elif( a % 5 == 0 ) :
    print( "World" )
else :
    print( a )