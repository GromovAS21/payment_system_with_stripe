import os
from typing import Optional, Union

import stripe


class StripeServices:
    """Сервис для работы с Stripe"""

    def __init__(
        self,
        name: str,
        price: float,
        currency: str,
        discount: Union[int, None] = None,
        tax: Union[int, None] = None,
    ):
        self.name = name
        self.price = price
        self.currency = currency
        self.discount = discount
        self.tax = tax
        self.__stripe_api_key = stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def stripe_create_price(self) -> Optional[str]:
        """Создание Stripe цены для продукта"""
        price = stripe.Price.create(
            currency=self.currency,
            unit_amount_decimal=self.price * 100,
            product_data={"name": self.name},
        )
        return price.get("id")

    def stripe_create_coupon(self) -> Optional[str]:
        """Создание купона для скидки"""
        if self.discount is not None:
            coupon = stripe.Coupon.create(
                duration="once",
                percent_off=self.discount,
            )
            return coupon.get("id")

    def stripe_create_tax(self) -> Optional[str]:
        """Создание налога"""
        if self.tax is not None:
            tax = stripe.TaxRate.create(
                display_name="НДС",
                percentage=self.tax,
                inclusive=False,
            )
            return tax.get("id")

    def stripe_create_session(self) -> Optional[str]:
        """Создание Stripe сессии"""
        price = self.stripe_create_price()
        coupon = self.stripe_create_coupon()
        stripe_session_data = {
            "success_url": f"http://{os.getenv("HOST")}/success_pay/",
            "line_items": [{"price": price, "quantity": 1}],
            "mode": "payment",
            "discounts": [{"coupon": coupon}],
            "tax_id_collection": {"enabled": True},
        }

        if self.tax is not None:
            tax = self.stripe_create_tax()
            stripe_session_data["line_items"][0]["tax_rates"] = [tax]

        try:
            session = stripe.checkout.Session.create(**stripe_session_data)
            return session.get("id")
        except stripe._error.InvalidRequestError as error:
            print(error)
