// shift <-> unshift
const numbers = [ 10, 20, 30, 40 ];
const value = numbers.shift();
numbers.shift();
numbers.shift();
numbers.shift();
console.log( numbers );
numbers.unshift(50);
numbers.unshift(40);
console.log( value );
console.log( numbers );

// pop <-> push
const numbers2 = [ 10, 20, 30, 40 ];
const value2 = numbers2.pop();
numbers2.push( 50 )
console.log( value2 );
console.log( numbers2 );

// concat
const arr1 = [ 1, 2, 3 ];
const arr2 = [ 4, 5, 6 ];
const concated = arr1.concat( arr2 )
console.log( arr1 );
console.log( arr2 );
console.log( concated );

// join : 배열을 활용하여 문자열을 만든다.
const array = [ 1, 2, 3, 4, 5 ];
console.log( array.join(', ') );