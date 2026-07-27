import React, { useEffect } from 'react'

const Timer = () => {

    useEffect(() =>{
        const timer = setInterval(() =>{
            console.log("Timer is running")
        },1000);

        return () => {
            clearInterval(timer);
            console.log("Timer stopped")
        }
    },[])
  return (
    <div className="bg-white p-5 rounded-lg mt-5 shadow-lg">
        <h2>Timer components</h2>
    </div>
  )
}

export default Timer