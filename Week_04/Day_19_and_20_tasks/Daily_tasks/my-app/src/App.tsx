import Counter from "./components/Counter";
import Card from "./components/Card";
import ItemList from "./components/ItemList";
import { technologies } from "./data/techData";


function App(){

  
  return(
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold text-center mb-10">React tasks</h1>
      <Counter/>

      <div className="mt-12 flex  justify-center gap-5 flex-wrap">
        {technologies.map((tech ,index) => (
          <Card key={index} title={tech.title} description={tech.description}/>
        ))} 
              
      </div>
      <ItemList />
    </div>

    
  )
}

export default App;