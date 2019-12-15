const numbers = {
    a: 1, 
    b: 2,
    get sum() {         // getter
        console.log( 'sum 함수가 실행됩니다!' );
        return this.a + this.b;
    }
};

console.log( numbers.sum )
numbers.a = 5;
console.log( numbers.sum )

const dog = {
    _name: '멍멍이',
    set name( value ) {
        console.log( '이름이 바뀝니다.. ' + value )
        this._name = value;
    }
}

console.log( dog._name );
dog.name = 