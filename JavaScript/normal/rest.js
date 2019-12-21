const purpleCuteSlime = {
    name : '슬라임',
    attribute : 'cute',
    color : 'purple'
}

const { color, ...cuteSlime } = purpleCuteSlime;

console.log( color );
console.log( cuteSlime );

const { attribute, ...slime } = cuteSlime;
console.log( slime );
console.log( '---------------------------' );

// ...rest 맨 앞에 올 수 없다.
const numbers = [ 0, 1, 2, 3, 4, 5 ];
const [ one, ...rest ] = numbers;
console.log( one );
console.log( rest );
console.log( '---------------------------' );


// function sum( a, b, c, d, e, f, g ) {
//     return a + b + c + d + e + f + g;
// }
function sum( ...rest ) {
    console.log( rest );
    return rest.reduce( (acc, current) => acc + current, 0 );
}

console.log( sum( 1, 2, 3, 4, 5, 6, 7, 8, 9 ) );

