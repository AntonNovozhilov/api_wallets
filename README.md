## FastAPI app.

Приложение, которое по REST принимает запросы на пополение и спиание ДС с кошельков. 

ручки:

POST api/v1/wallets/<WALLET_UUID>/operation
действия с кошельком списание или пополнение.

GET api/v1/wallets/{WALLET_UUID}
запросить баланс кошелька по его id 

GET api/v1/wallets
получить все кошельки из базы данных ( доступуно только администратору )

Стек.
Фаст апи, докер, докеркопозе, алембик, пайдантик,поетри,пайтест

установка.

1) клонируйте репозщиторий 
git clone git@github.com:AntonNovozhilov/api_wallets.git

2) 
создайте файл .env 
touch .env

заполните его 

TITLE=API на изменение состояния кошелька.
SECRET=qweqqqq
POSTGRES_PORT=5432
POSTGRES_SERVER=db
POSTGRES_DB=dbitc( название базы )
POSTGRES_USER=postgres ( логин ) 
POSTGRES_PASSWORD=postgres ( пароль )


запустите докерр композе 
docker compose up --build

После чего у вас по адресу http://127.0.0.1:8000/docs будет документация, в которой можно првоерь ручки.
данные тестого администратора
email = "test@test.ru"
password = "test"

данные тестого кошелька
id = 1
balance = 1000
owner = 1

## API для управления кошельками
Приложение на FastAPI, которое по REST-интерфейсу позволяет пополнять и списывать средства с кошельков.

### Эндпоинты
Метод URL	                                   Описание
POST  /api/v1/wallets/{WALLET_UUID}/operation  Пополнение или списание средств с кошелька
GET   /api/v1/wallets/{WALLET_UUID}	           Получить баланс кошелька по его ID
GET	  /api/v1/wallets	                       Получить список всех кошельков (доступно только администратору)

### Стек
- FastAPI
- SQLAlchemy
- Postgres
- Docker & Docker Compose
- Alembic
- Pydantic
- Poetry
- Pytest

### Установка и запуск
Клонируйте репозиторий:

```
git clone git@github.com:AntonNovozhilov/api_wallets.git
cd api_wallets
```

Создайте файл .env в корне проекта:

```
touch .env
```

Заполните .env следующими переменными:

```
TITLE=API на изменение состояния кошелька
SECRET=qweqqqq
POSTGRES_PORT=5432
POSTGRES_SERVER=db
POSTGRES_DB=dbitc             # Название базы данных
POSTGRES_USER=postgres        # Логин от PostgreSQL
POSTGRES_PASSWORD=postgres    # Пароль от PostgreSQL

Запустите приложение через Docker:

```
docker compose up --build
```

После запуска документация будет доступна по адресу:
http://127.0.0.1:8000/docs


Тестовые данные

Администратор
Email: test@test.ru
Пароль: test

Кошелёк
ID: 1
Баланс: 1000
Владелец: 1