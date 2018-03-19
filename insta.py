from InstagramAPI import InstagramAPI
from main import save_page_screenshot

LOGIN = "tester_testerenko"
PASS = "testtest"

AUCTION_PROFILE_ID = "1234814611"

API = InstagramAPI(LOGIN, PASS)
API.login()
# TODO while True

if API.getUserFeed(AUCTION_PROFILE_ID):
    items = API.LastJson["items"][:6]
    for item in items:
        # TODO database check
        save_page_screenshot(item["id"])

# TODO time.sleep
