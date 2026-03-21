// Factory Function
function createCircle(radius){
    return {
        radius,
        draw: function(){
            console.log('draw');
        }
    }; 
}

const circle = createCircle(1);


//Constructor Function
function Circle(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    }
}
const another = new Circle(1);

//Every Object has constructor property and that reference to the function was used to create that Object

Circle.call({},1)
Circle.apply({},[1,2,3]) //for array

//Functions are objects

/*Bt:
function User(username){
    this.username = username;
    this.login = function(){
        console.log('login');
    }
}
==> Use 'prototype' to get riđ of 'new' */ 

let x = 10;
let y = x;
x = 20;
//Value type: independent ==> stored in variable by value

let a = {value: 10};
let b = a;
a.value = 20;
//Reference type (Object/Array/Function): stored in memory/object 


/*Value Type: Number, String, Boolean, Symbol, undefined, null  ==> Primitives
  Reference Type: Function, Object, Array  ==> Object*/
let number = 10; //number ==> Value type
function increase(number){
    number++;
    return number;
} //copied number to create the copy as parameter for function
increase(number); //Will be undefined if try number = increase(number); ==> Pass by Value
console.log(number); //10

let obj = {value: 10};
function increase(obj){
    obj.value++;
} //point to the same object(adress in memory)
increase(obj); //11

const circle1 = new Circle(10);
circle1.location = {x: 1}; //adding property

const propertyName = 'location';
circle1[propertyName] = {x: 1}; //bracket notation

delete circle1['location']; //deleting property


//Enumerate object
for(let key in circle1){
    if(typeof circle1[key] !== 'function'){
        console.log(key, circle1[key]);
    }
} //

const keys = Object.keys(circle1);
console.log(keys); //Enumerate all the key

if('radius' in circle1){
    console.log('Circle has a radius.');
} //check if the property exists


//Abstraction ==> Hide the details - Show the essentials
function Circle2(radius){

    this.radius = radius;

    let defaultLocation = {x: 0, y: 0}; //Use 'let' to make a local variable  ==> Only available in this function

    let computeOptimumLocation = function(factor){
        //...
    };

    /*this.GetdefaultLocation = function(){
        return defaultLocation;
    },*/

    Object.defineProperty(this,'defaultLocation',{
        get: function(){
            return defaultLocation;
        }, //Getter ==> Read only property
        set: function(value){
            if(!value.x || !value.y){
                throw new Error('Invalid location');
            }

            defaultLocation = value;
        } //Setter 
    })

    this.draw = function(){

        //defaultLocation
        //this.radius
        computeOptimumLocation(0.1);  

        console.log('draw');
    }
} //defaultLocation and computeOptimumLocation are private members
const circle2 = new Circle2(10);
circle2.draw();

/*circle2.GetdefaultLocation(); Use a method to read*/

circle2.defaultLocation = {x: 2, y: 3}; 