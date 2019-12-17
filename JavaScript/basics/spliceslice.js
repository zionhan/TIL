const numbers = [ 10, 20, 30, 40 ];
const index = numbers.indexOf( 30 );
console.log( index );
const spliced = numbers.splice( index, 2 );  // index 부터 2개 지우겠다.
console.log( spliced );

const sliced = numbers.slice( 0, 2 );
console.log( sliced )