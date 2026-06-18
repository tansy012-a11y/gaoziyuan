import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:0.6b",
        "prompt": "你好",
        "stream": False
    }
)

print(response.json()["response"])