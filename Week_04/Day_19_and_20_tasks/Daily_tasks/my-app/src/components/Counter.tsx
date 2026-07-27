import { useState } from "react";

function Counter() {
  const [count, setCount] = useState<number>(0);

  function increase() {
    setCount(count + 1);
  }

  function decrease() {
    if (count>0){
        setCount(count - 1);
    }
    
  }

  return (
    <div className="bg-white shadow-lg rounded-xl p-8 w-96 text-center mx-auto mt-10">

      <h1 className="text-2xl font-bold text-gray-800 mb-4">
        Counter App
      </h1>

      <h2 className="text-4xl font-semibold text-blue-600 mb-6">
        {count}
      </h2>

      <div className="flex justify-center gap-4">

        <button
          className="bg-green-500 hover:bg-green-600 text-white px-5 py-2 rounded-lg transition duration-300"
          onClick={increase}
        >
          Increase
        </button>

        <button
          className="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-lg transition duration-300"
          onClick={decrease}
        >
          Decrease
        </button>

      </div>
    </div>
  );
}

export default Counter;