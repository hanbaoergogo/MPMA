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

    data = response.json()
    option = data['choices'][0]['message']['content']
    return option