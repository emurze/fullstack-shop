import React, { useEffect, useState } from "react"

const Sort = () => {
    const [isVisible, setIsVisible] = useState(false)
    const [activeIndex, setActiveIndex] = useState(0)
    const options = ["популярности", "цене", "алфавиту"]

    const onClickListItem = (i) => {
        setActiveIndex(i)
        setIsVisible(false)
    }

    useEffect(() => {
        console.log("DID MOUNT")
        return () => {
            console.log("DID UNMOUNT")
        }
    }, [])

    useEffect(() => {
        console.log("DID UPDATE")
    }) // Did Mount

    return (
        <div className="sort">
            <div
                className="sort__label"
                onClick={() => setIsVisible(!isVisible)}
            >
                <svg
                    width="10"
                    height="6"
                    viewBox="0 0 10 6"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M10 5C10 5.16927 9.93815 5.31576 9.81445 5.43945C9.69075 5.56315 9.54427 5.625 9.375 5.625H0.625C0.455729 5.625 0.309245 5.56315 0.185547 5.43945C0.061849 5.31576 0 5.16927 0 5C0 4.83073 0.061849 4.68424 0.185547 4.56055L4.56055 0.185547C4.68424 0.061849 4.83073 0 5 0C5.16927 0 5.31576 0.061849 5.43945 0.185547L9.81445 4.56055C9.93815 4.68424 10 4.83073 10 5Z"
                        fill="#2C2C2C"
                    />
                </svg>
                <b>Сортировка по:</b>
                <span>{options[activeIndex]}</span>
            </div>
            {isVisible && (
                <div className="sort__popup">
                    <ul>
                        {options.map((item, i) => (
                            <li
                                className={activeIndex === i ? "active" : ""}
                                key={i}
                                onClick={() => onClickListItem(i)}
                            >
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default Sort
