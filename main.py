import json
from api import get_resolution
from api import update_resolution
from ip_fetcher import getip
from ip_fetcher import best_ip

# 获取 IP 数据
ips_json = getip.main()
ips_data = json.loads(ips_json)
bestip = best_ip.get_top_ips(ips_data)


# 调用 GetResolution 并获取结果
resolution = get_resolution.GetResolution.main([])

# 检查是否有返回结果
if resolution:
    # 提取 response 中的 body 部分
    response_body = resolution.get('body', {})
    # 提取 DomainRecords 部分
    domain_records = response_body.get('DomainRecords', {}).get('Record', [])
    
    # 过滤出 Line 为非 "oversea" 的记录
    filtered_records = [record for record in domain_records if record['Line'] != 'oversea']
    
    for record in filtered_records:
        record_id = record['RecordId']
        rr = record['RR']
        record_type = 'A'
        line = record['Line']

        # 根据 Line 获取相应的 IP 地址列表
        if line in bestip:
            for value in bestip[line]:
                # 更新域名记录
                try:
                    update_resolution.UpdateResolution.update_domain_record(record_id, rr, record_type, value, line)
                    print(f"Updated Record ID: {record_id} with value: {value} for line: {line}")
                except Exception as e:
                    print(f"Failed to update Record ID: {record_id} with value: {value} for line: {line}. Error: {e}")
else:
    print("Error: No response received from GetResolution.main()")
