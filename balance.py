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
