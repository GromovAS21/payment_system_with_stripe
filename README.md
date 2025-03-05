# Платежный сервис

_Платежный сервис представляет собой веб-приложение, разработанное на базе Django, с интеграцией платежной системы Stripe. Сервис позволяет администраторам управлять товарами, заказами, скидками и налогами через админ-панель Django, а также обеспечивает возможность оплаты товаров и заказов с учетом примененных скидок и налогов._

---

## Основной функционал

- **Создание товара** через админ-панель Django
- **Создание заказа** через админ-панель Django
- **Создание скидки** для заказа через админ-панель Django
- **Создание налога** для заказа через админ-панель Django
- **Добавление налога и скидки** к заказу
- **Оплата товара и заказа** через интегрированную платежную систему Stripe с учетом скидок и налогов

---

## Технологии и зависимости

- **Python** = "^3.12"
- **Stripe** = "^11.6.0"
- **Django** = "^5.1.6"
- **Django REST Framework** = "^3.15.2"
- **python-dotenv** = "^1.0.1"
- **psycopg2-binary** = "^2.9.10"
- **gunicorn** = "^23.0.0"

---

## Архитектура приложения

### 1. Модели данных

- **Предмет (Item):**
  - Поля: 
  - `ID`, `название`, `описание`, `цена`, `валюта`.
  
- **Заказ (Order):**
  - Поля: `ID`, `предметы`, `цена заказа`, `валюта`, `скидка`, `налог`, `дата создания`.
  
- **Скидка (Discount):**
  - Поля: `ID`, `название`, `процент`.
  
- **Налог (Tax):**
  - Поля: `ID`, `название`, `процент`.

### 2. Эндпоинты

- **Предмет:**
  - `GET item/<int:pk>/` — получение HTML страницы с информацией о предмете и кнопкой "Купить" для перехода на Stripe для оплаты предмета.
  - `GET buy/item/<int:pk>/` — создание сессии Stripe для оплаты предмета (API).

- **Заказ:**
  - `GET order/<int:pk>/` — получение HTML страницы с информацией о заказе и кнопкой "Купить" для перехода на Stripe для оплаты заказа.
  - `GET buy/order/<int:pk>/` — создание сессии Stripe для оплаты заказа (API).

- **Админ-панель:**
  - `GET admin/` — переход в админ-панель Django для создания предмета, заказа.

- **Другие:**
  - `GET success_pay/` — получение HTML при успешной оплате через Stripe.

### 3. Веб-интерфейс

- Страница заказа
- Страница предмета
- Страница успешной оплаты

---

## Валидация данных

### 1. Создание Заказа
- **Предметы в заказе**: Не может быть заказ без предметов.
- **Сумма заказа**: Автоматический подсчет на основании цен предметов в заказе
- **Валюта**: В заказе могут быть предметы только с одинаковой валютой

### 2. Создание Скидки
- **Процент**: Не может быть отрицательным и больше 100

### 3. Создание Налога
- **Процент**: Не может быть отрицательным и больше 100

---

## Установка и запуск

### 1. Клонирование репозитория
   ```bash
   git clone https://github.com/GromovAS21/payment_system_with_stripe.git
   cd payment_system_with_stripe
   ```
### 2. Установка зависимостей

- Установите зависимости с помощью Poetry и активируйте виртуальное окружение:
    ```bash
    poetry install
    poetry shell
    ```

### 3. Настройка переменных окружения

- Переименуйте файл [.env.sample](.env.sample) в [.env](.env.sample) и заполните все переменные в этом файле.

### 4. Создание базы данных и ее заполнение

- Создайте базу данных PostgreSQL;
- Примените после этого команду для применения миграций:
     ```bash
     python manage.py migrate
     ```

### 5. Создание суперпользователя и добавление заявок и предметов в базу данных
   ```bash
   python manage.py csu 
   python manage.py loaddata items.json orders.json
   ```
### 6. Запуск приложения
   - Запуск локально (для разработки)
     ```bash
      python manage.py runserver
     ```
     _Веб-приложение будет доступно по адресу: http://127.0.0.1:8000_


   - Запуск через Docker (веб-сервис)
     - В файле [nginx.conf](nginx.conf) в `server_name` введите IP своего сервера 
       ```bash
       docker-compose up -d --build
       ```
     _Веб-приложение будет доступно по адресу: http://127.0.0.1_

---

## Pre-commit (Для разработки)

В проекте присутствует функция pre-commit, который проверяет код на соответствие стандартам PEP8 состоящие из `isort`,
`black`, `flake8`;

### Запуск Pre-commit

```bash
pre-commit install
git add .pre-commit-config.yaml
```

После этого при попытке создания коммита будет запускаться проверка кода и если все проверки проходят, создается коммит.

Для ручной проверки кода необходимо выполнить команду:

```bash
pre-commit run --all-files
```

#### ВАЖНО!!! ####

Перед коммитом необходимо выполнить одну из следующих команд:

```bash
git add . # Добавляет все файлы в индекс
```

```bash
git add <file_name> # Добавляет указанный файл в индекс
```

---

## Цитата

> "В теории, теория и практика неразделимы. На практике это не так."* - Yoggi Berra

---

Приятного использования! 🚀



