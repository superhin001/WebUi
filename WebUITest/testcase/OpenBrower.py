__author__ = 'Longtest'
# http://www.longtest.cn/
from selenium import webdriver
from Config.config import logger
from Config import config
import time

def is_brower(uchar, url):
    if uchar == 1:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(30)
        logger.info("打开了火狐浏览器")
        return driver
    elif uchar == 2:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        logger.info("打开了谷歌浏览器")
        time.sleep(2)
        return driver
    else:
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(30)
        return driver
if __name__ == '__main__':
    url1 = config.url
    broty = config.brotype
    # 函数调用
    is_brower(broty, url1)
