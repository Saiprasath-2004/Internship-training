"use strict";
class Stack {
    items = [];
    push(item) {
        this.items.push(item);
    }
    pop() {
        return this.items.pop();
    }
}
const numberStack = new Stack();
numberStack.push(1);
numberStack.push(2);
console.log(numberStack.pop());
const stringStack = new Stack();
stringStack.push("Hello");
stringStack.push("World");
console.log(stringStack.pop());
