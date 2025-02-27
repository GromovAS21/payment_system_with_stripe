import os

import stripe


class StripeServices:
    """Сервис для работы с Stripe"""

    def __init__(self, name: str, price: float, discount: int = None):
        self.name = name
        self.price = price
        self.discount = discount
        self.__stripe_api_key = stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def stripe_create_price(self) -> str:
        """Создание Stripe цены для продукта"""

        price = stripe.Price.create(
            currency="rub",
            unit_amount_decimal=self.price * 100,
            product_data={"name": self.name},
        )
        return price.get("id")

    @staticmethod
    def stripe_create_session(price_id: str) -> str:
        """Создание Stripe сессии"""

        session = stripe.checkout.Session.create(
            success_url=f"http://{os.getenv("HOST")}/success_pay/",
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
        )
        return session.get("id")

    def stripe_create_coupon(self):
        """Создание купона для скидки"""
        coupon = stripe.Coupon.create(
            duration="once",
            percent_off=self.discount,
        )
        return coupon.get("id")
