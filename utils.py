import json 
import requests
import os

def openai_query(query,instruction):
    Baseurl = ""
    Skey = "xxxxxxxxx" # your API key
    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": f"{instruction}"
            },
            {
                "role": "user",
                "content": f"{query}"
            }
        ]
    })
    url = Baseurl + "/v1/chat/completions"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {Skey}',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # 解析 JSON 数据为 Python 字典
    data = response.json()

    # 获取 content 字段的值
    option = data['choices'][0]['message']['content']
    return option