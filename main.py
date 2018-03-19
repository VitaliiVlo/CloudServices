from selenium import webdriver
from utils import media_id_to_code
from datetime import datetime
import os

BASE_DIR = os.path.dirname(__file__)
IMAGE_EXTENSION = "png"
INSTAGRAM_URL = "https://www.instagram.com/p/%s/"
CHROMIUM_DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"


def save_page_screenshot(media_id):
    # open in chrome
    driver = webdriver.Chrome(CHROMIUM_DRIVER_PATH)
    url = INSTAGRAM_URL % media_id_to_code(media_id)
    driver.get(url)

    driver.execute_script('''
    var comments = document.getElementsByTagName("ul")[0];
    var i = comments.childNodes.length;
    while(i--)
    comments.appendChild(comments.childNodes[i]);
    ''')

    save_name = "%s_%s.%s" % (media_id, datetime.now(), IMAGE_EXTENSION)

    driver.save_screenshot(os.path.join(BASE_DIR, save_name))
    driver.quit()
