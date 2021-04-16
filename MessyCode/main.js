console.log('Hello World!');

const name = 'Jason';
const age = 27;
const flag = false;
const height = 5.6;

console.log('Type of name', typeof name);
console.log('Type of age', typeof age);
console.log('Type of flag', typeof flag);
console.log('Type of height', typeof height);

let student1 = 'Jane';
var student2 = 'Josh';

let nums = '1,2,3,4,5';
console.log(nums.split(','));

const str = "hello world"
console.log('Str substring: ', str.substring(0, 5));

const integers = new Array(1,2,3,4);
console.log('Integers: ', integers);
const chars = ['aa','bb','cc','dd']
console.log('Chars: ', chars);
console.log('The length is ${chars.length}');
const mix = ['1', 2, true]
console.log({mix});
chars.push('ee');
console.log({chars});
chars.unshift('First to go');
// console.log({chars});
// chars.pop();
// console.log({chars});
chars.splice(1,2);
console.log({chars});

let person = {
    firstName: 'Jason',
    lastName: 'Guan',
    age: 19,
    hobbies: ['movies', 'cooking', 'jogging', 'socialing'],
    address: {
        street: '4500 Richmond Lane',
        city: 'Blacksburg',
        state: 'Virginia'
    }
}
console.log({person});
console.log(person.firstName);
console.log(person.hobbies[2]);
console.log(person.address.street);

person.email = 'jasonguan0107@gmail.com';
console.log({person});


function order(x, y){
    if(x>y){
        let tmp = x;
        x = y;
        y = tmp;
    }
    console.log(tmp==x);
    return [x, y]
}