import json 
import requests
import os

def openai_query(query,instruction):
    #格式{'id': 'chatcmpl-AUUsvzE4u7ZlkxqC29009j8IO3myM', 'object': 'chat.completion', 'created': 1731831925, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'E', 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 54, 'completion_tokens': 1, 'total_tokens': 55, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'system_fingerprint': 'fp_04751d0b65'}
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