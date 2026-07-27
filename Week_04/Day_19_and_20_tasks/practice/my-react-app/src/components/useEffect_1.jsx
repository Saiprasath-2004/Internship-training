import React, { useEffect, useState } from 'react'

function useEffect_1() {
    const [count,setCount] = useState(0);

    useEffect(() =>{
        console.log("Count changed")
    },[count])

    const increase =() => {
        setCount(count+1)
    }
  return (
    <div>
        
        <h2> useEffect_1</h2>
        <div className="bg-white p-5 rounded-lg shadow-lg mt-10">

            <h2>Check Browser Console</h2>
            <button onClick={increase}>Increment</button>
        </div>
        
        
    </div>
  )
}

export default useEffect_1