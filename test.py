from appium import webdriver
from selenium import webdriver as b
# 设置appium的配置
desired_caps = {}
desired_caps['platformName'] = 'Android'    # 系统类型 一般 Android 或者 IOS
desired_caps['platformVersion'] = '10.0.0'   # 操作系统版本
desired_caps['deviceName'] = 'JQYNW18928025032'   # 使用的手机或模拟器编号,使用命令 adb devices
desired_caps['appPackage'] = 'com.android.calculator2'   # 使用的apk包名
desired_caps['appActivity'] = '.Calculator'              # App启动名
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  #调用appium的驱动
# 定位元素
driver.find_element_by_name("9").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("8").click()
driver.find_element_by_name("4").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()

bdriver = b.Chrome()

# 退出程序
driver.quit()


