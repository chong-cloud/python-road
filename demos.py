from selenium import webdriver
from selenium.webdriver.support import abstract_event_listener as abel
from selenium.webdriver.support import event_firing_webdriver as efw
from selenium.webdriver.common.by import By
import logging
import py_compile as pp
import sys
import time


class DemoEventListener(abel.AbstractEventListener):
    def on_exception(self, exception, driver):
        print(sys._getframe(1).f_code.co_name)
        print(sys._getframe(2).f_code.co_name)
        print(sys._getframe(3).f_code.co_name)
        # 获取用例所在的文件名
        filename = sys._getframe(3).f_code.co_filename[sys._getframe(3).f_code.co_filename.rindex("/") + 1:-3]
        # 获取用例所在的方法名
        funcname = sys._getframe(3).f_code.co_name
        # 获取出错位置的代码行号
        row = sys._getframe(3).f_lineno
        # 获取当前的时间
        t = time.strftime("%m-%d~%H-%M-%S", time.localtime())
        print(t)
        # 组装成截图文件名
        imagename = filename + "-" + funcname + "-" + str(row) + "-" + str(t) + ".png"
        # 截图操作
        driver.save_screenshot("./aaa/" + imagename)


class testst():
    def bbb(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        return driver

    def aaa(self):
        dr = self.bbb()
        kk = efw.EventFiringWebDriver(dr, DemoEventListener())
        kk.maximize_window()
        kk.find_element(By.ID, "aaaaaaaaaaaaa")


testst().aaa()
pp.compile("demos.py")
