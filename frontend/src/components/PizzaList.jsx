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
    }, []) // FC runs when we firstly were showed on the page.

    return (
        <>
            {pizzas.map((item) => (
                <PizzaItem key={item.id} {...item} />
            ))}
        </>
    )
}

export default PizzaList
