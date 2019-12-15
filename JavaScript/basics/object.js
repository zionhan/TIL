const dogName = '멍멍이';
const dogAge = 2;

console.log( dogName );
console.log( dogAge );

// JSON JavaScript Object Notation( key : value )
const animal = {
    name : "멍멍이",
    age : 2,
    cute : true,
    'key with space' : true,
    sample : {
        a: 1,
        b: 2
    }
}

console.log( animal.age )

const ironMan = {
    name : '토니 스타크',
    actor : '로버트 다우니 주니어',
    alias : '아이언맨'
};

const captainAmerica = {
    name : '스티븐 로저스',
    actor : '크리스 에반스',
    alias : '캡틴 아메리카'
};

//  ES6 부터 제공. 비구조 할당
const{ name } = ironMan;
console.log( name );

function print( { alias, name, actor } ) {
    // const { alias, name, actor } = hero;
    // const text = `${hero.alias}(${hero.name}) 역할을 맡은 배우는 ${hero.actor} 입니다.`;
    const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
    console.log( text );
}

print( captainAmerica );


const dog = {
    name : '멍멍이',
    sound : '멍멍',
    // say : function say() {
    //     console.log( this.sound ),
    say() {
        console.log( this.sound )
    }
}

dog.say()

const cat = {
    name : '야옹이',
    sound : '야옹~'
}

cat.say = dog.say;
cat.say()