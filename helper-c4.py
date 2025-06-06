# helper-c4.py

import sys
import os
import requests
import json

# Получаем API ключ из переменной окружения
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    print("ERROR: Please set ANTHROPIC_API_KEY environment variable.")
    sys.exit(1)

# Собираем промпт из аргумента командной строки
if len(sys.argv) < 2:
    print("Usage: python helper-c4.py \"Your prompt here\"")
    sys.exit(1)

prompt = sys.argv[1]

# Готовим headers для API
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01"
}

# Anthropic API endpoint
url = "https://api.anthropic.com/v1/messages"

# Формируем payload
payload = {
    "model": "claude-3-opus-20240229",  # актуальная модель
    "max_tokens": 4096,
    "temperature": 0.3,
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

# Отправляем запрос
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Парсим ответ
if response.status_code == 200:
    result = response.json()
    message = result['content'][0]['text']
    print(message)  # печатаем результат для Codex или для файла
else:
    print(f"Error {response.status_code}: {response.text}")
