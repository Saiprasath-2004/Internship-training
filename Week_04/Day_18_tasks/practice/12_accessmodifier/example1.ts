
class User{
     private name: string;
    private age: number

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    public getName() {
        return this.name;
    }

    public getAge() {
        return this.age;
    }

    public setName(name : string) {
        return this.name =name;
    }

    public setAge(age: number){
        if (age > 0) {
            return this.age= age
        }
        
    }
}

const user = new User("Alice", 30);
console.log(user.getName());
console.log(user.getAge());

user.setAge(40);
user.setName("chandru");

console.log(user.getName());
console.log(user.getAge());
