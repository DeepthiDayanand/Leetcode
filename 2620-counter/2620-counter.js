/**
 * @param {number} n
 * @return {Function} counter
 */


var createCounter = function(n) {
    let count = n
    
    return function() {
        return count++
    };
};



/** 
 * const counter = createCounter(10)
 * counter() // 10 || here 10 is a hidden state, sort of like a private variable
 * counter() // 11
 * counter() // 12
 */