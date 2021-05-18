import json

import requests
import copyheaders

req_header = b'''
Host: www.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://www.baidu.com
Connection: keep-alive
'''

req_params = {"wd":"豆瓣源", "tn":"monline_4_dg", "ie":"utf-8"}

resp = requests.get("https://baidu.com", params=req_params, headers=copyheaders.headers_raw_to_dict(req_header))
if 200 == resp.status_code:
    resp.encoding = resp.apparent_encoding
    print(resp.text)
    print(resp.headers)

# 不同的格式一般在表头设置，数据都可以传给data参数，Content-Type设置为application/x-www-form-urlencoded，multipart/form-data，application/json，text/xml
# 传入json格式文本
# requests.post(url='', data=json.dumps({'key1':'value1', 'key2':'value2'}), headers={'Content-Type':'application/json'})
# requests.post(url='', json={{'key1':'value1', 'key2':'value2'}}, headers={'Content-Type':'application/json'})