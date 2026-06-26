"use strict";
class User {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    getName() {
        return this.name;
    }
    getAge() {
        return this.age;
    }
    setName(name) {
        return this.name = name;
    }
    setAge(age) {
        return this.age = age;
    }
}
const user = new User("Alice", 30);
console.log(user.getName());
console.log(user.getAge());
user.setAge(40);
user.setName("chandru");
console.log(user.getName());
console.log(user.getAge());
