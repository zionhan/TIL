import hashlib

hash_table = list( [ 0 for i in range( 8 ) ] )

def get_key( data ):
    hash_object = hashlib.sha256()
    hash_object.update( data.encode() )
    hex_dig = hash_object.hexdigest()
    return int( hex_dig, 16 ) # 16진수 문자열을 10진수로 변환

def hash_func( key ):
    return key % 8

def save_data( data, value ):
    index_key = get_key( data )
    hash_address = hash_func( index_key )
    
    if ( hash_table[hash_address] != 0 ) :
        for index in range( len( hash_table[hash_address] ) ) :
            if ( hash_table[hash_address][index][0] == index_key ):
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append( [index_key, value] )
    else :        
        hash_table[hash_address] = [ [index_key, value] ]    
    
def read_data( data ):
    index_key = get_key( data )    
    hash_address = hash_func( index_key )
    if hash_table[hash_address] != 0 :
        for index in range( len( hash_table[hash_address] ) ) :
            if ( hash_table[hash_address][index][0] == index_key ):
                return hash_table[hash_address][index][1]
        return None
    else :
        return None
        
        

save_data( "Dave", "1220123123" )
save_data( "Dd", "1231234123" )
save_data( "Data", "999999" )

print( hash_table )

print( read_data( "Dave" ) )
print( read_data( "Dd" ) )
print( read_data( "Data" ) )




    