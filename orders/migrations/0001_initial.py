# Generated by Django 5.1.6 on 2025-03-01 09:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название скидки")),
                (
                    "percent",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Процент скидки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Скидка",
                "verbose_name_plural": "Скидки",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Tax",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название налога")),
                (
                    "percent",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Процент налога",
                    ),
                ),
            ],
            options={
                "verbose_name": "Налог",
                "verbose_name_plural": "Налоги",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        editable=False,
                        max_digits=10,
                        null=True,
                        verbose_name="Сумма заказа",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")),
                (
                    "currency",
                    models.CharField(blank=True, editable=False, max_length=3, null=True, verbose_name="Валюта"),
                ),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders.discount",
                        verbose_name="Скидка",
                    ),
                ),
                ("items", models.ManyToManyField(to="items.item", verbose_name="Предметы заказа")),
                (
                    "tax",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="orders.tax",
                        verbose_name="Налог",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ("-id",),
            },
        ),
    ]
