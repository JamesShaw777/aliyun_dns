import requests

# 接口地址
url = "https://api.345673.xyz/get_data"

# 请求体
payload = {
    "key": "o1zrmHAF"
}

# 发出POST请求
response = requests.post(url, json=payload)

# 检查响应状态码
if response.status_code == 200:
    # 打印响应内容
    print("请求成功:", response.json())
else:
    print("请求失败:", response.status_code, response.text)
