

function ItemList(){
    const skills: string[] = [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "TypeScript"
    ];

    return(
        <div className="mt-12">
            <h2 className="text-2xl font-bold text-center mb-6">Tech Skills</h2>

            <div className="flex justify-center gap-4 flex-wrap">
                {
                    skills.map((skill,index) =>{
                        return(
                            <div key={index} className={skill==="React" || skill==="TypeScript" ? "bg-blue-500 text-white shadow-md px-6 py-3 rounded-lg": "bg-white shadow-md px-6 py-3 rounded-lg"} >
                                {skill}
                            </div>
                        )
                    })
                }
            </div>
        </div>  
    )
}

export default ItemList;