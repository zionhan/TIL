function add( a, b ) {
    return a + b;
}

const sum = add( 1, 2 );
console.log( sum )

function hello( name ) {
    // console.log( 'Hello, ' + name + '!' );    
    return `Hello ${name}!` ;       // ` ` 사용 ${}
}

hello( 'dana' );
const result = hello( 'hando' );
console.log( result )

// ES6  => ECMAScript6 자바스크립트의 버전을 의미

function getGrade( score ) {
    if( score > 90 ) {
        return 'A';        
    } else if( score > 80 ) {
        return 'B';
    } else if( score > 70 ) {
        return 'C';
    } else if( score >= 60 ) {
        return 'D';
    } else {
        return 'F';    
    }
}
const grade = getGrade( 50 );
console.log( grade )