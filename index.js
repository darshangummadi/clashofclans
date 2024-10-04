/**var executeCallback = function(callback){
    console.log("Calling the callback function...");
    callback();  // Executes the passed function
}

executeCallback(function(){
    console.log("Hello from the callback!");
});

console.log(typeof alert) // "undefined"

setTimeout(function(){
    console.log("Hello from the timeout!");
},5000);

function x(z){
    console.log("x");
    z();
}
x(function y(){
    console.log("y");
});**/
function attachEventListeners(){
    let count = 0;
    document.getElementById("clickme")
    .addEventListener("click", function xyz(){
    console.log("Button clicked!", ++count);
    window.open("https://www.google.com");
    });
}
attachEventListeners();

function isPalindrome(str){
    str = str.replace(/[^a-zA-Z0-9]/g,'').toLowerCase();
    const reversedStr = str.split('').reverse().join('');
    return str === reversedStr;
}
const word = "tenet";
console.log(isPalindrome(word));

function isPrime(num){
    if (num <= 1){
        return false;
    }
    if (num === 2){
        return true;
    }
    if (num % 2 == 0){
        return false;
    }
    for (let i=3;i<Math.sqrt(num); i+=2){
        if (num % i == 0){
            return false;
        }
    }
    return true;
}
console.log(isPrime(27));



var obj = JSON.parse('{"name":"John", "age":30}');
console.log(obj);

function setBgGreen() {
    document.body.style.backgroundColor = 'green';
}

function setBgRed() {
    document.body.style.backgroundColor = 'black'
}





