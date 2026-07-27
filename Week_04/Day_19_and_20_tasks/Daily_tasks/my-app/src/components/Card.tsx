interface CardProps{
    title:string
    description:string
}

function Card(props: CardProps){
    return(
        <div className="bg-white shadow-lg rounded-xl p-6 w-80 hover:scale-105 transition duration-300">
            <h2 className="text-xl font-bold text-gray-800 mb-3">
                {props.title}
            </h2>
            <p className="text-gray-600">
                {props.description}
            </p>
        </div>        
    )
}

export default Card;