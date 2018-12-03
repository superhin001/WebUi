# -*- coding: utf-8 -*-
import unittest
import os.path
from Config.config import reportpath
from Config.config import basedir
from Lib import GetTime
from Lib import HTMLTestRunner_PY3
suite = unittest.defaultTestLoader.discover(basedir + '/ApiTest/testcase/')
# unittest.TextTestRunner(verbosity=2).run(suite)
report_file = os.path.join(reportpath+GetTime.getNowTime()+'ApiReport.html')

outfile = open(report_file, "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='LongTest ApiTest Report',
    description='龙腾接口测试实战.'
    )
runner.run(suite)
outfile.close()
# from Lib import send_mail
# send_mail.send_mail_report('test')
