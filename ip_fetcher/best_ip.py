import json

def get_top_ips(data):
    top_ips = {
        "mobile": [],
        "unicom": [],
        "telecom": []
    }

    # 定义每个线路的键名映射
    key_map = {
        "CM": "mobile",
        "CT": "telecom",
        "CU": "unicom"
    }

    for line, ips in data['info'].items():
        # 按照下载速度排序，取前两个
        top_two_ips = sorted(ips, key=lambda x: float(x['downloadspeed'].replace('MB/s', '')), reverse=True)[:2]
        
        # 只返回IP地址
        top_ips[key_map[line]] = [ip['ip'] for ip in top_two_ips]

    return top_ips