#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import media_id_to_code, ChromeDriverWrapper
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tempfile
import os
import settings
import logging
import datetime

logger = logging.getLogger(__name__)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

with open("to_execute.js", "r") as file:
    JS_SCRIPT = file.read()


def save_page_screenshot(media_ids):
    """
    Makes screenshots of comments and uploads them to Google Drive.
    :param media_ids: list of media ids that have new comments
    :return:
    """

    now = datetime.datetime.now()

    with ChromeDriverWrapper() as driver:
        with tempfile.TemporaryDirectory() as temp_dir:
            for media_id in media_ids:
                url = settings.INSTAGRAM_URL % media_id_to_code(media_id)
                driver.get(url)
                driver.execute_script(JS_SCRIPT)

                file_name = "{}.{}".format(now.strftime("%d %B %Y %H-%M-%S"), settings.IMAGE_EXTENSION)
                file_path = os.path.join(temp_dir, file_name)
                logger.info("Saving screenshot %s to temp folder", file_name)
                driver.save_screenshot(file_path)

                file_entity = drive.CreateFile()
                file_entity.SetContentFile(file_path)
                file_entity['title'] = file_name
                file_entity.Upload()

                # TODO fix permission bug (not deleting tempdir)
                # TODO excel table on the GoogleDrive with statistics

