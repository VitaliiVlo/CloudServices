from InstagramAPI import InstagramAPI
from main import save_page_screenshot

LOGIN = "tester_testerenko"
PASS = "testtest"

API = InstagramAPI(LOGIN, PASS)
API.login()

if API.getUserFeed("1234814611"):
    items = API.LastJson["items"][:6]
    for item in items:
        save_page_screenshot(item["id"])
