import requests
import requests.utils as utils

# requests核心get，post，head，put，patch，delete等，本质都是使用request方法
# 两种写法同理
# resp = requests.get("https://www.baidu.com")
# resp1 = requests.request("get", "https://www.baidu.com")

# **kwargs参数：params，data（可传文件），json，headers——字典，HTTP定制头，cookies——字典或CookieJar，auth——元组，支持HTTP认证功能，
# timeout——设定超时时间，秒为单位，cert——本地SSL证书路径，files——传输文件，proxies——代理服务器
# 默认为TRUE参数：allow_redirects重定向开关——True/False，stream获取内容立即下载开关——True/False，verigy认证SSL证书开关——True/False

params = {'wd': '长城'}  # params为跟在URL后的参数，接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
kv = {"key1": "value1", "key2": "value2"}
# files——字典类型，传输文件
# fs = {'file': open('aa.txt', "r+")}
# proxies：字典类型，设置访问代理服务器，可以增加登录认证
pxs = {'http': 'http://****', 'https': 'https://***'}

# Case1：get请求
response = requests.get("http://www.baidu.com/s?", params=params, headers=headers)
# Case2:post请求，也可以使用json数据
resp = requests.post("http://www.baidu.com/s?", data=kv, json=None, headers=headers)

# 查看响应内容，response.text 返回的是HTTP响应内容的字符串形式，即，url对应的页面内容
print(response.text)
# 查看响应内容，response.content返回的字节流数据(二进制形式)
print(response.content)
# 查看完整url地址
print(response.url)
# 查看响应头部字符编码
print(response.encoding)
# 查看响应码
print(response.status_code)
# 根据内容分析出的响应内容-编码方式（备选编码方式）
print(response.apparent_encoding)

# 7. 返回CookieJar对象:
cookiejar = response.cookies
# 8. 将CookieJar转为字典：
cookiedict = utils.dict_from_cookiejar(cookiejar)
print("cookie rel : ", cookiedict, " \n ", cookiejar)

# session：这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开
# 1、创建session对象
ssion = requests.session()
# 2. 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 3. 需要登录的用户名和密码
data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}
# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data=data)
# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
res = ssion.get("http://www.renren.com/410043129/profile")
# 6. 打印响应内容
print(res.text)
print(utils.dict_from_cookiejar(res.cookies))