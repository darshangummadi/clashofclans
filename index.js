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

var longestCommonPrefix = function(strs) {
    if(!strs || strs.length === 0){
        return "";
    }
    let minLength = Infinity;

    for (let s of strs){
        if (s.length < minLength){
            minLength = s.length;
        }
    }

    let i = 0;
    while (i < minLength){
        let currentChar = strs[0][i];
        for (let s of strs){
            if (s[i] != currentChar){
                return s.slice(0,i);
            }
        }
        i++;
    }
    return strs[0].slice(0,i);
}

var generate = function(numRows) {
    const rows = [];
    const firstRow = [1];
    rows.push(firstRow);
    for (let i = 1; i < numRows; i++) {
        const prevRow = rows[i-1];
        const newRow = [1];
        for (let j = 1; j < prevRow.length; j++) {
            newRow.push(prevRow[j-1] + prevRow[j]);
        }
        newRow.push(1);
        rows.push(newRow);
    }
    return rows;
};

var lengthOfLongestSubstring = function(s) {
    let l = 0;
    let longest = 0;
    const set = new Set();
    const n = s.length;

    for (let r = 0; r < n; r++){
        while (set.has(s[r])){
            set.delete(s[l]);
            l++;
        }
        set.add(s[r]);
        longest = Math.max(longest, r - l + 1);
    }
    return longest;
}


