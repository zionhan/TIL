import hashlib

# SHA-1
data = 'test'.encode()      # == b'test'
hash_object = hashlib.sha1()
hash_object.update( data )  # = b'test' 와 같다. 데이터를 byte 형태로 변형해줘야 한다.
hex_dig = hash_object.hexdigest()
print( hex_dig )


# SHA-256

hash_object = hashlib.sha256()
hash_object.update( data )  # = b'test' 와 같다. 데이터를 byte 형태로 변형해줘야 한다.
hex_dig = hash_object.hexdigest()
print( hex_dig )
print( int( hex_dig, 16 ) )
