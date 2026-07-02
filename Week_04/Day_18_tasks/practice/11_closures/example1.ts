// without closures

let counterValue = 0


function incremenetCounter() {
    counterValue++;
}

function getCounterValue() {
    return counterValue;
}


incremenetCounter();
console.log(getCounterValue());


incremenetCounter();
console.log(getCounterValue());