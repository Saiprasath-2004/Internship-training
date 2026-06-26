interface User{
    firstName: string,
    lastName: string,
    age?: number,
    middleName?:string
}


function greetUser(user: User) {
    return `Hello ${user.firstName} ${user.lastName}`;
}


function logUserDetails(user:User){
    console.log(`User: ${user.firstName} ${user.lastName} Age: ${user.age}`)
}

let user1= {firstName:"JOhn",lastName: "Doe", age: 25};
console.log(greetUser(user1));
logUserDetails(user1)
