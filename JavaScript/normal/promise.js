// promise : asynchronize 작업을 위한 함수

// function increaseAndPrint( n, callback ) {
//     setTimeout( ( ) => {
//         const increased = n + 1;
//         console.log( increased );
//         if( callback ) {
//             callback( increased );
//         }
//     }, 1000 )
// }
// //  callback 지옥, 지저분해진다.
// increaseAndPrint( 0, (n) => {
//     increaseAndPrint( n, n => {
//         increaseAndPrint( n, n=> {            
//             increaseAndPrint( n, n=> {
//                 increaseAndPrint( n, n=> {
//                     console.log( '작업 끝!' );
//                 })
//             })
//         })
//     })
// } );
console.log( '=======================' );

const myPromise = new Promise( (resolve, reject ) => {
    // 구현
    setTimeout( () => {
        resolve( 'result' );
    }, 1000);
} );


myPromise.then( result => {
    console.log( result );
});