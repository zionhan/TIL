// function calculateCircleArea( r ) {
//     const radius = r || 1;
//     return Math.PI * radius * radius;
// }

// function calculateCircleArea( r = 1) {    
//     return Math.PI * r * r;
// }

const calculateCircleArea = ( r = 1 ) => Math.PI * r * r

const area = calculateCircleArea(5);
console.log( area )