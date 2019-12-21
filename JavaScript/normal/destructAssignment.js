// 비구조화 할당( 구조 분해 )
const object = { a: 1 };

const { a, b=2 }  = object;
console.log( a );
console.log( b );
console.log( '------------------------' )
// function print( { a, b=2 } ) {
//     console.log( a );
//     console.log( b );
// }

// print( object );

const animal = {
    name: '멍멍이',
    type: '개'
};

const { name: nickname }  = animal;
console.log( nickname );
console.log( animal ) 
console.log( '------------------------' )

const array = [ 1 ];
// const one = array[0];
// const two = array[1];
const [one, two=3] = array;

console.log( one );
console.log( two );

console.log( '------------------------' )

const deepObject = {
    state: {
        information: {
            name: 'velopert',
            languages: ['korean', 'english', 'chinese']
        }
    },
    value: 5
}

// const{ name, languages } = deepObject.state.information;
// const { value } = deepObject;
const { 
    state : {
        information : {
            name, languages: [firstLang, secondeLang]
        }
    },
    value
} = deepObject;


const extracted = {
    name,
    firstLang, secondeLang,
    value
};
console.log( extracted );
console.log( '------------------------' )


// ... rest 
hello = [ 1, 2, 3, 4, 5 ];
const [ first, second, ...rest ] = hello;
console.log( first );
console.log( second );
console.log( rest );