import React, { useState } from "react"
import PizzaAddButton from "./PizzaAddButton"

const PizzaItem = ({ title, price, sizes, types }) => {
    const [activeSize, setActiveSize] = useState(0)
    const [activeType, setActiveType] = useState(0)
    const typeNames = ["тонкое", "традиционное"]

    return (
        <div className="pizza-block">
            <img
                className="pizza-block__image"
                src="https://dodopizza-a.akamaihd.net/static/Img/Products/Pizza/ru-RU/b750f576-4a83-48e6-a283-5a8efb68c35d.jpg"
                alt="Pizza"
            />
            <h4 className="pizza-block__title">{title}</h4>
            <div className="pizza-block__selector">
                <ul>
                    {types.map((typeId, i) => (
                        <li
                            className={activeType === i ? "active" : ""}
                            key={i}
                            onClick={() => setActiveType(i)}
                        >
                            {typeNames[typeId]}
                        </li>
                    ))}
                </ul>
                <ul>
                    {sizes.map((size, i) => (
                        <li
                            className={activeSize === i ? "active" : ""}
                            key={i}
                            onClick={() => setActiveSize(i)}
                        >
                            {size}
                        </li>
                    ))}
                </ul>
            </div>
            <div className="pizza-block__bottom">
                <div className="pizza-block__price">от {price} ₽</div>
                <PizzaAddButton />
            </div>
        </div>
    )
}

export default PizzaItem
