function Animal( type, name, sound ) {
    this.type = type;
    this.name = name;
    this.sound = sound;
    // this.say = function() {
    //     console.log( this.sound );
    // }
}

// function say() {
//     console.log( this.sound );
// }


// prototype 객체 생성자로 무언가를 만들었을 때 그걸로 만든 객체들끼리 공유할 수 있는 값이나 함수.늄
Animal.prototype.say = function() {
    console.log( this.sound );
}
Animal.prototype.sharedValue = 1;

// javascript call 함수.
function Dog( name, sound ) {
    Animal.call( this, '개', name, sound );    
}

function Cat( name, sound ) {
    Animal.call( this, '고양이', name, sound );
}

Dog.prototype = Animal.prototype;
// Cat.prototype = Animal.prototype;

const dog = new Dog( '멍멍이', '멍멍' )
const cat = new Cat( '야옹이', '야옹' )

dog.say();
cat.say();
console.log( cat.sharedValue ) ;
console.log( dog.sharedValue ) ;