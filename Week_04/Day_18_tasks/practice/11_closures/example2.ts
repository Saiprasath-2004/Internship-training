function createCounter() {
    let counterValue = 0;

    return {
        increment: function () {
            counterValue ++
        },
        getValue: function () {
            return counterValue;
        }
    };
        
}

const  counter1  = createCounter();
counter1.increment();
console.log(counter1.getValue());
