import requests
from bs4 import BeautifulSoup

url = 'https://345673.xyz/'  # 将此URL替换为实际的URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # 创建字典存储线路和对应的IP
    data = {}

    # 找到所有的行
    rows = soup.find_all('tr', class_='line-cm') + soup.find_all('tr', class_='line-ct') + soup.find_all('tr', class_='line-cu')

    for row in rows:
        # 提取线路和IP
        columns = row.find_all('td')
        line = columns[0].text
        ip = columns[1].text

        # 如果线路不在字典中，创建新的列表
        if line not in data:
            data[line] = []
        
        # 添加IP到线路对应的列表中
        data[line].append(ip)

    # 打印结果
    for line, ips in data.items():
        print(f"{line}:")
        for ip in ips:
            print(f"  {ip}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
