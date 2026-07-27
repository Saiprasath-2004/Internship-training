import type { ReactNode } from "react";

interface CardProps{
    title: string;
    children: ReactNode;
}


export default function Card({title,children}: CardProps){
    return(
        <div style={{
                border: "1px solid #ccc",
                borderRadius: 10,
                padding: 20,
                marginBottom: 20,
            }}
        >
            <h2>{title}</h2>

            <hr />
            {children}
        </div>
    )
}