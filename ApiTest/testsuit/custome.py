import unittest
from Config.config import reportpath
import os.path
import time
from Lib import HTMLTestRunner_PY3
from ApiTest.testcase.bindingcard.test_bindingcard import BingdingCard
from Lib import GetTime

suite = unittest.makeSuite(BingdingCard)
report_file = os.path.join(reportpath+GetTime.getNowTime()+'ApiReport.html')

outfile = open(report_file, "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='LongTest ApiTest Report',
    description='龙腾测试实战.'
    )
runner.run(suite)
outfile.close()