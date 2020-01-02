// Promise.All 여러개 promise를 동시에 실행
// promise 중 하나라도 에러가 발생하면 오류가 난다.
// Promise.race 여러개 promise 중 가장 빨리 끝난 promise만 실행
// 가장 빨리 끝난 promise의 에러만 잡는다.

function sleep( ms ) {
    return new Promise( resolve => setTimeout( resolve, ms ) );
}

const getDog = async () => {
    await sleep( 1000 );
    return '멍멍이';
}

const getRabbit = async () => {
    await sleep( 500 );
    return '토끼';
}

const getTurtle = async () => {
    await sleep( 3000 );
    return '거북이';
}

async function process() {
    const start =  Date.now();
    // const results = await Promise.all( [getDog(), getRabbit(), getTurtle()] );
    // const [dog, rabbit, turtle] = await Promise.all( [getDog(), getRabbit(), getTurtle()] );
    const first = await Promise.race( [getDog(), getRabbit(), getTurtle()] );
    // console.log( results );
    // console.log( dog );
    // console.log( rabbit );
    // console.log( turtle );
    console.log( first );
    console.log( Date.now() - start );
}

process()