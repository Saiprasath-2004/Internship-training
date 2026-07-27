import { useEffect, useState } from "react";

import UseEffect_1 from "./components/useEffect_1"
import Timer from "./components/Timer";


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

useEffect(() => {
  console.log("Component loaded");
},[]);


const [show,setShow] = useState(true);



    const numbersCombined = [...numbersOne, ...numbersTwo]
      return (
        <>
          {/* <ul>
            {
              users.map(user => 
                <li key={user.id}> {user.name } is {user.age} years old</li>
              )
            }
          </ul> */}

            {/* <p>{numbersCombined}</p>

            <button onClick={myfunc}>Click me </button> */}


            <UseEffect_1 />
            <div className="p-5 mt-5 bg-white rounded-lg shadow-lg">
                <button className="w-4 p-4 bg-white mt-5" onClick={()=> setShow(!show)}> Toggler Timer </button>

              {show && <Timer /> }
            </div>
              
            
        </>
      )
}


export default App
