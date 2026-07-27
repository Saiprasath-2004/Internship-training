import { useState } from 'react';
// Separate your type imports from your runtime value imports
import type { ChangeEvent, ReactElement } from 'react'; 

function CounterForm(): ReactElement {

  console.log("App Rendered");
  const [count, setCount] = useState<number>(0);
  const [name, setName] = useState<string>('');

  const isEven: boolean = count % 2 === 0;

  // Uses the ChangeEvent utility type correctly
  const handleNameChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setName(e.target.value);
  };

  return (
    <>
      <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
        <label htmlFor="name-input" style={{ display: 'block', marginBottom: '5px' }}>
          Enter Name:
        </label>
        <input 
          id='name-input'
          type="text"
          value={name}
          onChange={handleNameChange} // Attached the typed handler here
          placeholder='Type a name...'
        />
        {name && <p>Hello, {name}!</p>}
      </div>

      <div style={{ paddingLeft: '20px', marginBottom: '10px' }}>
        <button
          type="button"
          className="counter"
          onClick={() => setCount((prev) => prev + 1)}
        >
          Count is {count}
        </button>
        
        {count > 0 && (
          <button 
            type="button" 
            onClick={() => setCount((prev) => prev - 1)}
            style={{ marginLeft: '10px' }}
          >
            -
          </button>
        )} 

        <p style={{ color: isEven ? 'green' : 'red', fontWeight: 'bold' }}>
          The count is {isEven ? 'Even' : 'Odd'}
        </p>
      </div>
    </>
  );
}

export default CounterForm;