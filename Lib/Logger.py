#! /usr/bin/env python
#coding=utf-8
import logging
import logging.config
from Config.config import basedir
class Logger:
    logger = None
    def __init__(self):
        logging.config.fileConfig(basedir+"/Config/logger.conf")
        self.logger = logging.getLogger()
    
    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)
    def error(self,message):
        self.logger.error(message)
    def cri(self,message):
        self.logger.critical(message)

"""
if __name__ =='__main__':
    logyyx = Logger()
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')
"""