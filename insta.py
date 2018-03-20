from InstagramAPI import InstagramAPI
from main import save_page_screenshot
import settings

API = InstagramAPI(settings.LOGIN, settings.PASS)
API.login()
# TODO while True

if API.getUserFeed(settings.AUCTION_PROFILE_ID):
    items = API.LastJson["items"][:6]
    ids = [item["id"] for item in items]
    # TODO database check (SQLAlchemy)
    save_page_screenshot(ids)

# TODO time.sleep
# TODO if __name__==__main__
