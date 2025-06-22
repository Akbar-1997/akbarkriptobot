# set_webhook.py

import requests

TOKEN = "7503644452:AAEmuYssvT673f8PyH1vP5u8a_Qxd8IOIdU"

# 🔁 Render'dagi haqiqiy domeningizni yozing:
WEBHOOK_URL = "https://akbarkriptobot.onrender.com/webhook"

res = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(res.json())