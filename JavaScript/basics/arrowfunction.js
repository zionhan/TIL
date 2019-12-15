const add = ( a, b ) => { 
    return a + b
}

const add2 = ( a, b ) => a + b;


const hello = ( name ) => {
    console.log( `Hello, ${name}!` );
}

const sum = add( 1, 2 );
const sum2 = add2( 3, 2 );
console.log( sum )
console.log( sum2 )

hello( "hando" )

