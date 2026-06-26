"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function logMethod(target, propertyKey, descriptor) {
    const originalMethod = descriptor.value;
    descriptor.value = function (...args) {
        console.log(`Calling ${propertyKey} method with arguments ${args.join(",")}`);
        const result = originalMethod.apply(this, args);
        console.log(`Result:${result}`);
        return result;
    };
}
class Calculator {
    add(a, b) {
        const result = a + b;
        return result;
    }
    subtract(a, b) {
        const result = a - b;
        return result;
    }
}
__decorate([
    logMethod
], Calculator.prototype, "add", null);
__decorate([
    logMethod
], Calculator.prototype, "subtract", null);
const calculator = new Calculator();
calculator.add(5, 4);
calculator.subtract(8, 3);
