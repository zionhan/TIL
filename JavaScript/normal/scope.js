// scope : 해당 변수 or 함수 유효 범위 
// Global   Function    Block

const value = 'hello!';

// function myFunction() {
//     console.log( 'myFunction : ' );
//     console.log( value );
// }

// function otherFunction() {
//     console.log( 'otherFunction : ' );
//     const value = 'bye!';
//     console.log( value );
// }

// myFunction();
// otherFunction();

// console.log( 'global scope : ' );
// console.log( value )

// function myFunction() {
//     const value = 'bye!';
//     const anotherValue = 'world';
//     function functionInside() {
//         console.log( 'functionInside : ' );
//         console.log( value );
//         console.log( anotherValue );
//     }

//     functionInside();
// }

function myFunction() {
    const value = 'bye!';
    if( true ) {
        const value = 'world';
        console.log( 'block scope : ' );
        console.log( value );
    }
    console.log( 'function scope : ' );
    console.log( value );
}


myFunction();
console.log( 'global scope : ' );
console.log( value );
console.log( '============================' );


// hoisting, 발생하지 않도록 개발을 하자! 헷갈리지 않게, 유지보수를 위해!
// var 은 hoisting 이 존재한다. let, const를 사용해라

myFunction2();

function myFunction2() {
    console.log( 'hello world ' );
}

console.log( number );

var number = 2;

function fn() {
    console.log( a );
    var a = 2;
}
fn();

const myFunction3 = function myFunction3() {
    console.log( 'hello world' );
}
myFunction3();

