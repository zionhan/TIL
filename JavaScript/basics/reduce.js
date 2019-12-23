// reduce( ( accumulator, current ) => accumulator + current, 0 ); Important!!
const numbers = [ 1, 2, 3, 4, 5 ];

const avg = numbers.reduce( ( accumulator, current, index, array ) => {
        if( index === array.length - 1 ) {
            return ( accumulator + current ) / array.length;
        } else {
            return accumulator + current;
        }
    }, 0 )

console.log( avg );

const alphabets = [ 'a', 'a', 'a', 'b', 'c', 'c', 'd', 'e' ];

const counts = alphabets.reduce( ( acc, current ) => {
        if( acc[current] ) {
            acc[current] += 1;
        } else {
            acc[current] = 1;
        }
        return acc;
    }, {} 
)
console.log( counts );


// 10 보다 큰 숫자의 갯수를 반환하는 함수
function countBiggerThanTen( numbers ) {
    const biggerNumbers = numbers.filter( function( number ) { if( number > 10 ) return number; } );
    return biggerNumbers.length ;
}

function countBiggerThanTen2( numbers ) {
    let count = 0
    numbers.forEach( number => {
        if( number > 10 ) {
            count ++
        }
    } );
    return count ;
}

function countBiggerThanTen3( numbers ) {
    const count = numbers.reduce( ( acc, current ) => {
        if( current > 10 ) {
            return acc + 1;            
        } else {
            return acc;
        }
    }, 0 );
    return count;
}

const count = countBiggerThanTen3( [ 1, 2, 3, 5, 10, 20, 30, 40, 50, 60 ] ) ;
console.log( count );