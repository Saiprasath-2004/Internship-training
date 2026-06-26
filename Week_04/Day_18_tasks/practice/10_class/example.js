"use strict";
class User {
    firstName;
    lastName;
    age;
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
    greet() {
        return `Hello, ${this.firstName} ${this.lastName}`;
    }
    getAge() {
        return this.age;
    }
}
// Creating instance 
let user1 = new User("John", "Doe", 25);
let user2 = new User("Janhe", "smith", 29);
console.log(user1.greet());
console.log(user2.greet());
console.log(user2.getAge());
