import os

import stripe

from config import settings


class StripeServices:
    """Сервис для работы с Stripe"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.stripe_api_key = stripe.api_key = settings.STRIPE_API_KEY

    def stripe_create_product(self) -> str:
        """Создание Stripe продукта"""

        product = stripe.Product.create(name=self.name)
        return product.get("id")

    def stripe_create_price(self, product_id: str) -> str:
        """Создание Stripe цены для продукта"""

        price = stripe.Price.create(
            currency="rub",
            unit_amount_decimal=self.price * 100,
            product_data={"name": product_id},
        )
        return price.get("id")

    @staticmethod
    def stripe_create_session(price_id: str) -> str:
        """Создание Stripe сессии"""

        session = stripe.checkout.Session.create(
            success_url=f"http://{os.getenv("HOST")}/success_pay/",
            line_items=[{"price": price_id, "quantity": 2}],
            mode="payment",
        )
        return session.get("id")
