import { useState } from "react";


function App() {
  
 const users = [
  { id: 1, name: 'John', age: 30 },
  { id: 2, name: 'Jane', age: 25 },
  { id: 3, name: 'Bob', age: 35 }
];

const numbersOne = [1, 2, 3];
const numbersTwo = [4, 5, 6];

const myfunc = () => {
  alert("hello world");
  
}

const numbersCombined = [...numbersOne, ...numbersTwo]
  return (
    <div >
      <ul>
        {
          users.map(user => 
            <li key={user.id}> {user.name } is {user.age} years old</li>
          )
        }
      </ul>

        <p>{numbersCombined}</p>

        <button onClick={myfunc}>Click me </button>

    </div>
  )
}


export default App
