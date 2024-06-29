import React, { useEffect, useState } from "react"
import { backendOrigin } from "../app/constants"
import PizzaItem from "./PizzaItem"
import Skeleton from "./PizzaItem/Skeleton"

const PizzaList = () => {
    let [pizzas, setPizzas] = useState([])
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        fetch(backendOrigin + "/pizzas/")
            .then((resp) => resp.json())
            .then((resp) => {
                setPizzas(resp)
                setIsLoading(false)
            })
        window.scrollTo(0, 0) // TODO: fix  Test it
    }, []) // FC runs when we firstly were showed on the page.

    return (
        <>
            {isLoading
                ? [...new Array(10)].map((_, idx) => <Skeleton key={idx} />)
                : pizzas.map((item) => <PizzaItem key={item.id} {...item} />)}
        </>
    )
}

export default PizzaList
