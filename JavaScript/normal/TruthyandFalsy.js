// undefined, null, 0, '', NaN, false 은 Falsy한 값.
// Falsy 한 값을 제외하면 모두 Truthy한 값( 빈 [] )

function print( person ) {
    // if( person === undefined || person === null ) {
    //     return;
    // }
    if( !person ) {
        return ;
    }

    console.log( person.name );
}


const person = {
    name : 'John'
};

const person2 = null
print();
print( person2 );
print( person );

const value2 = 1 / 'abdf';
console.log( value2 );

const value = null;
// const truthy = value ? true : false;
const truthy = !!value;

console.log( truthy );