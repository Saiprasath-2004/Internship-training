function App(){
  let name: string = "Sai"
  let age: number = 22
  let isLearning: boolean =true

  return (
    <div>
      <h1>hello {name}</h1>
      <p>Age: {age}</p>
      <p>Learning TypeScript: {String(isLearning)}</p>
    </div>
  )
}

export default App;