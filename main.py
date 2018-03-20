from selenium import webdriver
from utils import media_id_to_code
from datetime import datetime
import tempfile
import os

BASE_DIR = os.path.dirname(__file__)
IMAGE_EXTENSION = "png"
INSTAGRAM_URL = "https://www.instagram.com/p/%s/"
CHROMIUM_DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"


# TODO: celery or multi threading
# TODO excel table on the GoogleDrive with statistics

def save_page_screenshot(media_ids):
    """
    Makes screenshots of comments and uploads them to Google Drive.
    :param media_ids: list of media ids that have new comments
    :return:
    """
    # open in chrome
    driver = webdriver.Chrome(CHROMIUM_DRIVER_PATH)

    with tempfile.TemporaryDirectory() as temp_dir:
        for media_id in media_ids:
            url = INSTAGRAM_URL % media_id_to_code(media_id)
            driver.get(url)

            driver.execute_script('''
            document.getElementsByClassName('_2pnef')[0].style.visibility = 'hidden';
            var comments = document.getElementsByTagName("ul")[0];
            var i = comments.childNodes.length;
            while(i--)
            comments.appendChild(comments.childNodes[i]);
            ''')

            file_name = "%s.%s" % (media_id, IMAGE_EXTENSION)
            file_path = os.path.join(temp_dir, file_name)
            driver.save_screenshot(file_path)

            # TODO google drive upload
            # TODO change name and description of the file on the GoogleDrive
            # $file->setDescription('Нова ставка '.date("d F Y H:i:s").' from user id'. $from);
            # $file->setMimeType('image/jpeg');
            # $file->setName($name."_".time().".png");

    driver.quit()
