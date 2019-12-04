hash( "Dave" )
print( hash )

hash_table = list( [ 0 for i in range( 8 ) ] )

def get_key( data ):
    return hash( data )

def hash_func( key ):
    return key % 8

def save_data( data, value ):
    hash_address = hash_func( get_key( data ) )
    hash_table[ hash_address ] = value
    
def read_data( data ):
    hash_address = hash_func( get_key( data ) )
    return hash_table[ hash_address ]

save_data( "Dave", "21321312" )
save_data( "Andy", "23211312" )
save_data( "Andrew", "555555" )
save_data( "ohdy", "4444444" )
save_data( "haby", "3333333" )
save_data( "hong", "222222" )
save_data( "ko", "1111111" )
save_data( "la", "999999" )

print( read_data( "Dave" ) )
print( read_data( "Andy" ) )
print( read_data( "Andrew" ) )
print( read_data( "ohdy" ) )
print( read_data( "haby" ) )
print( read_data( "hong" ) )
print( read_data( "ko" ) )
print( read_data( "la" ) )


    