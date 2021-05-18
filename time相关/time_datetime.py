from datetime import datetime, timedelta, timezone
import time

# datetime模块使用
print(datetime.now()), print(datetime.ctime(datetime.now()))
print(datetime(3032, 3, 8, 8))

# 距离1970的基准时间的秒数与时间格式的转换
t = datetime(2018, 3, 8, 8) # 3000年时，会报参数错误，有时间限制？
print(t.timestamp())
print(datetime.fromtimestamp(t.timestamp()))
print("HERE     ", t.timetuple())
print(t.timetz())

# datatime与字符串间转换
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
print(t.strftime("%Y-%m-%d"))

print(datetime.now() + timedelta(hours=10))


# 时区设置，并设置UTC+0:00为基准时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 获取东京的时间，北京时间为hours=8
print(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=9))))


# time模块使用
time.sleep(1)
print(time.strftime("%Y-%m-%d", time.localtime()))
