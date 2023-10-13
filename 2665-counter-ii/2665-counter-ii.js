/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;
    
    const increment = () => { return ++count; }
    const reset = () => { count = init; return count; }
    const decrement = () => { return --count; }
    
    return { increment, decrement, reset }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */