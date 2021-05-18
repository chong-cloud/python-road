# logging方法，1、logging。error（）,这时的配置文件为baseConfig；2、使用四大组件：logger、handler，filter，formatter
import logging
import logging.handlers as lh
import traceback


class stringFilter(logging.Filter):
    def filter(self, record):
        if record.msg.find('A.B') == -1:
            return True
        return False


dio = {"aa": "123", "bb": "34"}
for it, k in dio.items():
    print(it, "   ", k)

print(dio.keys())
# 1、设置logger的名称
logger = logging.getLogger("gc")
# 确定logger的基础级别为DEBUG
logger.setLevel(logging.DEBUG)
# 2、准备logger日志的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 3、准备日志的目标输出位置，且handler有多个。过滤器、日志格式、日志级别都是在handler中进行编辑的，即handler是配置核心
console = logging.StreamHandler()
# 4、设置日志级别，
console.setLevel(logging.WARNING)
# 5、设置日志的格式
console.setFormatter(formatter)
# 6、将配置好的handler添加到logger中
logger.addHandler(console)

# error以上级别的日志输出到文件中
f_handler = logging.FileHandler("aa_test_python/error.txt")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
f_handler.addFilter(stringFilter())
logger.addHandler(f_handler)


for k in dio.keys():
    logger.warning(dio.get(k))
    logger.error(dio.get(k))
    logger.error("A.B")
    logger.error("A.B.234")
    logger.error("a.b.234")
    logger.error("AB.234")
    logger.error("234.A.B")
print(dio.values())

try:
    x = 1 / 0
except Exception as e:
    print("  HERE   ", traceback.format_exc())
    traceback.print_exc()
    print("*"*50)
    print(e)
    print("*"*50)