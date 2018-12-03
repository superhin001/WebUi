import unittest, os, sys, time
from Lib import HTMLTestRunner_PY3
from Config.config import basedir
from Lib import GetTime
from Config.config import reportpath

def suite():
    dir_case = unittest.defaultTestLoader.discover(
        basedir + '/AppUITest/testcase/')
    print(dir_case)
    return dir_case

webreport_file = os.path.join(reportpath+GetTime.getNowTime()+'WebUIReport.html')
outfile = open(webreport_file, "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='LongTest WebUITest Report',
    description='龙腾web自动化测试实战.'
    )
runner.run(suite())
outfile.close()

