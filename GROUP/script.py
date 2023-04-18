import requests
from bs4 import BeautifulSoup
import UTILS.scraper

target_url = "https://www.booking.com/hotel/ch/montreuxpalace.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


test3 = UTILS.scraper.scrape(url=target_url, html_element="a", css_selector="class",
                             css_identifier="hprt-roomtype-link")

# print(test3)
