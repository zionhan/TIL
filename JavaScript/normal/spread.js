const slime = {
    name : '슬라임'    
};

const cuteSlime = {
    // name : '슬라임',
    ...slime,
    attribute : 'cute'
};

const pupleCuteSlime = {
    // name : '슬라임',
    // attribute : 'cute',
    ...cuteSlime,
    color : 'puple'
};

const greenCuteSlime = {
    ...pupleCuteSlime,
    color : 'green'
}

console.log( slime );
console.log( cuteSlime );
console.log( pupleCuteSlime );
console.log( greenCuteSlime );
console.log( slime === cuteSlime );
console.log( '-----------------' );

const animals = [ '개', '고양이', '참새' ];
const anotherAnimals = [...animals, '비둘기' ];
console.log( anotherAnimals );
console.log( '----------------------------' );

function subtract( x, y ) {
    return x-y;
}

const numbers = [ 1, 2 ];
const result = subtract( ...numbers );
console.log( result );

function max( ...nums ) {
    return nums.reduce( ( acc, current ) => {
        if( acc > current ) {
            return acc;
        } else {
            return current;
        }
    }, -1 );
}
const nums = [ 1, 2, 3, 45, 5, 6, 7, 8 ];

const result2 = max( ...nums );
console.log( result2 );




