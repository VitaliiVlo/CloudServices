#!/usr/bin/env python
# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from main import save_page_screenshot
from utils import username_to_id
import settings
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

API = InstagramAPI(settings.LOGIN, settings.PASS)
API.login()
# TODO while True

AUCTION_PROFILE_ID = username_to_id(settings.AUCTION_PROFILE_USERNAME)

if API.getUserFeed(AUCTION_PROFILE_ID):
    items = API.LastJson["items"][:6]
    ids = [item["id"] for item in items]
    # TODO database check (SQLAlchemy)
    save_page_screenshot(ids)

# TODO time.sleep
# TODO if __name__==__main__
