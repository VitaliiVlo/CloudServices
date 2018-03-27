#!/usr/bin/env python
# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from main import save_page_screenshot
from utils import username_to_id, init_worker
from multiprocessing import Pool
from logger_module import *
import settings


if __name__ == "__main__":
    API = InstagramAPI(settings.LOGIN, settings.PASS)
    API.login()

    AUCTION_PROFILE_ID = username_to_id(settings.AUCTION_PROFILE_USERNAME)

    pool = Pool(initializer=init_worker)

    try:
        # TODO while True
        if API.getUserFeed(AUCTION_PROFILE_ID):
            items = API.LastJson["items"][:settings.LAST_ITEMS_LIMIT]
            ids = [item["id"] for item in items]
            # TODO database check (SQLAlchemy)
            pool.apply_async(save_page_screenshot, args=(ids,)).get(timeout=9999999)
            # TODO time.sleep

    except KeyboardInterrupt:
        logger.error("Process stopped manually")
    finally:
        pool.close()
        pool.join()
