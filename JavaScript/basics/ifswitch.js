const a = 1;
if( a+1 === 2 )  {
    const a = 2;
    console.log( 'if문 안의 a의 값은 ' + a );
} else if( a===3 ) {
    console.log( 'a+1은 2가 아닙니다.' );
} else {

}
console.log( 'if문 밖의 a의 값은 ' + a)


const device = 'ipad';

switch ( device ) {
    case 'iphone':
        console.log( "iphone" );
        break;
    case 'ipad' :
        console.log( "ipad" );
        break;
    case 'galaxy note' :
        console.log( "galaxy note" );
        break;
    default:
        console.log( "I don't know" );
        break;
}
