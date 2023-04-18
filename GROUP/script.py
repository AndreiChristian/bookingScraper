import requests
from bs4 import BeautifulSoup
import UTILS.scraper

fairmont_palace_montreux = {
    "roomTypes": []
}

target_url = "https://www.booking.com/hotel/ch/montreuxpalace.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


test1 = UTILS.scraper.scrape(url=target_url, html_element="a", css_selector="id",
                             css_identifier="room_type_id_6509831", is_nested=True)

# print(test3)

fairmont_palace_montreux["roomTypes"].append(test1)

test4 = UTILS.scraper.scrape(url=target_url, html_element="a", css_selector="id",
                             css_identifier="room_type_id_6509804", is_nested=True)

# print(test3)

fairmont_palace_montreux["roomTypes"].append(test4)



test5 = UTILS.scraper.scrape(url=target_url, html_element="a", css_selector="id",
                             css_identifier="room_type_id_6509805", is_nested=True)

fairmont_palace_montreux["roomTypes"].append(test5)

# print(fairmont_palace_montreux["roomTypes"])

# prco-valign-middle-helper

print(UTILS.scraper.scrape(url=target_url, html_element="span", css_selector="class",
                             css_identifier="prco-valign-middle-helper", is_nested=False)
)


