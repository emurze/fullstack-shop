import React, { useState } from "react"

const Categories = () => {
    const [activeIndex, setActiveIndex] = useState(0)
    const categories = [
        "Все",
        "Мясные",
        "Вегетарианская",
        "Гриль",
        "Острые",
        "Закрытые",
    ]

    return (
        <div className="categories">
            <ul>
                {categories.map((value, index) => (
                    <li
                        className={index === activeIndex ? "active" : ""}
                        key={index}
                        onClick={() => setActiveIndex(index)}
                    >
                        {value}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Categories
