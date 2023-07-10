# Общая информация
***Получение API ключа***

API ключ для доступа к REST сервису Tegro.money можно сгенерировать на странице настроек магазина https://tegro.money/my/shop-settings/

Все данные в запросах к сервису Tegro.money передаются методом POST по протоколу HTTP на адрес https://tegro.money/api/method. Параметры сообщения упаковываются в JSON-объект.

Вместе с запросом необходимо передавать подпись. Подписывать необходимо тело запроса целиком, в том виде, в котором оно отправляется на сервер Банка (после сериализации тела запроса в JSON для отправки по HTTP).

    В каждом запросе необходимо передавать параметр nonce, отличный от предыдущего! Например, можно использовать текущее время в секундах

Используйте для подписи ваш секретный ключ. Сформируйте подпись с алгоритмом SHA-256.

```import json
import time
import hashlib
import hmac
import requests

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': str(int(time.time())),
}

body = json.dumps(data)
sign = hmac.new(api_key.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

url = 'https://tegro.money/api/orders/'

response = requests.post(url, data=body, headers=headers)
print(response.text)
```

# Создание заказа
POST https://tegro.money/api/createOrder/ (Используйте этот метод для получения прямой ссылки на оплату заказа)
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': int(time.time()),
    "currency": "RUB",
    "amount": 1200,
    "order_id": "test order",
    "payment_system": 5,
    "fields": {
        "email": "user@email.ru",
        "phone": "79111231212"
    },
    "receipt": {
        "items": [
            {
                "name": "test item 1",
                "count": 1,
                "price": 600
            },
            {
                "name": "test item 2",
                "count": 1,
                "price": 600
            }
        ]
    }
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/createOrder/", data=body, headers=headers)

print(response.text)
```
***Ответ***
```
{
  "type": "success",
  "desc": "",
  "data": {
    "id": 755555,
    "url": "https://tegro.money/pay/complete/755555/7f259f856e7682a6e98179036a623696/"
  }
}
```
# Список магазинов
POST https://tegro.money/api/shops/ (Получение списка ваших магазинов) <br>
***Пример запроса***
```import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA935149B1E5D852A',
    'nonce': int(time.time()),
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/shops/", data=body, headers=headers)

print(response.text)
```
***Ответ***
```
{
  "type": "success",
  "desc": "",
  "data": {
    "user_id": 1,
    "shops": [
      {
        "id": 1,
        "date_added": "2020-11-03 18:04:07",
        "name": "DEMO1",
        "url": "https://demo1",
        "status": 1,
        "public_key": "D0F98E7DD86BB7500914",
        "desc": "DEMO1 SHOP"
      },
      {
        "id": 2,
        "date_added": "2020-11-03 22:38:58",
        "name": "DEMO2",
        "url": "https://demo2",
        "status": 0,
        "public_key": "1913EA935149B1E5D852A",
        "desc": "DEMO2 SHOP"
      }
    ]
  }
}
```
# Баланс
POST https://tegro.money/api/balance/ (Получение баланса всех кошельков) <br>
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    "shop_id": "1913EA935149B1E5D852A",
    "nonce": 1613435880,
    "currency": "RUB",
    "amount": 1200,
    "order_id": "test order",
    "payment_system": 5,
    "fields": {
        "email": "user@email.ru",
        "phone": "79111231212"
    },
    "receipt": {
        "items": [
        {
            "name": "test item 1",
            "count": 1,
            "price": 600
        },
        {
            "name": "test item 2",
            "count": 1,
            "price": 600
        }
        ]
    }
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/balance/", data=body, headers=headers)

print(response.text)
```
***Ответ***
```
{
  "type": "success",
  "desc": "",
  "data": {
    "user_id": 1,
    "balance": {
      "RUB": "1396.68",
      "USD": "0.00",
      "EUR": "1.23",
      "UAH": "0.00"
    }
  }
}
```
# Проверка заказа
POST https://tegro.money/api/order/ (Получение информации о заказе) <br>
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    "shop_id": "1913EA935149B1E5D852A",
    "nonce": 1613435880,
    "payment_id": "test order"
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/order/", data=body, headers=headers)

print(response.text)
```
***Ответ***
```
{
  "type": "success",
  "desc": "",
  "data": {
    "id": 1232,
    "date_created": "2020-11-14 23:32:37",
    "date_payed": "2020-11-14 23:33:39",
    "status": 1,
    "payment_system_id": 10,
    "currency_id": 1,
    "amount": "64.18000000",
    "fee": "4.00000000",
    "email": "user@site.ru",
    "test_order": 0,
    "payment_id": "Order #17854"
  }
}
```
# Список заказов 
POST https://tegro.money/api/orders/ (Получение информации о заказах) <br>
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': int(time.time()),
    'page': 1
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/orders/", data=body, headers=headers)

print(response.text)
```
***Ответ***
```
{
  "type": "success",
  "desc": "",
  "data": [
    {
      "id": 123,
      "date_created": "2020-11-14 23:32:37",
      "date_payed": "2020-11-14 23:33:39",
      "status": 1,
      "payment_system_id": 10,
      "currency_id": 1,
      "amount": "64.18000000",
      "fee": "4.00000000",
      "email": "user@somesite",
      "test_order": 0,
      "payment_id": "Order #4175"
    },
    {
      "id": 124,
      "date_created": "2020-11-14 23:30:05",
      "date_payed": null,
      "status": 0,
      "payment_system_id": 10,
      "currency_id": 1,
      "amount": "64.18000000",
      "fee": "4.00000000",
      "email": "user2@somesite",
      "test_order": 0,
      "payment_id": "Order #4174"
    }
  ]
}
```
# Создание выплаты
POST https://tegro.money/api/createWithdrawal/ <br>

***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': int(time.time()),
    'currency': 'RUB',
    'account': 'killme',
    'amount': 1200,
    'payment_id': 'argr',
    'payment_system': 5
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/createWithdrawal/", data=body, headers=headers)

print(response.text)
```
# Список выплат
POST https://tegro.money/api/withdrawals/ <br>
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': int(time.time()),
    'page': 1
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/withdrawals/", data=body, headers=headers)

print(response.text)
```
# Проверка выплаты
POST https://tegro.money/api/withdrawal/ <br>
***Пример запроса***
```
import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': int(time.time()),
    'order_id': 'argr',
    'payment_id': 'argrq',
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/withdrawals/", data=body, headers=headers)

print(response.text)
```
# 
