const array = [ 1,2,3,4,5, 'blabla', {}, 10 ];
console.log( array );
console.log( array[8] );

const objects = [
    { name: '멍멍이' },
    { name: '야옹이' }
]

console.log( objects );
console.log( objects[0] );
console.log( objects[1].name );

objects.push( 
    { name: '멍뭉이' }
)
console.log( objects[2])
console.log( objects.length )



const array2 = [
    1, true,
    { a: 1 },
    [ 1, 2, 3, 4 ]
]

array2.push( 6 );
console.log( array2[1] )