import React from "react"

const CartItem = () => {
    return (
        <div className="cart__item">
            <div className="cart__item-img">
                <img
                    className="pizza-block__image"
                    src="https://dodopizza-a.akamaihd.net/static/Img/Products/Pizza/ru-RU/b750f576-4a83-48e6-a283-5a8efb68c35d.jpg"
                    alt="Pizza"
                />
            </div>
            <div className="cart__item-info">
                <h3>Сырный цыпленок</h3>
                <p>тонкое тесто, 26 см.</p>
            </div>
            <div className="cart__item-count">
                <div className="button button--outline button--circle cart__item-count-minus">
                    {/*<*/}
                    {/*% include ../../../public/img/plus.svg %>*/}
                </div>
                <b>2</b>
                <div className="button button--outline button--circle cart__item-count-plus">
                    {/*<*/}
                    {/*% include ../../../public/img/plus.svg %>*/}
                </div>
            </div>
            <div className="cart__item-price">
                <b>770 ₽</b>
            </div>
            <div className="cart__item-remove">
                <div className="button button--outline button--circle">
                    {/*<*/}
                    {/*% include ../../../public/img/plus.svg %>*/}
                </div>
            </div>
        </div>
    )
}

export default CartItem
