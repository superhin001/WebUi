import time
# 获取当前时间另外一种方式是:
nowTime = time.strftime('%Y-%m-%d %X', time.localtime())


def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

