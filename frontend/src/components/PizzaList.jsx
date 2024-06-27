import React, { useEffect, useState } from "react"
import { backendOrigin } from "../app/constants"
import PizzaItem from "./PizzaItem"

const PizzaList = () => {
    let [pizzas, setPizzas] = useState([])

    useEffect(() => {
        fetch(backendOrigin + "/pizzas/")
            .then((resp) => resp.json())
            .then((resp) => {
                setPizzas(resp)
            })
    }, [])

    console.log(pizzas)

    return (
        <>
            {pizzas.map((item) => (
                <PizzaItem key={item.id} {...item} />
            ))}
        </>
    )
}

export default PizzaList
