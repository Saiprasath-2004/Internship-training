"use strict";
class Calculator {
    add(a, b) {
        console.log(`Calling add method with arguements ${a} and ${b}`);
        const result = a + b;
        console.log(`Result: ${result}`);
        return result;
    }
    subtract(a, b) {
        console.log(`Calling add method with arguements ${a} and ${b}`);
        const result = a - b;
        console.log(`Result: ${result}`);
        return result;
    }
}
const calculator = new Calculator();
calculator.add(5, 4);
calculator.subtract(8, 3);
