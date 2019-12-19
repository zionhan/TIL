//  condition ? true : false

const array = [];
let text = "";

if( array.length === 0 ) {
    text = '배열이 비어있습니다.';
} else {
    text = '배열이 비어있지 않습니다.';
}
console.log( text );

let text2 = array.length === 0 ? '배열 x' : '배열 o';
console.log( text2 );