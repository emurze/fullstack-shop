import React from "react"
import Categories from "../components/Categories"
import Sort from "../components/Sort"
import PizzaList from "../components/PizzaList"

const Home = () => {
    return (
        <>
            <div className="content__top">
                <Categories />
                <Sort />
            </div>
            <h2 className="content__title">Все пиццы</h2>
            <div className="content__items">
                <PizzaList />
            </div>
        </>
    )
}

export default Home
