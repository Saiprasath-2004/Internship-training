"use strict";
class User {
    name;
    static totalUsers = 0;
    constructor(name) {
        this.name = name;
        User.totalUsers++;
    }
    getName() {
        return this.name;
    }
    static getTotalUsers() {
        return User.totalUsers;
    }
}
const user1 = new User("ALice");
const user2 = new User("Bob");
console.log(user1.getName());
console.log(user2.getName());
console.log(User.getTotalUsers());
