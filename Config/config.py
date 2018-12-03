'''
@author:Longtest
__author__ = 'Longtest'
#官网：http://www.longtest.cn/
'''
import os
import logging
from Lib import GetTime
#WebUI自动化浏览器账户信息
brotype= 2
url= "http://39.104.14.232/ecshop/wwwroot/admin/privilege.php?act=login"
UserName="admin"
PassWord="fengliying123456"



# mysql的数据库的配置
host = "115.28.108.130"
user = "test"
password = "123456"
database = "longtengserver"
port = 3306

# 邮件配置
sender = '260137162@qq.com'  # 发送方
receiver = "260137162@qq.com"        # 接收方,多个收件人以逗号隔开"xx@qq.com,yy@qq.com"
emailusername = "260137162@qq.com"  # 登录邮箱的用户名
emailpassword = "deynljbeluxqbjhh"             # 登录邮箱的密码,请配置自己的
server = "smtp.qq.com"  # smtp服务器


#  项目目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录
datapath = os.path.join(basedir,'Data/')

# 报告目录
reportpath = os.path.join(basedir, 'Report/')

#  日志配置
logdir = os.path.join(basedir, 'Log/')
logpath =os.path.join(logdir, 'log.txt')


logger = logging.getLogger('AutoProject')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logpath, encoding='utf-8')
datafmt = "%Y-%m-%d %H:%M:%S"
fm = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)

logging.getLogger("requests").setLevel(logging.WARNING)
if __name__ == "__main__":
    logger.info('this is test')
    #print(basedir)







conn=dict(host='127.0.0.1',user='root',passwd='server',db='db',charset='utf8')




#app的配置

"""
#设置一个参数来   区别原生应用还是web应用 ,两个值 'web' 'native'
web_or_native = 'native'
android_or_ios = 'android' #android ios

platform_name = 'Android' #iOS
platform_version = '4.3'  #8.1.1
device_name = '6874b676'
app_package = 'com.sankuai.meituan'
app_activity = 'com.sankuai.meituan.activity.MainActivity'
reset_keyboard = 'True'
unicode_keyboard = 'True'

#纯 web 应用 注意：browser_name 与 app_package 和app_activity 只能设一个
browser_name = 'Chrome'
web_server = 'http://localhost:4723/wd/hub'

#ios 要设置app, udid
app = 'com.dangdang.iphone'
udid = '70643e56c1b0f3c3132c44c87e433a48b5531ee6'


"""
import os
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#设置一个参数来   区别原生应用还是web应用 ,两个值 'web' 'native'
web_or_native = 'native'
android_or_ios = 'android' #android ios

platform_name = 'Android' #iOS
platform_version = '4.4.2'  #8.1.1
device_name = '127.0.0.1:62001'#'6874b676'
app_package = 'com.dangdang.buy2'
app_activity = 'com.dangdang.buy2.activity.ActivityMainTab'
reset_keyboard = 'True'
unicode_keyboard = 'True'

#纯 web 应用 注意：browser_name 与 app_package 和app_activity 只能设一个
browser_name = 'Chrome'
web_server = 'http://localhost:4723/wd/hub'

#ios 要设置app, udid
app = 'com.dangdang.iphone' #desired_caps['app'] = os.path.abspath('/Users/.../TestAutomation.app')
udid = '70643e56c1b0f3c3132c44c87e433a48b5531ee6'
app_android = '../app/dangdang.apk'