#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler = logging.FileHandler('log.txt')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)
