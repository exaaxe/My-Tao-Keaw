import requests
import json
import os

webhook_url = 'https://discord.com/api/webhooks/1108963678000250931/VY9NMvl6-MiMVeYstLedixU3cPDy4AvhajNwJdGwGwBXS9Qoyei28-wQuBh978B0ERXE'

data = {
    'content': 'เต่า'
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

if response.status_code == 204:
    print('Message sent successfully!')
else:
    print('Error sending message')
