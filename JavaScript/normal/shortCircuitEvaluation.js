// 단축 평가 논리 계산법 short-circuit Evaluation ★★★

true && true // true
true && false // false
true || true // true
true || false // true


const dog = {
    name: '멍멍이'
};

function getName( animal ) {
    // if( animal ) {
    //     return animal.name;
    // }
    // return undefined;
    return animal && animal.name;
}


const name = getName()
console.log( name );


console.log( true && 'hello' );
console.log( false && 'hello' );
console.log( 'hello' && 'bye' );
console.log( null && 'hello' );
console.log( undefined && 'hello' );
console.log( '' && 'hello' );
console.log( 0 && 'hello' );
console.log( 1 && 'hello' );
console.log( 1 && undefined );

const object = null;
const name2 = object && object.name;
console.log( name2 );

const namelessDog = {
    name : ''
}

function getName( animal ) {
    const name = animal && animal.name;
    // if( !name ) {
    //     return '이름이 없는 동물입니다.';
    // } else {
    //     return name;
    // }
    return name || '이름이 없는 동물입니다.';
}
const name3 = getName( namelessDog );
console.log( name3 );

console.log( false || 'hello' );
console.log( '' || '이름없다' );
console.log( null || '널이다~' );
console.log( undefined || 'defiend 되지 않았다!' ); 
console.log( 0 || '제로다' );
console.log( 1 || '음?' );
console.log( true || '여기 안본다' );