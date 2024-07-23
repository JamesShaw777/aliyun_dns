import requests
from bs4 import BeautifulSoup
import json

def main():
    url = 'https://345673.xyz/'  # 将此URL替换为实际的URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 创建字典存储线路和对应的信息
        data = {
            "CM": [],
            "CT": [],
            "CU": []
        }

        # 找到所有的行
        rows = soup.find_all('tr', class_='line-cm') + soup.find_all('tr', class_='line-ct') + soup.find_all('tr', class_='line-cu')

        for row in rows:
            # 提取信息
            columns = row.find_all('td')
            line = columns[0].text
            ip = columns[1].text
            time = columns[2].text
            delay = columns[3].text
            downloadspeed = columns[4].text

            # 根据线路名称判断对应的key
            if line == "移动":
                key = "CM"
            elif line == "电信":
                key = "CT"
            elif line == "联通":
                key = "CU"
            else:
                continue

            # 添加信息到对应的列表中
            data[key].append({
                "ip": ip,
                "line": key,
                "node": line,
                "delay": delay,
                "downloadspeed": downloadspeed,
                "time": time
            })

        # 创建最终输出的字典
        output = {
            "code": 200,
            "info": data,
            "total": sum(len(v) for v in data.values())
        }

        # 打印JSON格式的结果
        return json.dumps(output, ensure_ascii=False, indent=2)
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"

if __name__ == "__main__":
    main()
