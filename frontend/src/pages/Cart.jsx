import React from "react"
import CartItem from "../components/CartItem"
import { Link } from "react-router-dom"

const Cart = () => {
    return (
        <div className="cart">
            <div className="cart__top">
                <h2 className="content__title">Корзина</h2>
                <div className="cart__clear">Очистить корзину</div>
            </div>
            <div className="cart__body">
                <CartItem />
                <CartItem />
                <CartItem />
            </div>
            <div className="cart__bottom">
                <div className="cart__bottom-details">
                    <span>
                        {" "}
                        Всего пицц: <b>3 шт.</b>{" "}
                    </span>
                    <span>
                        {" "}
                        Сумма заказа: <b>900 ₽</b>{" "}
                    </span>
                </div>
                <div className="cart__bottom-buttons">
                    <Link
                        to="/"
                        className="button button--outline button--add go-back-btn"
                    >
                        <span>Вернуться назад</span>
                    </Link>
                    <div className="button pay-btn">
                        <span>Оплатить сейчас</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Cart
