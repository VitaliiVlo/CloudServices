#!/usr/bin/env python
# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from main import save_page_screenshot
from utils import username_to_id, init_worker
from multiprocessing import Pool
from logger_module import *
from database import Post, get_db
from sqlalchemy.orm import sessionmaker
import settings


if __name__ == "__main__":
    engine = get_db()
    Session = sessionmaker(bind=engine)

    API = InstagramAPI(settings.LOGIN, settings.PASS)
    API.login()

    AUCTION_PROFILE_ID = username_to_id(settings.AUCTION_PROFILE_USERNAME)

    pool = Pool(initializer=init_worker)

    try:
        # TODO while True
        if API.getUserFeed(AUCTION_PROFILE_ID):
            items = API.LastJson["items"][:settings.LAST_ITEMS_LIMIT]

            ids = []
            for item in items:
                session = Session()
                media_id = item["id"]
                comment_count = item["comment_count"]
                existing_post = session.query(Post).filter_by(media_id=media_id).one_or_none()

                if existing_post is None:
                    p = Post(media_id=media_id, comment_count=comment_count)
                    session.add(p)
                    session.commit()
                    ids.append(media_id)
                elif comment_count != existing_post.comment_count:
                    existing_post.comment_count = comment_count
                    session.commit()
                    ids.append(media_id)

            if ids:
                pool.apply_async(save_page_screenshot, args=(ids,)).get(timeout=9999999)
            else:
                logger.debug("No new comments")

            # TODO time.sleep

    except KeyboardInterrupt:
        logger.error("Process stopped manually")
    finally:
        pool.close()
        pool.join()
